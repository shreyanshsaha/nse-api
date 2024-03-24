# in memory cache
from datetime import datetime
import time
from nse_bridge import get_stock_info
import math
import logging

class Cache:
  logger = logging.getLogger(__name__)
  __cachedStock = set({})
  __lastFetchedTime = {}
  __fetchDelayInMinutes = 30*60
  __cache = {}
  # self.__marketStartTime = datetime.date()
  # self.__marketEndTime = datetime.date()

  @classmethod
  def fetch_cached_data(self, stock):
    self.logger.info("Fetcing {} from cache".format(stock))
    if stock not  in self.__cachedStock:
      self.__insert_stock_to_cache(stock)

    curr_time = time.time()
    if self.__lastFetchedTime.get(stock, -math.inf) < curr_time - self.__fetchDelayInMinutes:
      self.__insert_stock_to_cache(stock)
    
    return self.__cache[stock]
  
  @classmethod
  def __insert_stock_to_cache(self, stock):
    self.logger.info("Adding stock {} to cache".format(stock))
    curr_time = time.time()
    data = get_stock_info(stock)
    self.__cachedStock.add(stock)
    self.__lastFetchedTime[stock]=curr_time
    self.__cache[stock] = data

    