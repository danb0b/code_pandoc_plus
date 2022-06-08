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

def process_file(path,output_extension,template,merge):


    output_extension = output_extension.strip()
    input_files = []
    for item in path:
        input_file_exp = item.strip()

        print('input: ',input_file_exp,', output extension: ', output_extension)

        input_files.extend(glob.glob(input_file_exp))
        # for input_file in input_files:

    input_file_string = '"'+'" "'.join(input_files)+'"'
    input_name,input_extension = os.path.splitext(input_files[0])

    template = template.strip()

    print('input: ',input_file_exp,', output extension: ', output_extension,', template: ',template)

    # input_files = glob.glob(input_file_exp)
    
    #print(input_extension,extractstring)
    
    extractstring = ''
    #print(input_extension,extractstring)
    if merge:
        process_internal(input_file_string,input_name,input_extension,output_extension,template)
    else:
        for input_file in input_files:
            input_name,input_extension = os.path.splitext(input_file)
            process_internal(input_file,input_name,input_extension,output_extension,template)

def process_internal(input_file_string,input_name,input_extension,output_extension,template):

    input_extension = input_extension[1:].lower()
    if  input_extension == "docx":
        extract_dir = input_name+'_media'
        os.mkdir(extract_dir)
        extractstring = '--extract-media="./'+extract_dir+'" '
    else:
        extractstring = ''


    if output_extension == 'pdf':
        s='pandoc -s -t latex+smart --citeproc --data-dir='+pandoc_dir+' --template='+template+'.tex --pdf-engine=xelatex '+extractstring+'--wrap=none --reference-links -o "'+input_name+'.'+ output_extension+'" '+input_file_string
    elif output_extension == 'docx':
        s='pandoc -s --reference-doc='+pandoc_dir+'/'+template+'.docx -o "'+input_name+'.'+output_extension+'" '+input_file_string
    elif output_extension == 'odt':
        s='pandoc -s -o "'+input_name+'.'+output_extension+'" '+input_file_string
    elif output_extension == 'tex':
        s='pandoc -s -t latex+smart --natbib --data-dir='+pandoc_dir+' --template='+template+'.tex --pdf-engine=xelatex '+extractstring+'--wrap=none --reference-links -o "'+input_name+'.'+ output_extension+'" '+input_file_string
    elif output_extension =='md':
        s='pandoc -s --wrap=none '+extractstring+' --markdown-headings=atx -t markdown-raw_html-bracketed_spans-native_spans-native_divs+fenced_divs -o "'+input_name+'.'+ output_extension+'" '+input_file_string
        #s='pandoc -s --wrap=none '+extractstring+' --markdown-headings=atx -t markdown-raw_html-bracketed_spans-native_spans-native_divs+fenced_divs-grid_tables-multiline_tables-simple_tables+pipe_tables -o "'+input_name+'.'+ output_extension+'" '+input_file_string
    
    print(s)
    result = subprocess.run(s,shell = True,check = True,capture_output=True)
    return 
        
if __name__=='__main__':
    
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('path',metavar='path',type=str,help='path', default = None,nargs='+')
    parser.add_argument('-o',dest='output_extension',default = None)
    parser.add_argument('-t',dest='template',default = None)
    parser.add_argument('-m','--merge',dest='merge',action='store_true', default = False)
    args = parser.parse_args()
    
    
    path = [os.path.normpath(os.path.expanduser(item)) for item in args.path]

    # import argparse
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-i',dest='input',default = None)
    # parser.add_argument('-o',dest='output_extension',default = None)
    # parser.add_argument('-t',dest='template',default = None)
    # args = parser.parse_args()

    # input_file = sys.argv[1]
    # output_extension = sys.argv[2]
    # template = sys.argv[3]

    result = process_file(path,args.output_extension,args.template,args.merge)

