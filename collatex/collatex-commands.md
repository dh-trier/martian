collatex-commands
=================

## Basics

Installation path: /home/christof/Programs/collatex/
Call up help: java -jar collatex-tools-1.7.1.jar -h

Example data from "The Martian" (on installation path)
Chapter 1
* ch1-v1.txt
* ch1-v2.txt

Sentence with transposition
* trsp-v1.txt
* trsp-v2.txt


## Usage example (on installation path)

### Default parameters
java -jar collatex-tools-1.7.1.jar ch1-v1.txt ch2-v2.txt
java -jar collatex-tools-1.7.1.jar trsp-v1.txt trsp-v2.txt

java -jar collatex-tools-1.7.1.jar trsp.json


### More useful parameter settings

java -jar collatex-tools-1.7.1.jar --format csv --output coll_dekker.csv trsp-v1.txt trsp-v2.txt

java -jar collatex-tools-1.7.1.jar --format tei --output coll_dekker.xml trsp-v1.txt trsp-v2.txt

java -jar collatex-tools-1.7.1.jar --algorithm medite --format tei --output coll_medite.xml trsp-v1.txt trsp-v2.txt

java -jar collatex-tools-1.7.1.jar --algorithm needleman-wunsch --format tei --output coll_newu.xml trsp-v1.txt trsp-v2.txt

java -jar collatex-tools-1.7.1.jar --format tei --output trsp-output_content-dekker.xml trsp-input_content.json
java -jar collatex-tools-1.7.1.jar --format tei --output trsp-tokens_content-dekker.xml trsp-input_tokens.json

java -jar collatex-tools-1.7.1.jar --algorithm needleman-wunsch --format tei --output trsp-output_content-neewu.xml trsp-input_content.json
java -jar collatex-tools-1.7.1.jar --algorithm needleman-wunsch --format tei --output trsp-tokens_content-neewu.xml trsp-input_tokens.json

java -jar collatex-tools-1.7.1.jar --algorithm medite --format tei --output trsp-output_content-medite.xml trsp-input_content.json
java -jar collatex-tools-1.7.1.jar --algorithm medite --format tei --output trsp-tokens_content-medite.xml trsp-input_tokens.json


java -jar collatex-tools-1.7.1.jar --algorithm dekker --format graphml --output ch1_gml.xml ch1-v1.txt ch1-v2.txt

java -jar collatex-tools-1.7.1.jar --algorithm dekker --format dot --output ch1_dot.gv ch1-v1.txt ch1-v2.txt

java -jar collatex-tools-1.7.1.jar --algorithm dekker --format graphml --output trsp-output_content-dekker_gml.xml trsp-input_content.json

java -jar collatex-tools-1.7.1.jar --algorithm dekker --format graphml --output trsp-short_gml.xml trsp-short-v1.txt trsp-short-v2.txt


### Usage with Martian in JSON, chapter-wise

Input files (each chapter with both versions in JSON format) are in the folder "json" in the collatext directory
Output files (in this case, a dot / graphviz file) go into the folder "out"

java -jar collatex-tools-1.7.1.jar --algorithm dekker --format dot --output out/Martians-ch01.gv json/Martians-ch01.json

At the bottom of the dot-files, the transpositions are listed
Open with Geany and replace the style info with the following for better visibility: [ color = "blue", style = "bold" arrowhead = "normal", arrowtail = "none" ];
Open with Dot-Viewer to see the graph.




## Help

usage: == collatex [<options>] (<json_input> | <witness_1> <witness_2> [[<witness_3>] ...])

-a,--algorithm <arg> == progressive alignment algorithm to use 'dekker' (default), 'medite', 'needleman-wunsch'

-cp,--context-path <arg> == URL base/context path of the service, default: '/' -dot,--dot-path <arg> path to Graphviz 'dot', auto-detected by default

-f,--format <arg> == result/output format: 'json', 'csv', 'dot', 'graphml', 'tei'

-h,--help == print usage instructions

-ie,--input-encoding <arg> charset to use for decoding non-XML witnesse[ color = "blue", style = "bold" arrowhead = "normal", arrowtail = "none" ]; default: UTF-8

-mcs,--max-collation-size <arg> maximum number of characters (counted over all witnesses) to perform collations on, default: unlimited

-mpc,--max-parallel-collations <arg> maximum number of collations to perform in parallel, default: 2

-o,--output <arg> == output fil[ color = "blue", style = "bold" arrowhead = "normal", arrowtail = "none" ]; '-' for standard output (default)

-oe,--output-encoding <arg> charset to use for encoding the outpu[ color = "blue", style = "bold" arrowhead = "normal", arrowtail = "none" ]; default: UTF-8

-p,--port <arg> == HTTP port to bind server to, default: 7369

-s,--script <arg> == ECMA/JavaScript resource with functions to be plugged into the alignment algorithm

-S,--http == start RESTful HTTP server

-t,--tokenized == consecutive matches of tokens will *not* be joined to segments

-xml,--xml-mode == witnesses are treated as XML documents

-xp,--xpath <arg> == XPath 1.0 expression evaluating to tokens of XML witnesse[ color = "blue", style = "bold" arrowhead = "normal", arrowtail = "none" ]; default: '//text()'




