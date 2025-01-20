from faker import Faker
from utils.enums import Priority, Category


class Payloads:

    fake = Faker()

    def task(self):
        return {
            "title": self.fake.sentence(nb_words=3),
            "start": self.fake.time(),
            "end": self.fake.time(),
            "priority": self.fake.random_element(elements=[priority.value for priority in Priority]),
            "category": self.fake.random_element(elements=[category.value for category in Category]),
            "date": self.fake.date_this_year().strftime('%Y-%m-%d')
        }

    def task_with_empty_title(self):
        return {
            "title": "",
            "start": self.fake.time(),
            "end": self.fake.time(),
            "priority": self.fake.random_element(elements=[priority.value for priority in Priority]),
            "category": self.fake.random_element(elements=[category.value for category in Category]),
            "date": self.fake.date_this_year().strftime('%Y-%m-%d')
        }

    def task_with_invalid_priority(self):
        return {
            "title": self.fake.sentence(nb_words=3),
            "start": self.fake.time(),
            "end": self.fake.time(),
            "priority": self.fake.word(),
            "category": self.fake.random_element(elements=[category.value for category in Category]),
            "date": self.fake.date_this_year().strftime('%Y-%m-%d')
        }

    def task_with_invalid_category(self):
        return {
            "title": self.fake.sentence(nb_words=3),
            "start": self.fake.time(),
            "end": self.fake.time(),
            "priority": self.fake.random_element(elements=[priority.value for priority in Priority]),
            "category": self.fake.word(),
            "date": self.fake.date_this_year().strftime('%Y-%m-%d')
        }

    def task_without_start_end_fields(self):
        return {
            "title": self.fake.sentence(nb_words=3),
            "priority": self.fake.random_element(elements=[priority.value for priority in Priority]),
            "category": self.fake.random_element(elements=[category.value for category in Category]),
            "date": self.fake.date_this_year().strftime('%Y-%m-%d')
        }

    def task_with_invalid_time(self):
        return {
            "title": self.fake.sentence(nb_words=3),
            "start": self.fake.word(),
            "end": self.fake.word(),
            "priority": self.fake.random_element(elements=[priority.value for priority in Priority]),
            "category": self.fake.random_element(elements=[category.value for category in Category]),
            "date": self.fake.date_this_year().strftime('%Y-%m-%d')
        }

    def task_with_invalid_date_format(self):
        return {
            "title": self.fake.sentence(nb_words=3),
            "start": self.fake.time(),
            "end": self.fake.time(),
            "priority": self.fake.random_element(elements=[priority.value for priority in Priority]),
            "category": self.fake.random_element(elements=[category.value for category in Category]),
            "date": self.fake.date_this_year().strftime('%m-%Y')
        }
