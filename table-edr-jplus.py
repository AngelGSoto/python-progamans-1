'''
Read the table generated by JPLUS ADQL
'''
from __future__ import print_function
import numpy as np
from astropy.io import fits
import os
import glob
import json
import argparse
import matplotlib.pyplot as plt
import pandas as pd
import StringIO
from astropy.table import Table

#create list with the magnitudes
n = 17
magnitude = [[] for _ in range(n)]

parser = argparse.ArgumentParser(
    description="""Write wave and flux of a spectrum""")

parser.add_argument("source", type=str,
                    default="table-6mil-obj-jplus",
                    help="Name of source, taken the prefix ")

parser.add_argument("--debug", action="store_true",
                    help="Print out verbose debugging info about each line in region file")

args = parser.parse_args()
file_ = args.source + ".dat"

f = open(file_, 'r')
header1 = f.readline()
for line in f:
    line = line.strip()
    columns = line.split()
    magnitude[0].append(float(columns[1]))
    magnitude[1].append(float(columns[2]))
    magnitude[2].append(float(columns[3]))
    magnitude[3].append(float(columns[17].split('"')[-1]))
    magnitude[4].append(float(columns[18]))
    magnitude[5].append(float(columns[19]))
    magnitude[6].append(float(columns[20]))
    magnitude[7].append(float(columns[21]))
    magnitude[8].append(float(columns[22]))
    magnitude[9].append(float(columns[23]))
    magnitude[10].append(float(columns[24]))
    magnitude[11].append(float(columns[25]))
    magnitude[12].append(float(columns[26]))
    magnitude[13].append(float(columns[27]))
    magnitude[14].append(float(columns[28].split('"')[0]))
    magnitude[15].append(float(columns[16]))
    magnitude[16].append(float(columns[0]))

#Crearting the table   
table = Table([magnitude[16], magnitude[0], magnitude[1], magnitude[2], magnitude[3], magnitude[4], 
           magnitude[5], magnitude[6], magnitude[7], magnitude[8], magnitude[9], magnitude[10], 
               magnitude[11], magnitude[12], magnitude[13], magnitude[14], magnitude[15]], names=('Tile', 'Number', 'RA', 'Dec', 'rSDSS', 'gSDSS', 'iSDSS', 'zSDSS', 'uJAVA', 'J0378', 'J0395', 'J0410', 'J0430', 'J0515', 'J0660', 'J0861', 'Class star' ), meta={'name': 'first table'})  

#Saving resultated table

asciifile = file_.replace(".dat", ".tab")
table.write(asciifile, format="ascii.tab")


    
