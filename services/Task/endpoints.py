

HOST = "https://goose-tracker-backend.p.goit.global"


class Endpoints:

    create_task = f"{HOST}/task"

    def get_list_of_task(self, year, month):
        return f"{HOST}/task/by-month?year={year}&month={month}"

    def update_task(self, task_id):
        return f"{HOST}/task/{task_id}"

    def delete_task(self, task_id):
        return f"{HOST}/task/{task_id}"
