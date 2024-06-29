import unittest
from unittest.mock import patch, mock_open, call
import os
import shutil
from move_files import move_specific_files

class TestMoveSpecificFiles(unittest.TestCase):
    @patch('os.listdir')
    @patch('os.path.exists')
    @patch('os.makedirs')
    @patch('shutil.move')
    def test_move_files(self, mock_move, mock_makedirs, mock_exists, mock_listdir):
        '''
        Setup mock return values
        Call the function
        Check the correct files were moved
        '''

        source_directory = '/source'
        target_directory = '/target'
        mock_listdir.return_value = ['file1 2.jpeg', 'file2.txt', 'file3 2.MOV', 'file4 (1).MOV']
        mock_exists.return_value = True
        move_specific_files(source_directory, target_directory)
        expected_calls = [
            call(os.path.join(source_directory, 'file1 2.jpeg'), os.path.join(target_directory, 'file1 2.jpeg')),
            call(os.path.join(source_directory, 'file3 2.MOV'), os.path.join(target_directory, 'file3 2.MOV')),
            call(os.path.join(source_directory, 'file4 (1).MOV'), os.path.join(target_directory, 'file4 (1).MOV'))
        ]
        mock_move.assert_has_calls(expected_calls, any_order=True)

    @patch('os.listdir')
    @patch('os.path.exists')
    def test_no_matching_files(self, mock_exists, mock_listdir):
        '''
        Setup mock return values
        Call the function and capture the output
        '''
        source_directory = '/source'
        target_directory = '/target'
        mock_listdir.return_value = ['file1.txt', 'file2.doc']
        mock_exists.return_value = True
        with patch('builtins.print') as mock_print:
            move_specific_files(source_directory, target_directory)
            mock_print.assert_called_once_with('No match found.')

    @patch('os.listdir')
    @patch('os.path.exists')
    @patch('os.makedirs')
    @patch('shutil.move')
    def test_create_target_directory(self, mock_move, mock_makedirs, mock_exists, mock_listdir):
        '''
        Setup mock return values
        Call the function
        Check the target directory was created
        '''
        source_directory = '/source'
        target_directory = '/target'
        mock_listdir.return_value = ['file1 2.jpeg']
        mock_exists.side_effect = lambda x: x == source_directory

        move_specific_files(source_directory, target_directory)

        mock_makedirs.assert_called_once_with(target_directory)

if __name__ == '__main__':
    unittest.main()
