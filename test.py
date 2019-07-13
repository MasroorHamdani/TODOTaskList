import sys
import unittest

from main import findFileContent, main


class TestTODO(unittest.TestCase):
    def test_using_all_params(self):
        """
        Test with correct input
        """
        folder_path = "./"
        search_string = "TODO"
        pattern = "*.py"
        exclude = ['env', '.vccode', '__pycache__']

        result = findFileContent(folder_path, search_string, pattern, exclude)
        expected_result = ['./test.py', './main.py']
        self.assertEqual(result, expected_result)

    def test_passing_incomplete_params(self):
        """
        Test with correct input
        """
        sys.argv = ["main.py", "./", "TODO"]
        result = main()
        expected_result = ['./test.py', './main.py']
        self.assertListEqual(result, expected_result)

    def test_passing_no_params(self):
        """
        Test with correct input
        """
        sys.argv = []
        result = main()
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_passing_some_params(self):
        """
        Test passing 3 params
        python main.py ./ TODO *.py
        """
        sys.argv = ["main.py", "./", "TODO", '*.py']
        result = main()
        expected_result = ['./test.py', './main.py']
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()