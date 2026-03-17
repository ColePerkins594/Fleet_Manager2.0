from src.helpers.db_tools.connection import Account, get_session

class AccountDAO:
    @staticmethod
    def fetch_accounts(account_id: int):
        session = get_session()
        if session is None:
            raise ConnectionError("Failed to establish database connection")
        try:
            accounts = session.query(Account).filter_by(account_id=account_id).all()
            return accounts
        except Exception as e:
            print(f"Error occurred while fetching accounts: {e}")
            raise RuntimeError(f"Error occurred while fetching accounts: {e}")
        finally:
            session.close()

    @staticmethod
    def insert_account(account_id: int, account_name: str):
        session = get_session()
        if session is None:
            raise ConnectionError("Failed to establish database connection")
        try:
            new_account = Account(account_id=account_id, name=account_name)
            session.add(new_account)
            session.commit()
            print(f"Inserted account with ID: {account_id}")
        except Exception as e:
            print(f"Error occurred while inserting account: {e}")
            raise RuntimeError(f"Error occurred while inserting account: {e}")
        finally:
            session.close()

    @staticmethod
    def delete_account(account_id: int):
        session = get_session()
        if session is None:
            raise ConnectionError("Failed to establish database connection")
        try:
            account_to_delete = session.query(Account).filter_by(account_id=account_id).first()
            if account_to_delete:
                session.delete(account_to_delete)
                session.commit()
                print(f"Deleted account with ID: {account_id}")
            else:
                print(f"No account found with ID: {account_id}")
        except Exception as e:
            print(f"Error occurred while deleting account: {e}")
            raise RuntimeError(f"Error occurred while deleting account: {e}")
        finally:
            session.close()
    
    @staticmethod
    def update_account(account_id: int, account_name: str = None):
        session = get_session()
        if session is None:
            raise ConnectionError("Failed to establish database connection")
        try:
            account = session.query(Account).filter_by(account_id=account_id).first()
            if account is None:
                print(f"No account found with ID: {account_id}")
                raise ValueError(f"No account found with ID: {account_id}")
            if account_name:
                account.name = account_name
            session.commit()
            print(f"Updated account with ID: {account_id}")
        except Exception as e:
            print(f"Error occurred while updating account: {e}")
            raise RuntimeError(f"Error occurred while updating account: {e}")
        finally:
            session.close()