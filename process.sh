#!/usr/bin/env bash
date=$1
pbpaste > $date.txt && ./process.py $date.txt && cat $date.txt.tsv
