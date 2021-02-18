import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np
from flask import Flask, jsonify, request

def fibHighToLow(pivotHighPrice, pivotLowPrice):
    # Fibonacci Levels for all high points with max of pivot low points
    f = 0
    level236ListHighToLow = []
    level382ListHighToLow = []
    level50ListHighToLow = []
    level618ListHighToLow = []
    level786ListHighToLow = []
    level100ListHighToLow = []
    level1272ListHighToLow = []
    level1618ListHighToLow = []
    level2ListHighToLow = []
    level2618ListHighToLow = []
    level4236ListHighToLow = []
    retracementHighToLow = []
    while f < len(pivotHighPrice):
        high_price = pivotHighPrice[f]
        f = f + 1
        low_price = min(pivotLowPrice)

        difference = round(high_price - low_price, 2)
        level0236H2L = round(low_price + 0.236 * difference, 2)
        level0382H2L = round(low_price + 0.382 * difference, 2)
        level050H2L = round(low_price + 0.50 * difference, 2)
        level0618H2L = round(low_price + 0.618 * difference, 2)
        level0786H2L = round(low_price + 0.786 * difference, 2)
        level1272H2L = round(low_price + 1.272 * difference, 2)
        level1618H2L = round(low_price + 1.618 * difference, 2)
        level2H2L = round(low_price + 2 * difference, 2)
        level2618H2L = round(low_price + 2.618 * difference, 2)
        level4236H2L = round(low_price + 4.236 * difference, 2)

        list236H2L = [level0236H2L, low_price, high_price]
        level236ListHighToLow.append(list236H2L)

        list382H2L = [level0382H2L, low_price, high_price]
        level382ListHighToLow.append(list382H2L)

        list50H2L = [level050H2L, low_price, high_price]
        level50ListHighToLow.append(list50H2L)

        list618H2L = [level0618H2L, low_price, high_price]
        level618ListHighToLow.append(list618H2L)

        list786H2L = [level0786H2L, low_price, high_price]
        level786ListHighToLow.append(list786H2L)

        list1272H2L = [level1272H2L, low_price, high_price]
        level1272ListHighToLow.append(list1272H2L)

        list1618H2L = [level1618H2L, low_price, high_price]
        level1618ListHighToLow.append(list1618H2L)

        list2H2L = [level2H2L, low_price, high_price]
        level2ListHighToLow.append(list2H2L)

        list2618H2L = [level2618H2L, low_price, high_price]
        level2618ListHighToLow.append(list2618H2L)

        list4236H2L = [level4236H2L, low_price, high_price]
        level4236ListHighToLow.append(list4236H2L)

        # work in progress for web service
        retracementHighToLow.append(
            {
                'pivotLowPricePoint(0)': low_price,
                'pivotHighPricePoint(1)': high_price,
                '0.236': level0236H2L,
                '0.382': level0382H2L,
                '0.5': level050H2L,
                '0.618': level0618H2L,
                '0.786': level0786H2L,
                '1.272': level1272H2L,
                '1.618': level1618H2L,
                '2.0': level2H2L,
                '2.618': level2618H2L,
                '4.236': level4236H2L
            }
        )
    print("===============================================================")
    print('level236ListHighToLow ' + str(level236ListHighToLow))
    print('level382ListHighToLow ' + str(level382ListHighToLow))
    print('level50ListHighToLow ' + str(level50ListHighToLow))
    print('level618ListHighToLow ' + str(level618ListHighToLow))
    print('level786ListHighToLow ' + str(level786ListHighToLow))
    print('level1272ListHighToLow ' + str(level1272ListHighToLow))
    print('level1618ListHighToLow ' + str(level1618ListHighToLow))
    print('level2ListHighToLow ' + str(level2ListHighToLow))
    print('level2618ListHighToLow ' + str(level2618ListHighToLow))
    print('level4236ListHighToLow ' + str(level4236ListHighToLow))
    print("===============================================================")
    return retracementHighToLow