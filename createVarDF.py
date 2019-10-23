#!/usr/bin/env python
# coding: utf-8
import pandas as pd
from tqdm import tqdm
from hscUtils import hcvsearch
from astropy.io import ascii

allVariables = []
variablesPath = '/media/SSD0/mauro/BCV/astro/dwldVariables/hubbleCatalogue/hlsp_hcv_hst_wfpc2-acs-wfc3_all_multi_v1_var-cat.dat'

with open(variablesPath) as infile:
    for line in infile:
        allVariables.append(line.split()[2])

alreadyDownloaded = pd.read_csv('./detailedVars.csv')
downloadedIds = set(alreadyDownloaded['MatchID'])


missingIds = set(allVariables)-downloadedIds

for matchid in tqdm(missingIds):
    dat = hcvsearch(table='detailed',MatchID=matchid)
    dat = ascii.read(dat)
    dat = dat.to_pandas()
    with open('detailedVars.csv', 'a') as f:
        dat.to_csv(f, header=False)
