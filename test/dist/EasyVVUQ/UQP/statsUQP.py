import os, sys
import numpy as np
import csv

def statsUQP(reader=None):
    if reader == None:
        sys.exit("A reader (e.g. csvReader) must be specified for the appropriate file type")

    def statsUQP_specific(dirname):
        l = reader(dirname)
        mean = np.mean(l)
        std = np.std(l)
        print("Mean = " + str(mean) + " std = " + str(std))

    return statsUQP_specific