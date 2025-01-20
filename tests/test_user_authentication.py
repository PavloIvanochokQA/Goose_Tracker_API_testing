from config.base_test import BaseTest
import allure
import pytest


@allure.feature("User Authentication")
class TestUserAuthentication(BaseTest):

    @pytest.mark.order(1)
    @allure.title("T01: Create a new user with a valid email, password, and name.")
    def test_create_user(self):
        self.api_user_auth.create_user()

    @pytest.mark.order(2)
    @allure.title("T02: Create a new user with an invalid email.")
    def test_create_user_with_invalid_email(self):
        self.api_user_auth.create_user_with_invalid_email()

    @pytest.mark.order(3)
    @allure.title("T03: Create a new user with an invalid password.")
    def test_create_user_with_invalid_password(self):
        self.api_user_auth.create_user_with_invalid_password()

    @pytest.mark.order(4)
    @allure.title("T04: Create a new user with an already existing email.")
    def test_create_user_with_already_existing_email(self):
        user = self.api_user_auth.create_user()
        self.api_user_auth.create_user_with_already_existing_email(email=user.email)

    @pytest.mark.order(5)
    @allure.title("T05: Create a new user without a password.")
    def test_create_user_without_password(self):
        self.api_user_auth.create_user_without_password()

    @pytest.mark.order(6)
    @allure.title("T06: Create a new user without a name.")
    def test_create_user_without_name(self):
        self.api_user_auth.create_user_without_name()

    @pytest.mark.order(7)
    @allure.title("T07: Create a new user without a email.")
    def test_create_user_without_email(self):
        self.api_user_auth.create_user_without_email()

    @pytest.mark.order(8)
    @allure.title("T08: Log in with valid email and password.")
    def test_login(self):
        self.api_user_auth.login()

    @pytest.mark.order(9)
    @allure.title("T09: Log in with a valid email that is not registered.")
    def test_login_with_no_registered_email(self):
        self.api_user_auth.login_with_no_registered_email()

    @pytest.mark.order(10)
    @allure.title("T10: Log in with an invalid email.")
    def test_login_with_invalid_email(self):
        self.api_user_auth.login_with_invalid_email()

    @pytest.mark.order(11)
    @allure.title("T11: Log in with an invalid password.")
    def test_login_with_invalid_password(self):
        self.api_user_auth.login_with_invalid_password()

    @pytest.mark.order(12)
    @allure.title("T12: Log in without a password.")
    def test_login_without_password(self):
        self.api_user_auth.login_without_password()

    @pytest.mark.order(13)
    @allure.title("T13: Log out from the account.")
    def test_logout(self):
        user = self.api_user_auth.login()
        self.api_user_auth.logout(Token=user.data.accessToken)

    @pytest.mark.order(14)
    @allure.title("T14: Log out with an invalid token.")
    def test_logout_with_invalid_token(self):
        self.api_user_auth.login()
        self.api_user_auth.logout_with_invalid_token()

    @pytest.mark.order(15)
    @allure.title("T15: Refresh tokens.")
    def test_refresh_tokens(self):
        user = self.api_user_auth.login()
        self.api_user_auth.refresh_tokens(Token=user.data.refreshToken)

    @pytest.mark.order(16)
    @allure.title("T16: Get current user info.")
    def test_get_user_info(self):
        user = self.api_user_auth.create_user()
        self.api_user_auth.get_user_info(Token=user.data.accessToken)

    @pytest.mark.order(17)
    @allure.title("T17: Get current user info with an invalid token.")
    def test_get_user_info_with_invalid_token(self):
        self.api_user_auth.create_user()
        self.api_user_auth.get_user_info_with_invalid_token()

    @pytest.mark.order(18)
    @allure.title("T18: Update user info with valid data.")
    def test_update_user_info(self):
        user = self.api_user_auth.create_user()
        self.api_user_auth.update_user_info(Token=user.data.accessToken)

    @pytest.mark.order(19)
    @allure.title("T19: Update user info with an empty name.")
    def test_update_user_info_with_empty_name(self):
        user = self.api_user_auth.create_user()
        self.api_user_auth.update_user_info_with_empty_name(Token=user.data.accessToken)

    @pytest.mark.order(20)
    @allure.title("T20: Update user info with an invalid email.")
    def test_update_user_info_with_invalid_email(self):
        user = self.api_user_auth.create_user()
        self.api_user_auth.update_user_info_with_invalid_email(Token=user.data.accessToken)

    @pytest.mark.order(21)
    @allure.title("T21: Update user info with an invalid token.")
    def test_update_user_info_with_invalid_token(self):
        self.api_user_auth.create_user()
        self.api_user_auth.update_user_info_with_invalid_token()
