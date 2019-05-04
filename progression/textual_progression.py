#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: textual_progression.py
# Author: Christof Schöch, 2016-2019.

"""
Script to visualize edits over textual progression.
"""


# === Imports === 

import re
import pandas as pd
import pygal
from pygal import Config
from scipy.signal import savgol_filter as sf

# === Parameters === 

analysisfile = "../analysis/martians_diff-analysis.csv"


# === Functions ===


def read_datafile(analysisfile): 
    with open(analysisfile, "r") as infile:
        data = pd.read_csv(infile, sep="\t", usecols=["itemid", "category", "lev-dist"])
    #print(data.head(10))
    return data


def split_itemid(data):
    split = data["itemid"].str.split("-", n = 1, expand = True) 
    data["line"]= split[0] 
    data["edit"]= split[1] 
    data.drop(columns =["itemid"], inplace = True)     
    #print(data.head(10))
    return data


def separate_categories(data): 
    data = data.groupby(["category", "line"], axis=0).sum()
    other = data.loc["other",:].reset_index().astype(int)
    script = data.loc["script-identifiable",:].reset_index().astype(int)
    #print(script.head(), other.head())
    return other, script


def supply_emptylines(): 
    rows = range(1,11479)
    levs = [0]*11479
    empty = pd.DataFrame(list(zip(rows,levs)), columns=["line", "lev-dist"]).astype(int) 
    #print(empty.head())
    return empty


def merge_frames(withdata, empty): 
    merged = empty.merge(withdata, how="left", on="line").fillna(0)
    merged["lev-dist"] = merged["lev-dist_x"] + merged["lev-dist_y"]
    merged.drop(["lev-dist_x", "lev-dist_y"], axis=1, inplace=True)
    #print(merged.shape)
    #print(merged.head(10))
    return merged    


def merge_again(other, script):
    data = other.merge(script, how="left", on="line")
    data.rename(columns={"lev-dist_x": "other", "lev-dist_y":"script"}, inplace=True)
    return data


def save_data(data, filename):
    with open(filename, "w", encoding="utf8") as outfile: 
        data.to_csv(outfile, sep="\t")


def prepare_data(analysisfile): 
    print("--prepare_data...")
    data = read_datafile(analysisfile)
    data = split_itemid(data)
    other,script = separate_categories(data)
    empty = supply_emptylines()
    other = merge_frames(other, empty)
    script = merge_frames(script, empty)
    data = merge_again(other, script)
    save_data(data, "martian_lev-dists-by-line.csv")
    #print(data.head())
    return data




def using_pygal(data):
    print("--using_pygal...")    
    lines = list(data.loc[: , "line"])
    # Apply some interpolation to the data (smoothing)    
    script = sf(data["script"], 35, 1, mode="nearest")
    other = sf(data["other"], 35, 1, mode="nearest")
    # Graph general configuration
    config = Config()
    config.show_legend = False
    config.human_readable = True
    config.fill = False
    # Line chart
    plot = pygal.StackedLine(config, 
                           height=1000,
                           width = 2000,
                           x_label_rotation=300, 
                           show_legend=True,
                           x_labels_major_every=200,
                           show_minor_x_labels=False,
                           show_dots=False,
                           fill=True,
                           logarithmic=False,
                           range=(0, 60))
    plot.title ="The Martian Modifications (copyedits and substantives)"
    plot.y_title = "Levenshtein distance (smoothed)"
    plot.x_title = "Lines in the novel"
    plot.x_labels = lines
    plot.add("Script-Identifiable Edits", script)
    plot.add("Other Edits", other)
    plot.render_to_file("martian_edits-over-textual-progression.svg")


# === Coordinating function ===

def textual_progression(analysisfile):
    data = prepare_data(analysisfile)
    using_pygal(data)

textual_progression(analysisfile)

