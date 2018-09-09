# sumValidator

sumValidator is written in pyton 2.7 and it can run in almost any OS.

This script validate if the file or files you have download are corrupted or not.

It take as argument the sum file (MD5 or SHA256) read the hashes and the files.

Then it create a hash file from the one you have download and compare it with the one from the file.

The sum file and the file you have download must be on the same folder else the script will not be able to validate it.

Usage: sumValidator [-h] [-version] filename

positional arguments:
  filename    Accept md5 or sha256 sum file as parameter

optional arguments:
  -h, --help  show this help message and exit
  -version    show program's version number and exit


Examples:

$ python sumValidator.py ~/Downloads/iso/sha256sum.txt 
Verified  /home/masteryoda/Downloads/iso/linuxmint-19-mate-64bit-v2.iso
