from logging import root
import PyPDF2
import os
import glob

for file in os.walk(os.getcwd()):
    print(file)