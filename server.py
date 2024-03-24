from nsepythonserver import *   
from nse_bridge import *
from flask import Flask, jsonify, request, make_response
from cache import Cache
import random
import requests
import logging

STOCK_SERVER_PORT=7654

app = Flask(__name__)
logger = logging.getLogger(__name__)

logging.basicConfig(
  level=logging.DEBUG,
  handlers=[
      logging.FileHandler("debug.log"),
      logging.StreamHandler()
])

@app.route('/v1/stock/<stock>')
def index(stock):
    try:
      
      api_key = request.args.get("api_key")
      if api_key!='<API_KEY>':
        return "api key is invalid", 401
      
      logger.info("Fetching for: {}".format(stock))
      data = get_stock_info_from_cache(stock)
    except Exception as e:
      logger.error(e)
      return make_response("Server Failure", 500)

    return jsonify(data)

def get_stock_info_from_cache(stock):
     return Cache.fetch_cached_data(stock)
   

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=7654)
