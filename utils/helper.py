import allure
import json
from allure_commons.types import AttachmentType


class Helper:

    def attach_response(self, response):
        response = json.dumps(response, indent=4)
        allure.attach(body=response, name="API Response", attachment_type=AttachmentType.JSON)

    def assert_status(self, response, expected_status):
        assert response.status_code == expected_status, \
            (f"Expected status code {expected_status}, but got {response.status_code}. Response: {response.json()}")
