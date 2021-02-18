import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np
from flask import Flask, jsonify, request

def pivotPoints(candles, listHigh, listlow):
    pivotLowPrice = []
    pivotHighPrice = []
    ###############################################
    ############Calculating Lows##################
    ###############################################
    min_value = min(listlow[0:candles])
    min_value_index = listlow.index(min_value)
    i = min_value_index
    while i < candles:
        if (listlow[i] < min(listlow[i + 1:i + 1 + candles])):
            if (i == 0):
                pivotLowPrice.append(round(listlow[i], 2))
                i = i + 1
            elif (listlow[i] < min(listlow[:i])):
                pivotLowPrice.append(round(listlow[i], 2))
                i = i + 1
            else:
                i = i + 1
        else:
            i = i + 1
    # i = candles
    while i < len(listlow) - candles:
        if (listlow[i] < min(listlow[i + 1:i + 1 + candles]) and listlow[i] < min(listlow[i - candles:i])):
            pivotLowPrice.append(round(listlow[i], 2))
            i = i + 1
        else:
            i = i + 1
    # last block here to calculate end of candles
    if (i == len(listlow) - candles):
        min_value_end = min(listlow[i:])
        min_value_index_end = listlow.index(min_value_end)
        i = min_value_index_end
        if (listlow[i] < min(listlow[i - candles:i])):
            pivotLowPrice.append(round(listlow[i], 2))
    ###############################################
    ############Calculating Highs##################
    ###############################################
    # first block here to calculate beginning of candles
    max_value = max(listHigh[0:candles])
    max_value_index = listHigh.index(max_value)
    h = max_value_index
    while h < candles:
        if (listHigh[h] > max(listHigh[h + 1:i + 1 + candles])):
            if (h == 0):
                pivotHighPrice.append(round(listHigh[h], 2))
                h = h + 1
            elif (listHigh[h] > max(listHigh[:h])):
                pivotHighPrice.append(round(listHigh[h], 2))
                h = h + 1
            else:
                h = h + 1
        else:
            h = h + 1
    # h = candles
    while h < len(listHigh) - candles:
        if (listHigh[h] > max(listHigh[h + 1:h + 1 + candles]) and listHigh[h] > max(listHigh[h - candles:h])):
            pivotHighPrice.append(round(listHigh[h], 2))
            h = h + 1
        else:
            h = h + 1
    # last block here to calculate end of candles
    if (h == len(listHigh) - candles):
        max_value_end = max(listHigh[h:])
        max_value_index_end = listHigh.index(max_value_end)
        h = max_value_index_end
        if (listHigh[h] > max(listHigh[h - candles:h])):
            pivotHighPrice.append(round(listHigh[h], 2))
    print("===============================================================")
    print('pivotLowPrice')
    print(pivotLowPrice)
    print("===============================================================")
    print("===============================================================")
    print('pivotHighPrice')
    print(pivotHighPrice)
    print("===============================================================")
    return pivotHighPrice, pivotLowPrice
