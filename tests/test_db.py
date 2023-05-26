from unittest import TestCase, mock
from app.database import select_tasks

tasks = [
        {'id':1, 'task_name': 'Dormir', 'date': '??', 'state': 'To Do'},
        {'id': 2, 'task_name': 'Acordar', 'date': '??', 'state': 'Doing'},
        {'id': 3, 'task_name': 'Comer', 'date': '??', 'state': 'Doing'},
        {'id': 4, 'task_name': 'Jantar', 'date': '??', 'state': 'To Do'},
        {'id': 5, 'task_name': 'Dormir de novo', 'date': '??', 'state': 'To Do'}
    ]
class TestSelectTasks(TestCase):

    @mock.patch('app.database.db', new=tasks)
    def test_select_tasks_acordar(self):
        results = select_tasks('Acordar', '')

        for result in results:
            with self.subTest(f'Acordar in {result}'):
                self.assertEqual('Acordar', result['task_name'])

    @mock.patch('app.database.db', new=tasks)
    def test_select_tasks_Doing(self):
        results = select_tasks('', 'Doing')

        for result in results:
            with self.subTest(f'Acordar in {result}'):
                self.assertEqual('Doing', result['state'])


