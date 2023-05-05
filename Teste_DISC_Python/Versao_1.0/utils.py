#################  Arquivo para armazenar imports  #################
import sys
import os.path
# Get the parent directory of the current file
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), './Views/Views_0_Descriptions'))
# Add the parent directory to the sys.path list
sys.path.append(parent_dir)
# Now we can import MyClass from utils.py
from View_Description import Description_Window
