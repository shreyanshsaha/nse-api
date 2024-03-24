from nsepythonserver import *   

def get_stock_info(stock):
  data = nsetools_get_quote(stock)
  data = _retrieve_fields(data)
  return data

def _retrieve_fields(data):
  return {
    'name': data['symbol'],
    'price': data['lastPrice'],
    'open': data['open'],
    'open': data['previousClose'],
    'change': data['change'],
    'percChange': data['pChange']
  }

