from flask import Flask
from flask import render_template
import os
import json
import datetime
import urllib.request
import io
import time
from flask import request
from flask import make_response
import sys
import logging
import Quandl
import pandas as pd
import pandas.io.data
import matplotlib.pyplot as plt
""" Instantiate a Flask App """

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

""" functions """
def get_stock_data(stockexchange,stockticker,years):
    djia = Quandl.get("YAHOO/INDEX_DJI", trim_start='2004-01-01', trim_end='2011-03-05')
    #print(djia)
    timeshift = datetime.timedelta(days=365*years)
    end = datetime.datetime.now()
    data = pandas.io.data.DataReader(stockticker, "yahoo", end - timeshift, end)
    return(data) 
    

""" Home Page"""
@app.route('/')
def index():

    """ Get the stock exchange and stock ticker from the form"""
    
    stockticker = request.args.get("stockticker")
    stockexchange = request.args.get("stockexchange")
    years = request.args.get("years")
    
    if not stockexchange:
        stockexchange = "NASDAQ"
    if not stockticker:
        stockticker = "AAPL"
    if not years:
        years = 1
    
    data1 = get_stock_data(stockexchange, stockticker, int(years))
    htmldata = data1.to_html()
    response = make_response(render_template("homepage.html", data = htmldata, stockticker=stockticker, years = years))

    #print (aapl)
#x = pd.DataFrame(screener
    #f1 = open('test.txt', 'w+')
    #print (djia, file=f1)
    #sys.stdout.flush()
    return( response)
#x.loc[:,['Adj Close','Close']].plot()
#plt.show()

#aapl.plot(aapl)
    #stockticker = request.args.get("stockticker")
    
    #if not stockexchange:
    #    stockexchange = "SEC"
    #if not stockticker:
    #    stockticker = "AAPL"
    
#    """ If incorrect ticker redirect to invalid html"""
    
    
    
#    """ If correct ticker execute get_stock_data"""
    
    
#    """ return to html the stock data - fundamentals, stock value"""
    
    
    
if __name__ == '__main__':
    
     port = int(os.environ.get('PORT', 5050))
     djia = Quandl.get("YAHOO/INDEX_DJI", trim_start='2004-01-01', trim_end='2011-03-05')
    #print(djia)
     timeshift = datetime.timedelta(days=365*3)
     end = datetime.datetime.now()
     aapl = pandas.io.data.DataReader('MSFT', "yahoo", end - timeshift, end)
    # print (aapl)
     app.run(host='0.0.0.0', port=port, debug=True)
    