import numpy as np
import pandas as pd
import math
import os

import processing as p

# Parse the metadata from CSV and produce a CSV with just the file and label
p.parser("/Users/asheraugustusholtham/Desktop/data/bird_songs_metadata.csv")

df = pd.read_csv('data.csv')

# Define sizes of each dataset for training the model
set_len = len(df)
train_len =  math.floor(set_len * .7)
validation_len =  math.floor(set_len * .15)
test_len = set_len - validation_len - train_len

df.set_index(df.columns[1], inplace=True)
for f in df.index:
    filename = str(f)
    filename = filename[:-4]
    l = int(df.loc[f])
    l = str(l)

    file = l + filename + '.npy'
    np.save(file,  p.converter('/Users/asheraugustusholtham/Desktop/data/wavfiles/' + f))

    if(df.loc(f) < train_len): os.path.join('train', file)
    elif(df.loc(f) < train_len + validation_len): os.path.join('validation', file)
    else: os.path.join('test', file)
    