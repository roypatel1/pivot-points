import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np
from flask import Flask, jsonify, request

#function to retrace level H2L
#start and end format Jun-1-2005
def fibRetracementListH2L(stock, startdate, enddate, candles):
    style.use('ggplot')

    startdate = dt.datetime.strptime(startdate, '%b-%d-%Y')
    enddate = dt.datetime.strptime(enddate, '%b-%d-%Y')

    print("stock symbol is = " + stock + " data between start date " + str(startdate) + " - end date " + str(enddate))

    df = web.DataReader(stock, 'yahoo', startdate, enddate)

    print(df.columns)

    listlow = list(round(df.Low, 2))
    listHigh = list(round(df.High,2))
    listClose = list(round(df.Close,2))
    lastClose = listClose[len(listClose)-1]

    pivotHighPrice, pivotLowPrice = pivotPoints(candles, listHigh, listlow)

    retracementHighToLow = fibHighToLow(pivotHighPrice, pivotLowPrice)

    return jsonify({'retracementHighToLow': retracementHighToLow})

#function to retrace level L2H
#start and end format Jun-1-2005
def fibRetracementListL2H(stock, startdate, enddate, candles):
    style.use('ggplot')

    startdate = dt.datetime.strptime(startdate, '%b-%d-%Y')
    enddate = dt.datetime.strptime(enddate, '%b-%d-%Y')

    print("stock symbol is = " + stock + " data between start date " + str(startdate) + " - end date " + str(enddate))

    df = web.DataReader(stock, 'yahoo', startdate, enddate)

    print(df.columns)

    listlow = list(round(df.Low, 2))
    listHigh = list(round(df.High,2))
    listClose = list(round(df.Close,2))
    lastClose = listClose[len(listClose)-1]

    pivotHighPrice, pivotLowPrice = pivotPoints(candles, listHigh, listlow)

    retracementLowToHigh = fibLowToHigh(pivotHighPrice, pivotLowPrice)

    return jsonify({'retracementLowToHigh': retracementLowToHigh})


#function to get pivot points
#start and end format Jun-1-2005
def pivotPointsLowAndHigh(stock, startdate, enddate, candles):
    style.use('ggplot')

    startdate = dt.datetime.strptime(startdate, '%b-%d-%Y')
    enddate = dt.datetime.strptime(enddate, '%b-%d-%Y')

    print("stock symbol is = " + stock + " data between start date " + str(startdate) + " - end date " + str(enddate))

    df = web.DataReader(stock, 'yahoo', startdate, enddate)

    print(df.columns)

    listlow = list(round(df.Low, 2))
    listHigh = list(round(df.High,2))
    listClose = list(round(df.Close,2))
    lastClose = listClose[len(listClose)-1]

    pivotHighPrice, pivotLowPrice = pivotPoints(candles, listHigh, listlow)

    return jsonify({'pivotHighPrice': pivotHighPrice,
                    'pivotLowPrice': pivotLowPrice})


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

        retracementLowToHigh.append([
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
        ])
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
        retracementHighToLow.append([
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
        ])
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


