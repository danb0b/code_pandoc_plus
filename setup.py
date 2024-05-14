# -*- coding: utf-8 -*-
'''
Written by Daniel M. Aukes and CONTRIBUTORS
Email: danaukes<at>asu.edu.
Please see LICENSE for full license.
'''

from setuptools import setup
import sys
import shutil

shutil.rmtree("build", ignore_errors=True)
shutil.rmtree("dist", ignore_errors=True)
shutil.rmtree('pandoc_plus.egg-info', ignore_errors=True)


packages = []
packages.append('pandoc_plus')

package_data = {}
package_data['pandoc_plus'] = []
# package_data['pandoc_plus'].append('support/config.yaml')

setup_kwargs = {}
setup_kwargs['name']='pandoc_plus'
setup_kwargs['version']='0.0.1'
setup_kwargs['classifiers']=['Programming Language :: Python','Programming Language :: Python :: 3']   
setup_kwargs['description']='Pandoc-plus is a collection of tools for making it easier to run pandoc'
setup_kwargs['author']='Dan Aukes'
setup_kwargs['author_email']='danaukes@danaukes.com'
setup_kwargs['url']='https://github.com/danb0b/code_pandoc_plus'
setup_kwargs['license']='MIT'
setup_kwargs['packages']=packages
setup_kwargs['package_dir']={'pandoc_plus' : 'python/pandoc_plus'}
setup_kwargs['package_data'] = package_data
setup_kwargs['install_requires']=[]
setup_kwargs['scripts'] = ['python/pandoc_plus/pandoc-plus','python/pandoc_plus/pandoc-plus.py','python/pandoc_plus/pp-beamer','python/pandoc_plus/pp-beamer.py']
  
setup(**setup_kwargs)
