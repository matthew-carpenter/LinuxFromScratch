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
	resources = (r'ftp://ftp.gnu.org/gnu/bash/bash-3.2.48.tar.gz',
		r'http://ftp.gnu.org/gnu/binutils/binutils-2.17.tar.bz2',
		r'http://ftp.gnu.org/gnu/bison/bison-2.3.tar.gz',
		r'http://www.bzip.org/1.0.6/bzip2-1.0.6.tar.gz',
		r'http://ftp.gnu.org/gnu/coreutils/coreutils-6.9.tar.gz',
		r'http://ftp.gnu.org/gnu/diffutils/diffutils-2.8.1.tar.gz',
		r'http://ftp.gnu.org/gnu/findutils/findutils-4.2.31.tar.gz',
		r'http://ftp.gnu.org/gnu/gawk/gawk-3.1.5.tar.gz',
		r'http://www.netgull.com/gcc/releases/gcc-4.1.2/gcc-4.1.2.tar.gz',
		r'http://ftp.gnu.org/gnu/glibc/glibc-2.5.1.tar.gz',
		r'http://ftp.gnu.org/gnu/grep/grep-2.5.1a.tar.gz',
		r'http://ftp.gnu.org/gnu/gzip/gzip-1.3.12.tar.gz',
		r'https://www.kernel.org/pub/linux/kernel/v2.6/longterm/v2.6.27/linux-2.6.27.58.tar.gz',
		r'http://ftp.gnu.org/gnu/m4/m4-1.4.10.tar.gz',
		r'http://ftp.gnu.org/gnu/make/make-3.81.tar.gz',
		r'http://ftp.gnu.org/gnu/patch/patch-2.5.4.tar.gz',
		r'http://www.cpan.org/src/5.0/perl-5.8.9.tar.gz',
		r'ftp://ftp.gnu.org/gnu/sed/sed-4.1.5.tar.gz',
		r'ftp://ftp.gnu.org/gnu/tar/tar-1.18.tar.gz',
		r'ftp://ftp.gnu.org/gnu/texinfo/texinfo-4.9.tar.gz',
		r'http://tukaani.org/xz/xz-5.0.0.tar.gz')
	
	for required_package in resources:
		get_web_resource(required_package)

if __name__== '__main__':
	main()
