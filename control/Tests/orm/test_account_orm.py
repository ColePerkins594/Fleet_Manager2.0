from src.helpers.db_tools.connection import get_session, Account
from src.DAO.account_dao import AccountDAO


def test_account_fetch():
    test_id = 1
    accounts = AccountDAO.fetch_accounts(account_id=test_id)
    for account in accounts:
        assert account.account_id == test_id

def test_account_insert():
    account_id = 999
    account_name = "Test Account"
    try:
        AccountDAO.insert_account(account_id=account_id, account_name=account_name)
        accounts = AccountDAO.fetch_accounts(account_id=account_id)
        assert len(accounts) == 1
        account = accounts[0]
        assert account.account_id == account_id
        assert account.name == account_name
    except Exception as e:
        print(f"Error during test_account_insert: {e}")
        assert False, f"Exception occurred: {e}"
    finally:
        try:
            session = get_session()
            if session:
                try:
                    account_to_delete = session.query(Account).filter_by(account_id=account_id).first()
                    if account_to_delete:
                        session.delete(account_to_delete)
                        session.commit()
                except Exception as e:
                    print(f"Error during cleanup in test_insert_vehicle: {e}")
            
        except Exception as e:
            print(f"Error during cleanup in test_account_insert: {e}")
        finally:
                session.close()

def test_account_delete():
    account_id = 999
    account_name = "Test Account"
    try:
        AccountDAO.insert_account(account_id=account_id, account_name=account_name)
        AccountDAO.delete_account(account_id=account_id)
        accounts = AccountDAO.fetch_accounts(account_id=account_id)
        assert len(accounts) == 0
    except Exception as e:
        print(f"Error during test_account_delete: {e}")
        assert False, f"Exception occurred: {e}"
    finally:
        try:
            session = get_session()
            if session:
                try:
                    account_to_delete = session.query(Account).filter_by(account_id=account_id).first()
                    if account_to_delete:
                        session.delete(account_to_delete)
                        session.commit()
                except Exception as e:
                    print(f"Error during cleanup in test_insert_vehicle: {e}")
            
        except Exception as e:
            print(f"Error during cleanup in test_account_insert: {e}")
        finally:
                session.close()

def test_account_update():
    account_id = 999
    account_name = "Test Account"
    updated_account_name = "Updated Test Account"
    try:
        AccountDAO.insert_account(account_id=account_id, account_name=account_name)
        AccountDAO.update_account(account_id=account_id, account_name=updated_account_name)
        accounts = AccountDAO.fetch_accounts(account_id=account_id)
        assert len(accounts) == 1
        account = accounts[0]
        assert account.account_id == account_id
        assert account.name == updated_account_name
    except Exception as e:
        print(f"Error during test_account_update: {e}")
        assert False, f"Exception occurred: {e}"
    finally:
        try:
            session = get_session()
            if session:
                try:
                    account_to_delete = session.query(Account).filter_by(account_id=account_id).first()
                    if account_to_delete:
                        session.delete(account_to_delete)
                        session.commit()
                except Exception as e:
                    print(f"Error during cleanup in test_insert_vehicle: {e}")
            
        except Exception as e:
            print(f"Error during cleanup in test_account_insert: {e}")
        finally:
                session.close()