#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: my_collatex.py
# Author: #cf, 2016.

"""
Script using the python implementation of collatex for text comparison. 
See https://pypi.python.org/pypi/collatex and http://collatex.obdurodon.org/
"""

import collatex as cx
print("collatex version", cx.__version__)
#print(help(cx))

WorkDir = "/media/christof/data/Dropbox/0-Analysen/2016/martians/collatex/"
file1 = WorkDir+"trsp-v1.txt"
file2 = WorkDir+"trsp-v2.txt"
#file1 = WorkDir+"ch1-v1.txt"
#file2 = WorkDir+"ch1-v2.txt"


def perform_collation(file1, file2):
    
    ## Get text from files ##
    with open(file1, "r") as in1:
        version1 = in1.read()
    with open(file2, "r") as in2:
        version2 = in2.read()

    ## Perform basic collation ##
    collation = cx.Collation()
    collation.add_plain_witness("v1", version1)
    collation.add_plain_witness("v2", version2)
    result = cx.collate(collation, 
                        output="table",    # table|json|svg|html|html2
                        layout="vertical", # vertical|horizontal 
                        segmentation=True,
                        detect_transpositions=False)
    print(result)

    ## Create collation graph ## 
    
    mygraph = cx.collate(collation, 
                         output="svg", 
                         segmentation=True,
                         detect_transpositions=False)
    
    


perform_collation(file1, file2)
