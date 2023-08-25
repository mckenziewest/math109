# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 10:30:05 2023

@author: WESTMR
"""
import os 
import subprocess


def tex_if_needed(filenames='ready_to_publish.txt',verbose=True):
    with open(filenames) as file:
    	ready_files = file.read().split('\n')
        
    for directory in [rf for rf in ready_files if rf != '']:
        items = os.listdir(directory)
        for filename in items:
            if filename.endswith(".tex"):
                associated_pdf = filename[:-4]+".pdf"
                if associated_pdf not in items:
                    print(f"Currently texing {directory}\\{filename}")
                    x = subprocess.call(f'pdflatex -output-directory {directory} {filename}')
                else: 
                    tex_time = os.path.getmtime(directory + "\\" + filename)
                    pdf_time = os.path.getmtime(directory + "\\" + associated_pdf) 
                    if pdf_time<tex_time:
                        print(f"Currently texing {directory}\\{filename}")
                        x = subprocess.call(f'pdflatex -output-directory {directory} {filename}')
                    else: 
                        x=0
                        if verbose:
                            print(f"Not re-texing {directory}\\{filename}")
                if x != 0:
                    print(f"error compiling {directory}\\{filename}")
                    
if __name__ == "__main__":
    tex_if_needed()