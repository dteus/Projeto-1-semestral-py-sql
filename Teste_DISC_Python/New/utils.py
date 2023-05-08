#################  Arquivo para armazenar imports  #################
import sys
import os.path
# Get the parent directory of the current file
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
# Add the parent directory to the sys.path list
sys.path.append(parent_dir)

# Now we can import MyClass from utils.py
from App.Views import View_Description

from App.Views import View_Login
