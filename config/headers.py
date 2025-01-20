from faker import Faker


class Headers:

    fake = Faker()

    def basic(self, Token):
        return {
            "Authorization": f"Bearer {Token}",
        }

    def invalid_token(self):
        return {
            "Authorization": f"Bearer {self.fake.md5()}",
        }
