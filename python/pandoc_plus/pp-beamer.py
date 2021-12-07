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
project_path = '/'.join(os.path.normpath(initfile).split(os.path.sep)[:-3])
module_path = '/'.join(os.path.normpath(initfile).split(os.path.sep)[:-1])
support_path = '/'.join([project_path,'support'])
slidy_path = 'file:///' + '/'.join([support_path,'slidy2'])
slideous_path = 'file:///' + '/'.join([support_path,'slideous'])
s5_path = 'file:///' + '/'.join([support_path,'s5-11','ui','default'])
revealjs_path = 'file:///' + '/'.join([support_path,'reveal.js'])

def process_file(path,output_extension):


    output_extension = output_extension.strip()
    input_files = []
    for item in path:
        input_file_exp = item.strip()

        print('input: ',input_file_exp,', output extension: ', output_extension)

        input_files.extend(glob.glob(input_file_exp))
        # for input_file in input_files:
        
    input_file_string = '"'+'" "'.join(input_files)+'"'
    input_name,dummy = os.path.splitext(input_files[0])
    
    if output_extension in ['pdf','tex']:
        s='pandoc '+project_path+'/bat/beamer_default.yaml -V titlegraphic="'+support_path+'/fulton.png'+'" -s -t beamer --pdf-engine=xelatex --slide-level=2 -o "'+input_name+'.'+output_extension+'" '+input_file_string 
        
    elif output_extension in ['slidy','slideous','s5','dzslides','revealjs']:
        s='pandoc -s -t '+output_extension+' --slide-level=2 -V slidy-url="'+slidy_path+'" -V slideous-url="'+slideous_path+'" -V s5-url="'+s5_path+'" -V revealjs-url="'+revealjs_path+'" -o "'+input_name+'.html" '+input_file_string 

    elif output_extension =='pptx':
        s='pandoc -s --slide-level=2 -o "'+input_name+'.'+ output_extension+'" '+input_file_string 
    
    print(s)
    subprocess.run(s,shell = True,check = True,stdout=subprocess.PIPE,stderr = subprocess.STDOUT)        
    
if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('path',metavar='path',type=str,help='path', default = None,nargs='+')

    # parser.add_argument('-i',dest='input',default = None)
    parser.add_argument('-o',dest='output_extension',default = None)
    parser.add_argument('-d','--debug',dest='debug',action='store_true', default = False)
    # parser.add_argument('-t',dest='template',default = None)
    args = parser.parse_args()

    # input_file = sys.argv[1]
    # output_extension = sys.argv[2]
    
    path = [os.path.normpath(os.path.expanduser(item)) for item in args.path]
    
    if args.debug:
        print('path: ',path)
        print('output_extension: ',args.output_extension)

    process_file(path,args.output_extension)

