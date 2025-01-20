import requests
import allure
from utils.helper import Helper
from services.Task.payloads import Payloads
from services.Task.endpoints import Endpoints
from config.headers import Headers
from services.Task.models.task_model import TaskModel
from services.Task.models.list_item_model import ListItemModel
from services.Task.models.error_model import ErrorModel
from services.Task.models.task_update_model import TaskUpdateModel
from services.Task.models.bad_request_model import BadRequestModel


class TaskAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Create a new task.")
    def create_task(self, Token):
        response = requests.post(
            url=self.endpoints.create_task,
            json=self.payloads.task(),
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 201)
        self.attach_response(response.json())
        model = TaskModel(**response.json())
        return model
    
    @allure.step("Get the list of tasks.")
    def get_task_list(self, Token, year, month):
        response = requests.get(
            url=self.endpoints.get_list_of_task(year, month),
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 200)
        self.attach_response(response.json())
        model = [ListItemModel(**item) for item in response.json()]
        return model
    
    @allure.step("Create a task with an empty title.")
    def create_task_with_empty_title(self, Token):
        response = requests.post(
            url=self.endpoints.create_task,
            json=self.payloads.task_with_empty_title(),
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 400)
        self.attach_response(response.json())
        model = ErrorModel(**response.json())
        return model
    
    @allure.step("Create a task with an invalid priority.")
    def create_task_with_invalid_priority(self, Token):
        response = requests.post(
            url=self.endpoints.create_task,
            json=self.payloads.task_with_invalid_priority(),
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 400)
        self.attach_response(response.json())
        model = ErrorModel(**response.json())
        return model
    
    @allure.step("Create a task with an invalid category.")
    def create_task_with_invalid_category(self, Token):
        response = requests.post(
            url=self.endpoints.create_task,
            json=self.payloads.task_with_invalid_category(),
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 400)
        self.attach_response(response.json())
        model = ErrorModel(**response.json())
        return model
    
    @allure.step("Create a task without start/end fields.")
    def create_task_without_start_end_fields(self, Token):
        response = requests.post(
            url=self.endpoints.create_task,
            json=self.payloads.task_without_start_end_fields(),
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 400)
        self.attach_response(response.json())
        model = ErrorModel(**response.json())
        return model
    
    @allure.step("Create a task with an invalid time.")
    def create_task_with_invalid_time(self, Token):
        response = requests.post(
            url=self.endpoints.create_task,
            json=self.payloads.task_with_invalid_time(),
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 400)
        self.attach_response(response.json())
        model = ErrorModel(**response.json())
        return model
    
    @allure.step("Create a task with an invalid date format.")
    def create_task_with_invalid_date_format(self, Token):
        response = requests.post(
            url=self.endpoints.create_task,
            json=self.payloads.task_with_invalid_date_format(),
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 400)
        self.attach_response(response.json())
        model = ErrorModel(**response.json())
        return model
    
    @allure.step("Update an existing task with valid data.")
    def update_task(self, Token, task_id):
        response = requests.put(
            url=self.endpoints.update_task(task_id),
            json=self.payloads.task(),
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 200)
        self.attach_response(response.json())
        model = TaskUpdateModel(**response.json())
        return model
    
    @allure.step("Update an existing task with an empty title.")
    def update_task_with_empty_title(self, Token, task_id):
        response = requests.put(
            url=self.endpoints.update_task(task_id),
            json=self.payloads.task_with_empty_title(),
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 400)
        self.attach_response(response.json())
        model = ErrorModel(**response.json())
        return model
    
    @allure.step("Update an existing task with an invalid time.")
    def update_task_with_invalid_time(self, Token, task_id):
        response = requests.put(
            url=self.endpoints.update_task(task_id),
            json=self.payloads.task_with_invalid_time(),
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 400)
        self.attach_response(response.json())
        model = ErrorModel(**response.json())
        return model
    
    @allure.step("Update an existing task with an invalid priority.")
    def update_task_with_invalid_priority(self, Token, task_id):
        response = requests.put(
            url=self.endpoints.update_task(task_id),
            json=self.payloads.task_with_invalid_priority(),
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 400)
        self.attach_response(response.json())
        model = ErrorModel(**response.json())
        return model
    
    @allure.step("Update an existing task with an invalid category.")
    def update_task_with_invalid_category(self, Token, task_id):
        response = requests.put(
            url=self.endpoints.update_task(task_id),
            json=self.payloads.task_with_invalid_category(),
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 400)
        self.attach_response(response.json())
        model = ErrorModel(**response.json())
        return model
    
    @allure.step("Delete one of the existing tasks.")
    def delete_task(self, Token, task_id):
        response = requests.delete(
            url=self.endpoints.delete_task(task_id),
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 200)
        self.attach_response(response.json())
        model = TaskModel(**response.json())
        return model
    
    @allure.step("Delete a task that has already been deleted.")
    def delete_already_deleted_task(self, Token, task_id):
        response = requests.delete(
            url=self.endpoints.delete_task(task_id),
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 400)
        self.attach_response(response.json())
        model = BadRequestModel(**response.json())
        return model
    
    @allure.step("Attempt to delete another user's task.")
    def delete_another_user_task(self, Token, task_id):
        response = requests.delete(
            url=self.endpoints.delete_task(task_id),
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 401)
        self.attach_response(response.json())
        model = BadRequestModel(**response.json())
        return model
    
    @allure.step("Attempt to update a task that belongs to another user.")
    def update_another_user_task(self, Token, task_id):
        response = requests.put(
            url=self.endpoints.update_task(task_id),
            json=self.payloads.task(),
            headers=self.headers.basic(Token)
        )
        self.assert_status(response, 401)
        self.attach_response(response.json())
        model = BadRequestModel(**response.json())
        return model