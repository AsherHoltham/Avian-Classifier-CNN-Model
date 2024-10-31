import pandas as pd
import math

import processing as p

# Parse the metadata from CSV and produce a CSV with just the file and label
p.parser("/Users/asheraugustusholtham/Desktop/data/bird_songs_metadata.csv")

df = pd.read_csv('data.csv')

set_len = len(df)
train_len =  math.floor(set_len * .7)
validation_len =  math.floor(set_len * .15)
test_len = set_len - validation_len - train_len

print(train_len)
print(validation_len)
print(test_len)

print(set_len)
