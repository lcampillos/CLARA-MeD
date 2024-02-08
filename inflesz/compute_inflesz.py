#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Computes Inflesz value and its interpretation of a set of sentences.
# The Inflesz readability scale is computed as the perspicuity (Szigriszt Pazos),
# calculated with the formula explained at: https://legible.es/blog/escala-inflesz/
#
# This code applies to a set of sentences the code prepared by Alejandro Muñoz:
# (https://github.com/alejandromunozes/legibilidad/
#
# The input is a file with sentences, for each element the Inflesz value is computed.
# The average and standard deviation of all Inflesz values are returned.
#
#
# L. Campillos-Llanos, CLARA-MeD project (2023)
#
#####################################################################################

import os
import sys
import legibilidad
import statistics
from statistics import mean,stdev


def inflesz_string(s):

    ''' Returns the Szigriszt Pazos score of an input string '''

    score=legibilidad.szigriszt_pazos(s)

    return score


Scores = []

with open(sys.argv[1], 'r', encoding="utf-8") as f:

    Lines = f.readlines()

    for line in Lines:
        line = line.strip()
        inflesz_score = inflesz_string(line)
        Scores.append(inflesz_score)

# Compute average and standard deviation
avg = float("{0:.2f}".format(mean(Scores)))
sd = float("{0:.2f}".format(stdev(Scores)))

print("Average Inflesz score: %f (%f)" % (avg,sd))

interpret = legibilidad.inflesz(avg)
print(interpret)

basename = os.path.basename(sys.argv[1])
# Print each value to out file (to draw graph)
outFileName = "inflesz_scores_" + basename
with open(outFileName, 'w', encoding="utf-8") as f:
    for s in Scores:
        print(s,file=f)
