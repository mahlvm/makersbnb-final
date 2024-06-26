from lib.login import LoginUser
from lib.login_repository import LoginRepository

def test_can_return_a_user_that_has_signed_up(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = LoginRepository(db_connection)
    login_user = repository.find('test user name', 'test password')
    assert login_user == LoginUser(1, 'test user name', 'test email', 'test password')

    