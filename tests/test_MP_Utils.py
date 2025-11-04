## MP_Utils_Tests program for testing MP_Utils library functions
#
# Copyright (C) 2025, Infor AOGG-UCM

# As MP_Utils uses tkinter dialogs which we assume are already tested we are going to use mock testing
# to replicate the user interactions for unit testing purposes. In this way we can test the behaviour
# of the functions without requiring actual user interaction.
#
# The basis of the process is the function patch from the unittest.mock module which allows us to replace
# parts of our system under test and make assertions about how they have been used.



# Load unittest.mock module function patch
from unittest.mock import patch
# import os module for testing
import os
import pytest 
import sys

# Add the main directory to the sys.`path` to allow imports
# This allows MP_Utils_Test to import MP_Utils from the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import MP_Utils library
import MP_Utils as mpu

class Test_MPUtils_Library:
    """ Unit tests for MP_Utils library functions """

    """ Test mpu_getfile function with no arguments"""
    @patch('tkinter.filedialog.askopenfilename', return_value='C:/user/testfile.txt')
    def test_mpu_uigetfile_no_args(self, mock_askopenfilename):
        """ Test mpu_uigetfile with no arguments """
        # 1. Calls the function
        filename, dirname = mpu.mpu_uigetfile()
        
        # 2.- Verify the results
        assert filename == 'testfile.txt'  # Check file name
        assert dirname == 'C:/user'  # Check directory name
        
        # 3.- Verify that askopenfilename was called with default parameters
        mock_askopenfilename.assert_called_once_with(title="Select a file to open", initialfile="", filetypes=[("All Files", '*.*')], multiple=False)

    """ Test mpu_uigetfile function with just title argument"""
    @patch('tkinter.filedialog.askopenfilename', return_value = 'C:/user/testfile.txt', title = "Open a file for test procesing")
    def text_mpu_uigetfile_title_arg(self, mock_askopenfilename):
        """ Test mpu_uigetfile with title argument """
        # 1. Calls the function
        filename, dirname = mpu.mpu_uigetfile(title="Open a file for test procesing")
        
        # 2.- Verify the results
        assert filename == 'testfile.txt'  # Check file name
        assert dirname == 'C:/user'  # Check directory name
        
        # 3.- Verify that askopenfilename was called with correct parameters
        mock_askopenfilename.assert_called_once_with(title="Open a file for test procesing", initialfile="", filetypes=[("All Files", '*.*')], multiple=False)

    """ Test mpu_uigetfile function with multiple arguments"""
    file_set = ('C:/user/testfile1.txt', 'C:/user/testfile2.txt')
    @patch('tkinter.filedialog.askopenfilename', return_value = file_set)
    def text_mpu_uigetfile_title_arg(self, mock_askopenfilename):
        """ Test mpu_uigetfile with title argument """
        # 1. Calls the function
        filename, dirname = mpu.mpu_uigetfile(multiple = True)
        
        # 2.- Verify the results
        assert filename(0) == 'testfile1.txt' # Check the first file name
        assert filename(1) == 'testfile2.txt'  # Check the second file name
        assert dirname(0) == 'C:/user'  # Check directory name for the first file
        assert dirname(1) == 'C:/user'  # Check directory name for the second file
        
        # 3.- Verify that askopenfilename was called with correct parameters
        mock_askopenfilename.assert_called_once_with(title="Open a file to open", initialfile="", filetypes=[("All Files", '*.*')], multiple=True)