import requests
import allure
from utils.helper import Helper
from services.UserAuth.endpoints import Endpoints
from services.UserAuth.payloads import Payloads
from config.headers import Headers
from services.UserAuth.models.user_base_model import UserBaseModel
from services.UserAuth.models.bad_request_model import BadRequestModel
from services.UserAuth.models.user_logout_model import UserLogoutModel
from services.UserAuth.models.tokens_refresh_model import TokensRefreshModel
from services.UserAuth.models.user_info_model import UserInfoModel
from services.UserAuth.models.update_user_model import UpdateUserModel


class UserAuthAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Create a new user.")
    def create_user(self):
        response = requests.post(
            url=self.endpoints.user_registration,
            json=self.payloads.user_registration()
        )
        self.assert_status(response, 201)
        self.attach_response(response.json())
        model = UserBaseModel(**response.json())
        return model

    @allure.step("Create a new user with an invalid email.")
    def create_user_with_invalid_email(self):
        response = requests.post(
            url=self.endpoints.user_registration,
            json=self.payloads.user_registration_with_invalid_email()
        )
        self.assert_status(response, 400)
        self.attach_response(response.json())
        model = BadRequestModel(**response.json())
        return model

    @allure.step("Create a new user with an invalid password.")
    def create_user_with_invalid_password(self):
        response = requests.post(
            url=self.endpoints.user_registration,
            json=self.payloads.user_registration_with_invalid_password()
        )
        self.assert_status(response, 400)
        self.attach_response(response.json())
        model = BadRequestModel(**response.json())
        return model

    @allure.step("Create user with an already existing email.")
    def create_user_with_already_existing_email(self, email):
        response = requests.post(
            url=self.endpoints.user_registration,
            json=self.payloads.user_registration_with_email(email)
        )
        self.assert_status(response, 409)
        self.attach_response(response.json())
        model = BadRequestModel(**response.json())
        return model

    @allure.step("Create a new user without a password.")
    def create_user_without_password(self):
        response = requests.post(
            url=self.endpoints.user_registration,
            json=self.payloads.user_registration_without_password()
        )
        self.assert_status(response, 400)
        self.attach_response(response.json())
        model = BadRequestModel(**response.json())
        return model

    @allure.step("Create a new user without a name.")
    def create_user_without_name(self):
        response = requests.post(
            url=self.endpoints.user_registration,
            json=self.payloads.user_registration_without_name()
        )
        self.assert_status(response, 400)
        self.attach_response(response.json())
        model = BadRequestModel(**response.json())
        return model

    @allure.step("Create a new user without a email.")
    def create_user_without_email(self):
        response = requests.post(
            url=self.endpoints.user_registration,
            json=self.payloads.user_registration_without_email()
        )
        self.assert_status(response, 400)
        self.attach_response(response.json())
        model = BadRequestModel(**response.json())
        return model

    @allure.step("Log in.")
    def login(self):
        response = requests.post(
            url=self.endpoints.user_authentication,
            json=self.payloads.login
        )
        self.assert_status(response, 200)
        self.attach_response(response.json())
        model = UserBaseModel(**response.json())
        return model

    @allure.step("Log in with a valid email that is not registered.")
    def login_with_no_registered_email(self):
        response = requests.post(
            url=self.endpoints.user_authentication,
            json=self.payloads.login_with_no_registered_email()
        )
        self.assert_status(response, 401)
        self.attach_response(response.json())
        model = BadRequestModel(**response.json())
        return model

    @allure.step("Log in with an invalid email.")
    def login_with_invalid_email(self):
        response = requests.post(
            url=self.endpoints.user_authentication,
            json=self.payloads.login_with_invalid_email()
        )
        self.assert_status(response, 409)
        self.attach_response(response.json())
        model = BadRequestModel(**response.json())
        return model

    @allure.step("Log in with an invalid password.")
    def login_with_invalid_password(self):
        response = requests.post(
            url=self.endpoints.user_authentication,
            json=self.payloads.login_with_invalid_password()
        )
        self.assert_status(response, 401)
        self.attach_response(response.json())
        model = BadRequestModel(**response.json())
        return model

    @allure.step("Log in without a password.")
    def login_without_password(self):
        response = requests.post(
            url=self.endpoints.user_authentication,
            json=self.payloads.login_without_password
        )
        self.assert_status(response, 409)
        self.attach_response(response.json())
        model = BadRequestModel(**response.json())
        return model

    @allure.step("Log out from the account.")
    def logout(self, Token):
        response = requests.get(
            url=self.endpoints.logout,
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 200)
        self.attach_response(response.json())
        model = UserLogoutModel(**response.json())
        return model

    @allure.step("Log out with an invalid token.")
    def logout_with_invalid_token(self):
        response = requests.get(
            url=self.endpoints.logout,
            headers=self.headers.invalid_token()
        )
        self.assert_status(response, 401)
        self.attach_response(response.json())
        model = BadRequestModel(**response.json())
        return model

    @allure.step("Refresh tokens.")
    def refresh_tokens(self, Token):
        response = requests.post(
            url=self.endpoints.refresh_tokens,
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 200)
        self.attach_response(response.json())
        model = TokensRefreshModel(**response.json())
        return model

    @allure.step("Get user info.")
    def get_user_info(self, Token):
        response = requests.get(
            url=self.endpoints.get_user_info,
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 200)
        self.attach_response(response.json())
        model = UserInfoModel(**response.json())
        return model

    @allure.step("Get user info with an invalid token.")
    def get_user_info_with_invalid_token(self):
        response = requests.get(
            url=self.endpoints.get_user_info,
            headers=self.headers.invalid_token()
        )
        self.assert_status(response, 401)
        self.attach_response(response.json())
        model = BadRequestModel(**response.json())
        return model

    @allure.step("Update user info.")
    def update_user_info(self, Token):
        response = requests.patch(
            url=self.endpoints.update_user_info,
            json=self.payloads.update_user_info(),
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 200)
        self.attach_response(response.json())
        model = UpdateUserModel(**response.json())
        return model

    @allure.step("Update user info with empty name.")
    def update_user_info_with_empty_name(self, Token):
        response = requests.patch(
            url=self.endpoints.update_user_info,
            json=self.payloads.update_user_info_with_empty_name(),
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 400)
        self.attach_response(response.json())
        model = BadRequestModel(**response.json())
        return model

    @allure.step("Update user info with an invalid email.")
    def update_user_info_with_invalid_email(self, Token):
        response = requests.patch(
            url=self.endpoints.update_user_info,
            json=self.payloads.update_user_info_with_invalid_email(),
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 400)
        self.attach_response(response.json())
        model = BadRequestModel(**response.json())
        return model
    
    @allure.step("Update user info with an invalid token.")
    def update_user_info_with_invalid_token(self):
        response = requests.patch(
            url=self.endpoints.update_user_info,
            json=self.payloads.update_user_info(),
            headers=self.headers.invalid_token()
        )
        self.assert_status(response, 401)
        self.attach_response(response.json())
        model = BadRequestModel(**response.json())
        return model

    