#!/home/danaukes/anaconda3/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:06:40 2019

@author: daukes
"""
import os
import yaml
import sys
import subprocess
import glob
import sys
import pandoc_plus

module = sys.modules['pandoc_plus']
initfile = module.__file__
project_path = os.path.sep.join(os.path.normpath(initfile).split(os.path.sep)[:-3])
module_path = os.path.sep.join(os.path.normpath(initfile).split(os.path.sep)[:-1])
support_path = os.path.join(project_path,'support')
slideous_path = os.path.join(support_path,'slideous')
s5_path = os.path.join(support_path,'s5')
revealjs_path = os.path.join(support_path,'reveal.js')

def process_file(input_file_exp,output_extension):


    output_extension = output_extension.strip()
    input_file_exp = input_file_exp.strip()

    print('input: ',input_file_exp,', output extension: ', output_extension)

    input_files = glob.glob(input_file_exp)
    for input_file in input_files:
        
        input_name,input_extension = os.path.splitext(input_file)
        
        if output_extension == 'pdf':
            s='pandoc '+project_path+'/bat/beamer_default.yaml -s -t beamer --pdf-engine=xelatex --slide-level=2 "'+input_file+'" -o "'+input_name+'.'+output_extension+'"'
            
        elif output_extension == 'tex':
            s='pandoc '+project_path+'/bat/beamer_default.yaml -s -t beamer --pdf-engine=xelatex --slide-level=2 "'+input_file+'" -o "'+input_name+'.'+output_extension+'"'

        elif output_extension in ['slidy','slideous','s5','dzslides','revealjs']:
            s='pandoc -s -t '+output_extension+' --slide-level=2 -V slideous-url="'+slideous_path+'" -V s5-url="'+s5_path+'" -V revealjs-url="'+revealjs_path+'" "'+input_file+'" -o "'+input_name+'.html"'

        elif output_extension =='pptx':
            s='pandoc -s --slide-level=2 "'+input_file+'" -o "'+input_name+'.'+ output_extension+'"'
        
        print(s)
        subprocess.run(s,shell = True,check = True,stdout=subprocess.PIPE,stderr = subprocess.STDOUT)        
    
if __name__=='__main__':
    # import argparse
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-i',dest='input',default = None)
    # parser.add_argument('-o',dest='output_extension',default = None)
    # parser.add_argument('-t',dest='template',default = None)
    # args = parser.parse_args()

    input_file = sys.argv[1]
    output_extension = sys.argv[2]
    
    process_file(input_file,output_extension)

