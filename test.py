import sys
import unittest

from main import findFileContent, main


class TestTODO(unittest.TestCase):
    def test_using_all_params(self):
        """
        Test with all input params
        python main.py ./ TODO '*.py' 'env'
        """
        folder_path = "./"
        search_string = "TODO"
        pattern = "*.py"
        exclude = "env"

        result = findFileContent(folder_path, search_string, pattern, exclude)
        expected_result = ['./test.py', './main.py', './test_folder/test_file.py', './main_folder/test_file.py']
        self.assertEqual(result, expected_result)

    def test_using_valid_exclude_params(self):
        """
        Test with all input params
        python main.py ./ TODO '*.py' 'test_folder, main_folder'
        """
        folder_path = "./"
        search_string = "TODO"
        pattern = "*.py"
        exclude = "test_folder, main_folder"

        result = findFileContent(folder_path, search_string, pattern, exclude)
        expected_result = ['./test.py', './main.py']
        self.assertEqual(result, expected_result)

    def test_using_one_exclude_params(self):
        """
        Test with all input params
        python main.py ./ TODO '*.py' 'test_folder'
        """
        folder_path = "./"
        search_string = "TODO"
        pattern = "*.py"
        exclude = "test_folder"

        result = findFileContent(folder_path, search_string, pattern, exclude)
        expected_result = ['./test.py', './main.py', './main_folder/test_file.py']
        self.assertEqual(result, expected_result)

    def test_passing_incomplete_params(self):
        """
        Test with imcomplete input params
        Passing only folder_path and search_string
        python main.py ./ TODO
        """
        sys.argv = ["main.py", "./", "TODO"]
        result = main()
        expected_result = ['./test.py', './main.py', './test_folder/test_file.py', './main_folder/test_file.py']
        self.assertListEqual(result, expected_result)

    def test_passing_no_params(self):
        """
        Test with passing no params
        python main.py
        """
        sys.argv = []
        result = main()
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_passing_some_params(self):
        """
        Test passing 3 params
        Passing only folder_path, search_string and pattern
        python main.py ./ TODO *.py
        """
        sys.argv = ["main.py", "./", "TODO", '*.py']
        result = main()
        expected_result = ['./test.py', './main.py', './test_folder/test_file.py', './main_folder/test_file.py']
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()