import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np
from flask import Flask, jsonify, request


def fibLowToHigh(pivotHighPrice, pivotLowPrice):
    # Fibonacci Levels for all low points with max of pivot high points
    f = 0
    level236ListLowToHigh = []
    level382ListLowToHigh = []
    level50ListLowToHigh = []
    level618ListLowToHigh = []
    level786ListLowToHigh = []
    level1272ListLowToHigh = []
    level1618ListLowToHigh = []
    level2ListLowToHigh = []
    level2618ListLowToHigh = []
    level4236ListLowToHigh = []
    level236ListLToH = []
    level382ListLToH = []
    level50ListLToH = []
    level618ListLToH = []
    level786ListLToH = []
    level1272ListLToH = []
    level1618ListLToH = []
    level2ListLToH = []
    level2618ListLToH = []
    level4236ListLToH = []
    retracementLowToHigh = []

    while f < len(pivotLowPrice):
        low_price = pivotLowPrice[f]
        f = f + 1
        high_price = max(pivotHighPrice)

        difference = round(high_price - low_price, 2)
        level0236 = round(high_price - 0.236 * difference, 2)
        level0382 = round(high_price - 0.382 * difference, 2)
        level050 = round(high_price - 0.50 * difference, 2)
        level0618 = round(high_price - 0.618 * difference, 2)
        level0786 = round(high_price - 0.786 * difference, 2)
        level1272 = round(high_price - 1.272 * difference, 2)
        level1618 = round(high_price - 1.618 * difference, 2)
        level2 = round(high_price - 2 * difference, 2)
        level2618 = round(high_price - 2.618 * difference, 2)
        level4236 = round(high_price - 4.236 * difference, 2)

        list236 = [level0236, low_price, high_price]
        level236ListLowToHigh.append(list236)
        level236ListLToH.append(level0236)

        list382 = [level0382, low_price, high_price]
        level382ListLowToHigh.append(list382)
        level382ListLToH.append(level0382)

        list50 = [level050, low_price, high_price]
        level50ListLowToHigh.append(list50)
        level50ListLToH.append(level050)

        list618 = [level0618, low_price, high_price]
        level618ListLowToHigh.append(list618)
        level618ListLToH.append(level0618)

        list786 = [level0786, low_price, high_price]
        level786ListLowToHigh.append(list786)
        level786ListLToH.append(level0786)

        list1272 = [level1272, low_price, high_price]
        level1272ListLowToHigh.append(list1272)
        level1272ListLToH.append(level1272)

        list1618 = [level1618, low_price, high_price]
        level1618ListLowToHigh.append(list1618)
        level1618ListLToH.append(level1618)

        list2 = [level2, low_price, high_price]
        level2ListLowToHigh.append(list2)
        level2ListLToH.append(level2)

        list2618 = [level2618, low_price, high_price]
        level2618ListLowToHigh.append(list2618)
        level2618ListLToH.append(level2618)

        list4236 = [level4236, low_price, high_price]
        level4236ListLowToHigh.append(list4236)
        level4236ListLToH.append(level4236)

        retracementLowToHigh.append(
            {
                'pivotLowPricePoint(1)': low_price,
                'pivotHighPricePoint(0)': high_price,
                '0.236': level0236,
                '0.382': level0382,
                '0.5': level050,
                '0.618': level0618,
                '0.786': level0786,
                '1.272': level1272,
                '1.618': level1618,
                '2.0': level2,
                '2.618': level2618,
                '4.236': level4236
            }
        )
    print("===============================================================")
    print('level236List ' + str(level236ListLowToHigh))
    print('level382List ' + str(level382ListLowToHigh))
    print('level50List ' + str(level50ListLowToHigh))
    print('level618List ' + str(level618ListLowToHigh))
    print('level786List ' + str(level786ListLowToHigh))
    print('level1272List ' + str(level1272ListLowToHigh))
    print('level1618List ' + str(level1618ListLowToHigh))
    print('level2List ' + str(level2ListLowToHigh))
    print('level2618List ' + str(level2618ListLowToHigh))
    print('level4236List ' + str(level4236ListLowToHigh))
    print("===============================================================")
    return retracementLowToHigh