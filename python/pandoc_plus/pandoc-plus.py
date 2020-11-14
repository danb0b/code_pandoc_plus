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
project_path = initfile.split(os.path.sep)
project_path = os.path.sep.join(project_path[:-3])
pandoc_dir = os.path.join(project_path,'pandoc')

def process_file(input_file_exp,output_extension,template):


    output_extension = output_extension.strip()
    input_file_exp = input_file_exp.strip()
    template = template.strip()

    print('input: ',input_file_exp,', output extension: ', output_extension,', template: ',template)

    input_files = glob.glob(input_file_exp)
    for input_file in input_files:
        
        input_name,input_extension = input_file.split('.')
        
        
        
        if input_extension.lower() == "docx":
            extract_dir = input_name+'_media'
            os.mkdir(extract_dir)
            extractstring = '--extract-media="./'+extract_dir+'" '
        else:
            extractstring = ''
    
        if output_extension == 'pdf':
            args = ['pandoc',input_file,'-s','-t','latex+smart','--citeproc','--data-dir='+pandoc_dir,'--template='+template+'.tex','--pdf-engine=xelatex',extractstring,'--wrap=none','--reference-links','--no-highlight','-o',input_name+'.'+ output_extension]
            s = ' '.join(args)
        elif output_extension == 'docx':
            s='pandoc '+input_file+' -s --reference-doc='+pandoc_dir+'/'+template+'.docx -o '+input_name+'.'+output_extension
        elif output_extension == 'odt':
            s='pandoc '+input_file+' -s -o '+input_name+'.'+output_extension
        elif output_extension == 'tex':
            s='pandoc '+input_file+' -s -t latex+smart --natbib --data-dir='+pandoc_dir+' --template='+template+'.tex --pdf-engine=xelatex '+extractstring+'--wrap=none --reference-links  --no-highlight -o '+input_name+'.'+ output_extension
        elif output_extension =='md':
            s='pandoc '+input_file+' -s --wrap=none --reference-links '+extractstring+' --atx-headers -t markdown-raw_html-bracketed_spans-native_spans-native_divs-fenced_divs -o '+input_name+'.'+ output_extension
            # s='pandoc '+input_file+' -s --wrap=none --reference-links '+extractstring+' --atx-headers -t markdown-raw_html-bracketed_spans-native_spans-native_divs-fenced_divs-grid_tables-multiline_tables-simple_tables+pipe_tables -o '+input_name+'.'+ output_extension
        
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
    template = sys.argv[3]

    process_file(input_file,output_extension,template)

