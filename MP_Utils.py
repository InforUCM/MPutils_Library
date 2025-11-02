## MP_Utils Library for an easy migration of MATLAB utility functions to Python
##
## Copyright (C) 2025, Infor AOGG-UCM

from tkinter import filedialog, messagebox
import tkinter as tk
import os

# This code is necessary to avoid the root window appearing and it
# is automatically executed upon importing this module
root = tk.Tk()      # Creates a blank window.
root.withdraw()     # Hides the blank window.

def mpu_err_dlg(**kwargs):
    """
    Displays an error message dialog using tkinter's messagebox.

    Parameters:
    -----------
    **kwargs : dict
        Keyword arguments to be passed to messagebox.showerror.
        Common keys include 'title' and 'message'.

    Example:
    --------
    mpu_err_dlpg(title="Error", message="An unexpected error occurred.")
    """
    messagebox.showerror(**kwargs)

    def mpu_warn_dlg(**kwargs):
        """
        Displays a warning message dialog using tkinter's messagebox.

        Parameters:
        -----------
        **kwargs : dict
            Keyword arguments to be passed to messagebox.showwarning.
            Common keys include 'title' and 'message'.

        Example:
        --------
        mpu_warn_dlg(title="Warning", message="This action is not recommended.")
        """
        messagebox.showwarning(**kwargs)

        def mpu_uigetfile(**kwargs):
            """
            Opens a file dialog to select a file using tkinter's filedialog.

            Parameters:
            -----------
            **kwargs : dict
                Keyword arguments to be passed to filedialog.askopenfilename.
                Common keys include 'initialdir', 'title', and 'filetypes'.

            Returns:
            --------
            str
                The selected file path. Returns an empty string if no file is selected.

            Example:
            --------
            filepath = mpu_uigetfile(title="Select a file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            """
            return filedialog.askopenfilename(**kwargs)
        
        def mpu_uiputfile(**kwargs):
            """
            Opens a file dialog to save a file using tkinter's filedialog.

            Parameters:
            -----------
            **kwargs : dict
                Keyword arguments to be passed to filedialog.asksaveasfilename.
                Common keys include 'initialdir', 'title', and 'defaultextension'.

            Returns:
            --------
            str
                The selected file path for saving. Returns an empty string if no file is selected.

            Example:
            --------
            filepath = mpu_uiputfile(title="Save file as", defaultextension=".txt")
            """
            return filedialog.asksaveasfilename(**kwargs)
        
        def mpu_uigetdir(**kwargs):
            """
            Opens a directory selection dialog using tkinter's filedialog.

            Parameters:
            -----------
            **kwargs : dict
                Keyword arguments to be passed to filedialog.askdirectory.
                Common keys include 'initialdir' and 'title'.

            Returns:
            --------
            str
                The selected directory path. Returns an empty string if no directory is selected.

            Example:
            --------
            dirpath = mpu_uigetdir(title="Select a directory")
            """
            return filedialog.askdirectory(**kwargs)