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

# print the top 10 count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
top_ten = sorted(items[:10], key=lambda x: x[1])

# creating separate lists for top_ten
k = [] # for keys
v = [] # for number of tweets

# adding top ten values to these
for i,j in sorted(top_ten, key=lambda x:x[1]):
    k.append(i)
    v.append(j)

print(k)
print(v)

# creating plot
plt.bar(k,
        v,
        color = 'green',
        width = 0.25
        )
plt.ylabel("tweet count")

# if input is reduced.country, set axes accordingly
# else (if input is reduced.lang), change axes
if args.input_path == 'reduced.country':
    plt.title(args.key + " tweets across top 10 countries")
    plt.xlabel("country")
    if args.key == '#coronavirus':
        plt.savefig('plt-1-coronavirus-country.png')
    elif args.key == '#코로나바이러스':
        plt.savefig('plt-2-코로나바이러스-country.png')
else:
    plt.title(args.key + " tweets across top 10 languages")
    plt.xlabel("languages")
    if args.key == '#coronavirus':
        plt.savefig('plt-2-coronavirus-lang.png')
    elif args.key == '#코로나바이러스':
        plt.savefig('plt-3-코로나바이러스-lang.png')


