import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np
from flask import Flask, jsonify, request
from fibHighToLow import fibHighToLow
from fibLowToHigh import fibLowToHigh
from pivotPoints import pivotPoints
import yfinance as yf
import json


# function to retrace level H2L
# start and end format Jun-1-2005
def fibRetracementListH2L(stock, startdate, enddate, candles):
    style.use('ggplot')

    startdate = dt.datetime.strptime(startdate, '%b-%d-%Y')
    enddate = dt.datetime.strptime(enddate, '%b-%d-%Y')

    print("stock symbol is = " + stock + " data between start date " + str(startdate) + " - end date " + str(enddate))

    df = web.DataReader(stock, 'yahoo', startdate, enddate)

    print(df.columns)

    listDate = list(df.index)
    listlow = list(round(df.Low, 2))
    listHigh = list(round(df.High, 2))
    listClose = list(round(df.Close, 2))
    lastClose = listClose[len(listClose) - 1]

    pivotHighPrice, pivotLowPrice = pivotPoints(candles, listHigh, listlow)

    retracementHighToLow = fibHighToLow(pivotHighPrice, pivotLowPrice)

    return jsonify({'retracementHighToLow': retracementHighToLow})


# function to retrace level L2H
# start and end format Jun-1-2005
def fibRetracementListL2H(stock, startdate, enddate, candles):
    style.use('ggplot')

    startdate = dt.datetime.strptime(startdate, '%b-%d-%Y')
    enddate = dt.datetime.strptime(enddate, '%b-%d-%Y')

    print("stock symbol is = " + stock + " data between start date " + str(startdate) + " - end date " + str(enddate))

    df = web.DataReader(stock, 'yahoo', startdate, enddate)

    print(df.columns)

    listDate = list(df.index)
    listlow = list(round(df.Low, 2))
    listHigh = list(round(df.High, 2))
    listClose = list(round(df.Close, 2))
    lastClose = listClose[len(listClose) - 1]

    pivotHighPrice, pivotLowPrice = pivotPoints(candles, listHigh, listlow)

    retracementLowToHigh = fibLowToHigh(pivotHighPrice, pivotLowPrice)

    return jsonify({'retracementLowToHigh': retracementLowToHigh})


# function to retrace level L2H
# start and end format Jun-1-2005
def cluster1L2H(stock, startdate, enddate, candles):
    style.use('ggplot')

    startdate = dt.datetime.strptime(startdate, '%b-%d-%Y')
    enddate = dt.datetime.strptime(enddate, '%b-%d-%Y')

    print("stock symbol is = " + stock + " data between start date " + str(startdate) + " - end date " + str(enddate))

    df = web.DataReader(stock, 'yahoo', startdate, enddate)

    listDate = list(df.index)
    listlow = list(round(df.Low, 2))
    listHigh = list(round(df.High, 2))
    listClose = list(round(df.Close, 2))
    lastClose = listClose[len(listClose) - 1]

    pivotHighPrice, pivotLowPrice = pivotPoints(candles, listHigh, listlow)

    retracementLowToHigh = fibLowToHigh(pivotHighPrice, pivotLowPrice)

    cluster1 = []
    pricebetween = lastClose - (lastClose * .01 / 100)
    pricebetween2 = lastClose - (lastClose * 3.5 / 100)

    cluster2 = []
    pricebetweenCluster2 = lastClose - (lastClose * 3.5 / 100)
    pricebetweenCluster2Max = lastClose - (lastClose * 6.0 / 100)

    for entry in retracementLowToHigh:
        if entry['0.236'] > pricebetween2 and entry['0.236'] < pricebetween:
            cluster1.append(str(entry['0.236']) + ' : 0.236')
        if entry['0.382'] > pricebetween2 and entry['0.382'] < pricebetween:
            cluster1.append(str(entry['0.382']) + ' : 0.382')
        if entry['0.5'] > pricebetween2 and entry['0.5'] < pricebetween:
            cluster1.append(str(entry['0.5']) + ' : 0.5')
        if entry['0.618'] > pricebetween2 and entry['0.618'] < pricebetween:
            cluster1.append(str(entry['0.618']) + ' : 0.618')
        if entry['0.786'] > pricebetween2 and entry['0.786'] < pricebetween:
            cluster1.append(str(entry['0.786']) + ' : 0.786')
        if entry['1.272'] > pricebetween2 and entry['1.272'] < pricebetween:
            cluster1.append(str(entry['1.272']) + ' : 1.272')
        if pricebetween2 < entry['1.618'] < pricebetween:
            cluster1.append(str(entry['1.618']) + ' : 1.618')
        if pricebetween2 < entry['2.0'] < pricebetween:
            cluster1.append(str(entry['2.0']) + ' : 2.0')
        if pricebetween2 < entry['2.618'] < pricebetween:
            cluster1.append(str(entry['2.618']) + ' : 2.618')
        if entry['0.236'] > pricebetweenCluster2Max and entry['0.236'] < pricebetweenCluster2:
            cluster2.append(str(entry['0.236']) + ' : 0.236')
        if entry['0.382'] > pricebetweenCluster2Max and entry['0.382'] < pricebetweenCluster2:
            cluster2.append(str(entry['0.382']) + ' : 0.382')
        if entry['0.5'] > pricebetweenCluster2Max and entry['0.5'] < pricebetweenCluster2:
            cluster2.append(str(entry['0.5']) + ' : 0.5')
        if entry['0.618'] > pricebetweenCluster2Max and entry['0.618'] < pricebetweenCluster2:
            cluster2.append(str(entry['0.618']) + ' : 0.618')
        if entry['0.786'] > pricebetweenCluster2Max and entry['0.786'] < pricebetweenCluster2:
            cluster2.append(str(entry['0.786']) + ' : 0.786')
        if entry['1.272'] > pricebetweenCluster2Max and entry['1.272'] < pricebetweenCluster2:
            cluster2.append(str(entry['1.272']) + ' : 1.272')
        if pricebetweenCluster2Max < entry['1.618'] < pricebetweenCluster2:
            cluster2.append(str(entry['1.618']) + ' : 1.618')
        if pricebetweenCluster2Max < entry['2.0'] < pricebetweenCluster2:
            cluster2.append(str(entry['2.0']) + ' : 2.0')
        if pricebetweenCluster2Max < entry['2.618'] < pricebetweenCluster2:
            cluster2.append(str(entry['2.618']) + ' : 2.618')

    return jsonify({'cluster1': cluster1},
                   {'cluster2': cluster2},
                   {'retracementLowToHigh': retracementLowToHigh})


# function to get pivot points
# start and end format Jun-1-2005
def pivotPointsLowAndHigh(stock, startdate, enddate, candles):
    style.use('ggplot')

    startdate = dt.datetime.strptime(startdate, '%b-%d-%Y')
    enddate = dt.datetime.strptime(enddate, '%b-%d-%Y')

    print("stock symbol is = " + stock + " data between start date " + str(startdate) + " - end date " + str(enddate))

    df = web.DataReader(stock, 'yahoo', startdate, enddate)

    print(df.columns)

    listDate = list(df.index)
    listlow = list(round(df.Low, 2))
    listHigh = list(round(df.High, 2))
    listClose = list(round(df.Close, 2))
    lastClose = listClose[len(listClose) - 1]

    pivotHighPrice, pivotLowPrice = pivotPoints(candles, listHigh, listlow)

    return jsonify({'pivotHighPrice': pivotHighPrice,
                    'pivotLowPrice': pivotLowPrice})
