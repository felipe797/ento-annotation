#!/usr/bin/python

import os
import csv

def main():
    pathName = os.getcwd()
    directory = '/annotate/row[0]/'

def base(row):
    text = open(strains.csv, "rU")
    reader = csv.DictReader(text, delimiter=',')
    for row in reader:
            return row[0]
    dtype={"row[0]": str}

from os import listdir

def list_files(directory, fa):
    for file in directory:
        if file.endswith(".protein.fa"):
            print(os.path.join("directory", file))
            return file
    
with open(os.path.join("directory", file),'r') as inFile:
    with open("row[0].unspliced.fa","w+") as outFile:
        CopyLines=Falsue
        for line in inFile.readlines():
            if "T1" in line:
                CopyLines=True
            if CopyLines:
                outFile.write(line)
        inFile.close()
        outfile.close()
