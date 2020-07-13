#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:06:40 2019

@author: daukes
"""
import os
import yaml
import sys
import argparse
import subprocess


if __name__=='__main__':
    print(sys.argv)
    parser = argparse.ArgumentParser()
    parser.add_argument('-i',dest='input',default = None)
    parser.add_argument('-o',dest='output_extension',default = None)
    parser.add_argument('-t',dest='template',default = None)

    args = parser.parse_args()
    output_extension = args.output_extension.strip()
    input = args.input.strip()
    template = args.template.strip()

    print('input: ',input,', output extension: ', output_extension,', template: ',template)
    
    input_name,input_extension = input.split('.')
    
    
    if input_extension.lower() == "docx":
        extract_dir = input_name+'_media'
        os.mkdir(extract_dir)
        extractstring = '--extract-media = ./'+extract_dir+' '
    else:
        extractstring = ''

    if output_extension == 'pdf':
        args = ['pandoc',input,'-s','-t','latex+smart','--filter','pandoc-citeproc','--data-dir=/home/danaukes/code_danb0b/code_pandoc_plus/pandoc','--template='+template+'.tex','--pdf-engine=xelatex',extractstring,'--wrap=none','--reference-links','--no-highlight','-o',input_name+'.'+ output_extension]
        s = ' '.join(args)
    elif output_extension == 'docx':
        s='pandoc '+input+' -s --reference-doc=/home/danaukes/code_danb0b/code_pandoc_plus/pandoc/'+template+'.docx -o '+input_name+'.'+output_extension
    elif output_extension == 'tex':
        s='pandoc '+input+' -s -t latex+smart --natbib --data-dir=/home/danaukes/code_danb0b/code_pandoc_plus/pandoc --template='+template+'.tex --pdf-engine=xelatex '+extractstring+'--wrap=none --reference-links  --no-highlight -o '+input_name+'.'+ output_extension
    elif output_extension =='md':
        s='pandoc '+input+' -s --wrap=none --reference-links '+extractstring+' --atx-headers -t markdown-raw_html-bracketed_spans-native_spans-native_divs-fenced_divs -o '+input_name+'.'+ output_extension
    
    print(s)
    subprocess.run(s,shell = True,check = True,stdout=subprocess.PIPE,stderr = subprocess.STDOUT)        

