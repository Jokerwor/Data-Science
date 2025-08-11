# Module : In which we write classes and methods
# Package: The folder in e=which we write modules
# Program: In which we write the main code
# File: payment_details.py

import os, sys
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__),'....')))

def payment():
    print("Payment Successful!")

payment()
