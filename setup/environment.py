#!/bin/python

# Simple script used to get prerequisite system requirements recommended
# by the linux from scratch home page:
# http://www.linuxfromscratch.org/

import subprocess

def get_web_resource(url):
	command = ['wget', url]
	returncode = call_subprocess(command)
	if returncode is not 0:
		raise ValueError('\nGetting the web resource failed with return code ' + returncode)
	
def call_subprocess(command):
	rc = None
	rc = subprocess.call(command)
	return rc
	

def main():
	res = (r'ftp://ftp.gnu.org/gnu/bash/bash-3.2.48.tar.gz',
			r'')
	get_web_resource(res[0])

if __name__== '__main__':
	main()
