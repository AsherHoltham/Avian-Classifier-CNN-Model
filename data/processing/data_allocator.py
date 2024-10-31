import os
import numpy as np

def allocater(input, file, label, odir):
    new_data = str(label + file) + '.npy'
    np.save(new_data,  input)
    os.path.join(odir, new_data)