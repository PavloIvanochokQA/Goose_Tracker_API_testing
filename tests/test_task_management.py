from config.base_test import BaseTest
import allure
import pytest


@allure.feature("Task Management")
class TestTaskManagement(BaseTest):

    @pytest.mark.order(22)
    @allure.title("T22: Create a task with valid data.")
    def test_create_task(self):
        user = self.api_user_auth.create_user()
        self.api_task.create_task(Token=user.data.accessToken)

    @pytest.mark.order(23)
    @allure.title("T23: Get the list of tasks.")
    def test_get_task_list(self):
        user = self.api_user_auth.login()
        self.api_task.get_task_list(Token=user.data.accessToken, year=2025, month=1)

    @pytest.mark.order(24)
    @allure.title("T24: Create a task with an empty title.")
    def test_create_task_with_empty_title(self):
        user = self.api_user_auth.create_user()
        self.api_task.create_task_with_empty_title(Token=user.data.accessToken)

    @pytest.mark.order(25)
    @allure.title("T25: Create a task with an invalid priority.")
    def test_create_task_with_invalid_priority(self):
        user = self.api_user_auth.create_user()
        self.api_task.create_task_with_invalid_priority(Token=user.data.accessToken)

    @pytest.mark.order(26)
    @allure.title("T26: Create a task with an invalid category.")
    def test_create_task_with_invalid_category(self):
        user = self.api_user_auth.create_user()
        self.api_task.create_task_with_invalid_category(Token=user.data.accessToken)

    @pytest.mark.order(27)
    @allure.title("T27: Create a task without start/end fields.")
    def test_create_task_without_start_end_fields(self):
        user = self.api_user_auth.create_user()
        self.api_task.create_task_without_start_end_fields(Token=user.data.accessToken)

    @pytest.mark.order(28)
    @allure.title("T28: Create a task with an invalid time.")
    def test_create_task_with_invalid_time(self):
        user = self.api_user_auth.create_user()
        self.api_task.create_task_with_invalid_time(Token=user.data.accessToken)

    @pytest.mark.order(29)
    @allure.title("T29: Create a task with an invalid date format.")
    def test_create_task_with_invalid_date_format(self):
        user = self.api_user_auth.create_user()
        self.api_task.create_task_with_invalid_date_format(Token=user.data.accessToken)

    @pytest.mark.order(30)
    @allure.title("T30: Update an existing task with valid data.")
    def test_update_task(self):
        user = self.api_user_auth.create_user()
        task = self.api_task.create_task(Token=user.data.accessToken)
        self.api_task.update_task(Token=user.data.accessToken, task_id=task.id)

    @pytest.mark.order(31)
    @allure.title("T31: Update an existing task with an empty title.")
    def test_update_task_with_empty_title(self):
        user = self.api_user_auth.create_user()
        task = self.api_task.create_task(Token=user.data.accessToken)
        self.api_task.update_task_with_empty_title(Token=user.data.accessToken, task_id=task.id)

    @pytest.mark.order(32)
    @allure.title("T32: Update an existing task with an invalid time.")
    def test_update_task_with_invalid_time(self):
        user = self.api_user_auth.create_user()
        task = self.api_task.create_task(Token=user.data.accessToken)
        self.api_task.update_task_with_invalid_time(Token=user.data.accessToken, task_id=task.id)

    @pytest.mark.order(33)
    @allure.title("T33: Update an existing task with an invalid priority.")
    def test_update_task_with_invalid_priority(self):
        user = self.api_user_auth.create_user()
        task = self.api_task.create_task(Token=user.data.accessToken)
        self.api_task.update_task_with_invalid_priority(Token=user.data.accessToken, task_id=task.id)

    @pytest.mark.order(34)
    @allure.title("T34: Update an existing task with an invalid category.")
    def test_update_task_with_invalid_category(self):
        user = self.api_user_auth.create_user()
        task = self.api_task.create_task(Token=user.data.accessToken)
        self.api_task.update_task_with_invalid_category(Token=user.data.accessToken, task_id=task.id)

    @pytest.mark.order(35)
    @allure.title("T35: Delete one of the existing tasks.")
    def test_delete_task(self):
        user = self.api_user_auth.create_user()
        task = self.api_task.create_task(Token=user.data.accessToken)
        self.api_task.delete_task(Token=user.data.accessToken, task_id=task.id)

    @pytest.mark.order(36)
    @allure.title("T36: Delete a task that has already been deleted.")
    def test_delete_already_deleted_task(self):
        user = self.api_user_auth.create_user()
        task = self.api_task.create_task(Token=user.data.accessToken)
        self.api_task.delete_task(Token=user.data.accessToken, task_id=task.id)
        self.api_task.delete_already_deleted_task(Token=user.data.accessToken, task_id=task.id)

    @pytest.mark.order(37)
    @allure.title("T37: Attempt to delete another user's task.")
    def test_delete_another_user_task(self):
        new_user = self.api_user_auth.create_user()
        task = self.api_task.create_task(Token=new_user.data.accessToken)
        user = self.api_user_auth.login()
        self.api_task.delete_another_user_task(Token=user.data.accessToken, task_id=task.id)

    @pytest.mark.order(38)
    @allure.title("T38: Attempt to update a task that belongs to another user.")
    def test_update_another_user_task(self):
        new_user = self.api_user_auth.create_user()
        task = self.api_task.create_task(Token=new_user.data.accessToken)
        user = self.api_user_auth.login()
        self.api_task.update_another_user_task(Token=user.data.accessToken, task_id=task.id)
