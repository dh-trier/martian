#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Christof Schöch, 2016-2019.

"""
Uses subprocess to call wdiff from the command line. 
You need to have wdiff installed. 
"""


# === Imports ===

import subprocess
from os.path import join
import os
import sys


# === Functions === 

def call_wdiff(sentfile1, sentfile2, wdfile):     
    command = "wdiff --avoid-wraps " + sentfile1 + " " + sentfile2 + " > " + wdfile
    #print(command)
    subprocess.Popen(command, shell=True)
 
    
# === Main === 

def main(file1, file2, wdfile): 
    print("-- Running martians2_wdiff")
    call_wdiff(file1, file2, wdfile)


if __name__ == "__main__":
    main(sentfile1, sentfile2, wdfile)
