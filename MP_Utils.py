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

def mpu_err_dlpg(**kwargs):
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