################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    """ ------------- Updated this function ------------- """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2  # Calculate the average of the buying price and selling price as the price
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    """ ------------- Updated this function ------------- """
    if price_b == 0:
        return 0  # Avoid division by zero
    return price_a / price_b  # Return the ratio of two stock prices


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        """ ----------- Updated to get the ratio --------------- """

        prices = {}  # Dictionary to store prices of stocks

        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price  # Store price using stock symbol as key
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        # Ensure both stocks 'ABC' and 'DEF' are present in the data before calculating ratio
        if 'ABC' in prices and 'DEF' in prices:
            print("Ratio of ABC to DEF is %s" % getRatio(prices['ABC'], prices['DEF']))
        else:
            print("Data for one or both stocks is missing.")
