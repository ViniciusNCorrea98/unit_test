from unittest import TestCase, mock
from app.to_do import nova_task, process_date
from datetime import datetime
class TestNovaTask(TestCase):
    def test_nova_task(self):
        esperado = {
            'id':1,
            'task_name': 'Ligar para o Caio',
            'date': datetime(2023, 5, 23, 0, 0, 0),
            'state': 'To Do'
        }
        result = nova_task('Ligar para o Caio', '23/05/2023')
        self.assertEqual(esperado, result)

    @mock.patch('app.to_do.process_date', return_value=123)
    def test_process_date_check_value(self, mocked):
        result = nova_task('', '24/05/2023')
        mocked.assert_called_with('24/05/2023')

        self.assertEqual(result['date'], 123)

    @mock.patch('app.to_do.insert_task')
    def test_insert_task(self, mocked):
        result = nova_task('Ligar para o Caio', '23/05/2023')

        mocked.assert_called_with(result)

class TestProcessDate(TestCase):
    def test_process_date(self):

        esperado = datetime(2023, 5, 23, 0, 0, 0)
        result = process_date('23/05/2023')

        self.assertEqual(esperado, result)