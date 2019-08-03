#!/usr/bin/python2.7

import sys
import argparse
import hashlib
import os
import re


def usage():
    print """usage: sumValidator.py [-h] [-version] filename

			positional arguments:
				filename    Accept md5 or sha256 sum file as parameter

			optional arguments:
				-h, --help  show this help message and exit
				-version    show program's version number and exit"""
    sys.exit()


def checkMD5():
    for key in res:
        getFile = res.get(key)
        if os.path.isfile(getFile) is False:
            continue

        return_md5 = hashlib.md5(open(getFile, 'rb').read()).hexdigest()
        if return_md5 in res.keys():
            print "Verified ",getFile
        else:
            print "Not verified ",getFile


def checkSingle(singleFile, ext):
    extens = ext
    getFileName = singleFile
    verified = ""
    return_sha = hashlib.sha256(open(getFileName, 'rb').read()).hexdigest()
    fullFileName = getFileName + extens
    with open(fullFileName) as f:
        for line in f:
            if return_sha in line:
                verified = True
                break
            else:
                verified = False

    if verified is True:
        print "Verified ", singleFile
    else:
        print "Not verified ", singleFile


getFileName = ""
res = {}
searchAsteriscDot = '*.'
searchDot = '.'

parser = argparse.ArgumentParser(prog='sumValidator')
parser.add_argument("file", metavar='filename', help="Accept md5 or sha256 sum file as parameter")
parser.add_argument("-version", action='version', version='%(prog)s 0.1')
args = parser.parse_args()


if args.file:
    getFileName = args.file
if getFileName == "":
    usage()


FileName, Ext = os.path.splitext(getFileName)

if Ext == ".sha256":
    checkSingle(FileName, Ext)
    sys.exit()


path, fileName = os.path.split(getFileName)

if path == "":
    files = open(os.path.realpath(getFileName), "r")
    getFullPath = os.path.dirname(os.path.realpath(getFileName)) + "/"
    print "File: ",getFileName," Path Empty: ",getFullPath
else:
    localFileName = path+"/"+fileName
    files = open(localFileName, "r")
    getFullPath = path + "/"
    getFileName = fileName
    print "File: ",getFileName," Path NE: ",getFullPath


for line in files:
    key, value = line.split()
    res[key] = value

    results = value.find(searchAsteriscDot)
    resultsDot = value.find(searchDot)

    if results != -1 or resultsDot != -1:
        cFileName = re.sub(r'^\*./|^\./', getFullPath, value)
        res[key] = cFileName
    else:
        cFileName = getFullPath+ "/" +value
        res[key] = cFileName


sumFileName, sumExt = os.path.splitext(getFileName)

if sumExt == "" or sumExt == ".txt":
    searchSum = "sum"
    result = sumFileName.lower().find(searchSum)

    if result == 6 or result == 3:
        findHash = re.sub(r'sum|[s]', '', sumFileName.lower())
    else:
        findHash = sumFileName

if sumExt == ".sum":
    findHash = sumFileName
if findHash.lower() == "md5":
    checkMD5()
if findHash.lower() == "sha256":
    checkSHA256()
