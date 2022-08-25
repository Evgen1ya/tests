import unittest
from unittest.mock import patch
from main import get_doc_owner_name, add_new_shelf, delete_doc, get_doc_shelf, show_document_info, add_new_doc, documents
from parameterized import parameterized

class TestFunction(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @patch('builtins.input')
    def test_get_doc_owner_name(self, mocked_input):
        mocked_input.return_value = "10006"
        result = get_doc_owner_name()
        self.assertEqual(result, "Аристарх Павлов")

    @patch('builtins.input')
    def test_add_new_shelf_true(self, mocked_input):
        mocked_input.return_value = "4"
        result = add_new_shelf()
        self.assertEqual(result, ("4", True))

    @patch('builtins.input')
    def test_add_new_shelf_false(self, mocked_input):
        mocked_input.return_value = "2"
        result = add_new_shelf()
        self.assertEqual(result, ("2", False))

    @patch('builtins.input')
    def test_delete_doc(self, mocked_input):
        mocked_input.return_value = "10006"
        result = delete_doc()
        self.assertEqual(result, ("10006", True))

    @patch('builtins.input')
    def test_get_doc_shelf(self, mocked_input):
        mocked_input.return_value = "10006"
        result = get_doc_shelf()
        self.assertEqual(result, '2')

    @patch('builtins.input')
    def test_add_new_doc(self, mocked_input):
        mocked_input.return_value = "3"
        result = add_new_doc()
        self.assertEqual(result, '3')

    @parameterized.expand(documents)
    def test_show_document_info(self):
        result = show_document_info(documents)
        self.assertEqual(result, 'passport "2207 876234" "Василий Гупкин"')

    # Не понимаю, что здесь необходимо вввести, если функция не просит никакие данные на вход. Подскажите, как правильно можно это оформить.
