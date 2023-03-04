#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()
import matplotlib # setting up plt import
matplotlib.use('Agg')

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt # importing plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# remove all items with 'country_code'
counts[args.key] = {k:v for k,v in counts[args.key].items() if 'country_code' not in k}

# saving the top  10 count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
top_ten = sorted(sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)[:10], key=lambda x: x[1])
print("top = ", top_ten)


# creating separate lists for top_ten
x = [] # for keys
y = [] # for number of tweets

# adding top ten values to these
for k,v in top_ten:
    x.append(k)
    y.append(v)

# printing
print(x)
print(y)

# creating plot
plt.bar(x,
        y,
        color = 'green',
        width = 0.25
        )
plt.ylabel("tweet count")

# if input is reduced.country, set axes accordingly
# else (if input is reduced.lang), change axes
if args.input_path == 'reduced.country':
    plt.xlabel("country")
    plt.title(args.key + " tweets across top 10 countries")
    if args.key == '#coronavirus':
        plt.savefig('plt-1-coronavirus-country.png')
    elif args.key == '#코로나바이러스':
        plt.savefig('plt-2-코로나바이러스-country.png')
else:
    plt.xlabel("languages")
    plt.title(args.key + " tweets across top 10 languages")
    if args.key == '#coronavirus':
        plt.savefig('plt-2-coronavirus-lang.png')
    elif args.key == '#코로나바이러스':
        plt.savefig('plt-3-코로나바이러스-lang.png')
