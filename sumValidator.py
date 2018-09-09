#!/usr/bin/python

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
    for key in saveOutput:
        getFile = saveOutput.get(key)
        if os.path.isfile(getFile) is False:
            continue

        return_md5 = hashlib.md5(open(getFile, 'rb').read()).hexdigest()
        if return_md5 in saveOutput.keys():
            print "Verified ",getFile
        else:
            print "Not verified ",getFile
	
	
def checkSHA256():
    for key in saveOutput:
        getFile = saveOutput.get(key)
        if os.path.isfile(getFile) is False:
            continue

        return_sha = hashlib.sha256(open(getFile, 'rb').read()).hexdigest()
        if return_sha in saveOutput.keys():
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
saveOutput = {}
searchAsteriscDot = '*.'
searchAsterisc = '*'

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
    getFullPath = os.path.dirname(os.path.realpath(getFileName))
else:
    localFileName = path+"/"+fileName
    files = open(localFileName, "r")
    getFullPath = path + "/"
    getFileName = fileName
    #print "File: ",getFileName," Path: ",getFullPath

for line in files:
    x = line.split()
    fileName = x[0]
    checkSum = x[1]
    saveOutput[fileName] = checkSum


#Remove the *. from the fullpaths

for key, value in saveOutput.items():
    results = value.find(searchAsteriscDot)
    if results != "-1":
        cFileName = re.sub(r'^\*.', getFullPath, value)
        saveOutput[key] = cFileName

    return_asterisc = value.find(searchAsterisc)
    if return_asterisc != "-1":
        cFileName = re.sub(r'\*', getFullPath, value)
        saveOutput[key] = cFileName
		

sumFileName, sumExt = os.path.splitext(getFileName)

if sumExt == "" or sumExt == ".txt":
    searchSum = "sum"
    result = sumFileName.lower().find(searchSum)
    if result == 6:
        findHash = re.sub(r'sum', '', sumFileName.lower())
    elif result == 3:
        findHash = re.sub(r'sums', '', sumFileName.lower())
    else:
        findHash = sumFileName


if sumExt == ".sum":
    findHash = sumFileName

if findHash.lower() == "md5":
    checkMD5()
	
if findHash.lower() == "sha256":
    checkSHA256()

