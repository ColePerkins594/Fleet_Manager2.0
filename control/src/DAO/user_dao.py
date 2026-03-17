from src.helpers.db_tools.enums import user_role, user_status, channel
from src.helpers.db_tools.connection import User, get_session, Contact_Point

class UserDAO:

    @staticmethod
    def fetch_user(account_id: int,first_name: str = None, last_name: str = None, role: user_role = None, status: user_status = None, age: int = None,
                   addr: str = None, phone: str = None, email: str = None, sms: str = None):
        session = get_session().query(User)
        if session is None:
            return None
        if first_name:
            session = session.filter_by(first_name=first_name)
        if last_name:
            session = session.filter_by(last_name=last_name)
        if role:
            session = session.filter_by(role=role.value)
        if status:
            session = session.filter_by(status=status.value)
        if age:
            session = session.filter_by(age=age)
        if addr:
            session = session.filter_by(address=addr)
        if phone or email or sms:
            if phone:
                session = session.filter_by(User.contact_points.any(channel=channel.phone.value, point=phone))
            elif email:
                session = session.filter_by(User.contact_points.any(channel=channel.email.value, point=email))
            elif sms:
                session = session.filter_by(User.contact_points.any(channel=channel.sms.value, point=sms))
        try:
            user = session.query(User).filter_by(account_id=account_id).first()
            return user
        except Exception as e:
            print(f"Error occurred while fetching user: {e}")
            return None
        finally:
            session.close()


    @staticmethod
    def insert_user(first_name: str, last_name: str, role: user_role, status: user_status, age: int, 
                    addr: str, account_id: int, phone: str = None, email: str = None, sms: str = None, preferred_channel: channel = channel.email.value):
        session = get_session()
        if session is None:
            return None
        try:
            new_user = User(
                first_name=first_name,
                last_name=last_name,
                role=role.value,
                status=status.value,
                age=age,
                address=addr,
                account_id=account_id,
            )
            session.add(new_user)
            session.commit()
            if phone:
               phone_point = Contact_Point(
                    user_id=new_user.id,
                    channel=channel.phone.value,
                    point=phone,
                    is_preferred= True if preferred_channel == channel.phone.value else False,
               )
               session.add(phone_point)
            if email:
                email_point = Contact_Point(
                    user_id=new_user.id,
                    channel=channel.email.value,
                    point=email,
                    is_preferred= True if preferred_channel == channel.email.value else False,
                )
                session.add(email_point)
            if sms:
                sms_point = Contact_Point(
                    user_id=new_user.id,
                    channel=channel.sms.value,
                    point=sms,
                    is_preferred= True if preferred_channel == channel.sms.value else False,
                )
                session.add(sms_point)
            session.commit()
            return new_user.id
        except Exception as e:
            print(f"Error occurred while inserting user: {e}")
            session.rollback()
            return None
        finally:
            session.close()

    def update_user(user_id: int, first_name: str = None, last_name: str = None, role: user_role = None, status: user_status = None, age: int = None,
                    addr: str = None, phone: str = None, email: str = None, sms: str = None, preferred_channel: channel = None):
        session = get_session()
        if session is None:
            return False
        try:
            user = session.query(User).filter_by(id=user_id).first()
            if not user:
                print(f"User with id {user_id} not found.")
                return False
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            if role:
                user.role = role.value
            if status:
                user.status = status.value
            if age:
                user.age = age
            if addr:
                user.address = addr
            if phone or email or sms:
                contact_points = session.query(Contact_Point).filter_by(user_id=user_id).all()
                for cp in contact_points:
                    if phone and cp.channel == channel.phone.value:
                        cp.point = phone
                        cp.is_preferred = True if preferred_channel == channel.phone.value else False
                    elif email and cp.channel == channel.email.value:
                        cp.point = email
                        cp.is_preferred = True if preferred_channel == channel.email.value else False
                    elif sms and cp.channel == channel.sms.value:
                        cp.point = sms
                        cp.is_preferred = True if preferred_channel == channel.sms.value else False
            session.commit()
            return True
        except Exception as e:
            print(f"Error occurred while updating user: {e}")
            session.rollback()
            return False
        finally:
            session.close()

    def delete_user(user_id: int):
        session = get_session()
        if session is None:
            return False
        try:
            user = session.query(User).filter_by(id=user_id).first()
            if not user:
                print(f"User with id {user_id} not found.")
                return False
            session.delete(user)
            session.commit()
            return True
        except Exception as e:
            print(f"Error occurred while deleting user: {e}")
            session.rollback()
            return False
        finally:
            session.close()