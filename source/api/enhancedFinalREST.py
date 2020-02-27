#!/usr/bin/python
import json
from bson import json_util, ObjectId
import datetime
import urllib
from bottle import Bottle, route, run, request, abort, post, get, response
from pymongo import MongoClient
  
#mongodb connection
client = MongoClient('localhost', 27017)
db = client['market']
collection = db['stocks']

#allowable pymongo commands - for safety - depracated: no need due to static routes
cmds = ['save','find','find_one','remove']

fields = ['Ticker','Profit Margin','Institutional Ownership','EPS growth past 5 years','Total Debt/Equity',
          'Current Ratio','Return on Assets','Sector','P/S','Change from Open','Performance (YTD)',
          'Performance (Week)','Quick Ratio','Insider Transactions','P/B','EPS growth quarter over quarter',
          'Payout Ratio','Performance (Quarter)','Forward P/E','P/E','200-Day Simple Moving Average',
          'Shares Outstanding','Earnings Date','52-Week High','P/Cash','Change','Analyst Recom',
          'Volatility (Week)','Country','Return on Equity','50-Day Low', '_id','50-Day High',
          '20-Day Simple Moving Average','Relative Volume','Dividend Yield','EPS growth next year',
          'Performance (Half Year)','52-Week Low','Insider Ownership','Float Short','Sales growth past 5 years',
          'Market Cap','Shares Float','LT Debt/Equity','PEG','Operating Margin','Price','Performance (Month)',
          'Gap','Volume','Beta','Sales growth quarter over quarter','Performance (Year)','Short Ratio',
          'P/Free Cash Flow','Average Volume','Industry','EPS growth this year','EPS (ttm)',
          '50-Day Simple Moving Average','Average True Range','Institutional Transactions','EPS growth next 5 years',
          'Return on Investment','Volatility (Month)','Gross Margin','Relative Strength Index (14)','Company']


app = Bottle()

#JSON encoder
def mongoJSON(o):
    if isinstance(o, datetime.datetime):
        return o.isoformat()
    elif isinstance(o, ObjectId):
        return str(o)
    else:
        raise TypeError(o)

#supplies HTTP response headers via @headerWrap decorator
def headerWrap(func):
    def wrapper(*args, **kwargs):
        response.headers['Access-Control-Allow-Origin'] = 'http://caramel-comrade.codio.io' # * in case you want to be accessed via any website
        response.content_type = 'application/json'
        return func(*args, **kwargs)

    return wrapper
  
#returns all documents from database collection
@route('/stocks', methods='GET')
@headerWrap
def findAll():
  result = [json.dumps(i,default=mongoJSON) for i in collection.find({},{'_id':1, 'Ticker': 1, 'Company':1}) if i]

  return dict(data=result)

#performs document update - removes document ObjectId to prevent duplication
@route('/update', methods='GET')
@headerWrap
def updateStock():
    doc = request.query
    oid = doc['_id']
    del doc['_id']
    
    #validates document fields - else abort with HTTP.response 400
    for key in doc.keys():
      if not(key in fields):
        response.status = 400
        return (dict(info="ERROR - BAD KEY:" + str(key))) 

    x = collection.update_one({'_id':ObjectId(oid)},{'$set':doc})
    result = x.raw_result
    
    return result
    

#inserts new document - removes document Id to prevent collision - DB handles ID assignments
@route('/create', methods='GET')
@headerWrap
def createStock():
  doc = request.query
  oid = '_id'
  if oid in doc:
    del doc[oid]
    
  #validates document fields - else abort with HTTP.response 400
  for key in doc.keys():
    if not(key in fields):
        response.status = 400
        return (dict(info="ERROR - BAD KEY:" + str(key)))     
      
  x = collection.insert_one(doc)
  result = json.dumps(x.inserted_id,default=mongoJSON)
      
  return result
  
  
#returns the document matching the specified ObjectId 
@route('/find', methods='GET')
@headerWrap
def findStock():
  oid = request.query.id
  result = json.dumps(collection.find_one({'_id':ObjectId(oid)}),default=mongoJSON)
  
  return result

#deletes document matching the specified ObjectId
@route('/delete', methods='GET')
@headerWrap
def deleteStock():
  oid = request.query.id
  x = collection.delete_one({'_id':ObjectId(oid)})
  result = x.raw_result
  
  return result


if __name__ == '__main__':
  app.run(debug=True)
  run(host='0.0.0.0', port=8080)  
    