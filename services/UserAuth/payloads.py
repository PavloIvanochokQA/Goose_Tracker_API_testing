from faker import Faker
from config.data import Data


class Payloads:

    fake = Faker()

    def user_registration(self):
        return {
            "name": self.fake.first_name(),
            "email": self.fake.email(),
            "password": self.fake.password(length=12)
        }
        
    def user_registration_with_invalid_email(self):
        return {
            "name": self.fake.first_name(),
            "email": self.fake.user_name(),
            "password": self.fake.password(length=12)
        }

    def user_registration_with_invalid_password(self):
        return {
            "name": self.fake.first_name(),
            "email": self.fake.email(),
            "password": self.fake.password(length=40)
        }

    def user_registration_with_email(self, email):
        return {
            "name": self.fake.first_name(),
            "email": email,
            "password": self.fake.password(length=12)
        }

    def user_registration_without_password(self):
        return {
            "name": self.fake.first_name(),
            "email": self.fake.email(),
        }

    def user_registration_without_name(self):
        return {
            "email": self.fake.email(),
            "password": self.fake.password(length=12)
        }

    def user_registration_without_email(self):
        return {
            "name": self.fake.first_name(),
            "password": self.fake.password(length=12)
        }

    login = {
        "email": Data.EMAIL,
        "password": Data.PASSWORD
    }

    def login_with_no_registered_email(self):
        return {
            "email": self.fake.email(),
            "password": Data.PASSWORD
        }

    def login_with_invalid_email(self):
        return {
            "email": self.fake.user_name(),
            "password": Data.PASSWORD
        }

    def login_with_invalid_password(self):
        return {
            "email": Data.EMAIL,
            "password": self.fake.password(length=12)
        }

    login_without_password = {
        "email": Data.EMAIL
    }

    def update_user_info(self):
        return {
            "name": self.fake.first_name(),
            "email": self.fake.email(),
            "phone": self.fake.phone_number(),
            "birthday": self.fake.date_of_birth().isoformat(),
            "skype": self.fake.user_name(),
            "userImgUrl": self.fake.image_url()
        }

    def update_user_info_with_empty_name(self):
        return {
            "name": "",
            "email": self.fake.email(),
            "phone": self.fake.phone_number(),
            "birthday": self.fake.date_of_birth().isoformat(),
            "skype": self.fake.user_name(),
            "userImgUrl": self.fake.image_url()
        }

    def update_user_info_with_invalid_email(self):
        return {
            "name": self.fake.first_name(),
            "email": self.fake.user_name(),
            "phone": self.fake.phone_number(),
            "birthday": self.fake.date_of_birth().isoformat(),
            "skype": self.fake.user_name(),
            "userImgUrl": self.fake.image_url()
        }
