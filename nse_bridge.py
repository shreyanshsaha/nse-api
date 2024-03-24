from nsepythonserver import *   

def get_stock_info(stock):
  
  if stock in nse_get_index_list():
    data = nse_get_index_quote(stock)
  else:
    data = nsetools_get_quote(stock)

  if data is None:
    raise Exception("Stock does not exist")
  
  if stock in nse_get_index_list():
    data = _retrieve_index_fields(data)
  else:
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

def _retrieve_index_fields(data):
  return {
    'name': data['indexName'],
    'price': data['last'],
    'open': data['open'],
    'close': data['previousClose'],
    'change': 0,
    'percChange': data['percChange']
  }

if __name__ == "__main__":
  print(get_stock_info("NIFTY 50"))
