#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Christof Schöch, 2016-2019.

"""
Splits a plain text file with newlines for paragraph endings 
into a sequence of sentences, one sentence per line. 
This is the first step in the alignement process. 

Place variant texts in a folder (variable: "inputs"). 
"""



# === Imports ===

import nltk
import glob
import os
from os.path import join
import re



# === Functions === 


def read_text(file): 
    """
    Reads the text from a plain text file.
    """
    with open(file, "r") as infile:
        text = infile.read()
        text = re.sub("\n", " ", text)
        text = re.sub("  ", " ", text)
        return text
    

def sentence_splitter(text):
    """
    Splits a text string into individual sentences.
    """
    sents = nltk.sent_tokenize(text)
    sents = "\n".join(sents)
    return sents


def save_sents(sents, outputs, filename):
    """
    Saves the sentences to a file, one sentence per line.
    """ 
    with open(join(outputs, filename + "-sent.txt"), "w") as outfile:
        outfile.write(sents)


# === Main function ===

def main(inputs, outputs):
    print("-- Running martians1_preprocess.py")
    for file in glob.glob(inputs):
        filename = os.path.basename(file).split(".")[0]
        #print(filename)
        text = read_text(file) 
        sents = sentence_splitter(text)
        save_sents(sents, outputs, filename)


if __name__ == "__main__":
    main(inputs, outputs)
