# Manipulating Lists

stock_tickers = ["AMZN", "CSCO", "FB", "GOOG", "INTC", "MSFT", "SQ", "TWTR", "WRK"]


# Update the ticker 'WRK' to 'WORK'
stock_tickers[8] = "WORK"

# Alternatively, you can use -1 to select the index of the last item in the list.
# stock_tickers[-1] = 'WORK'

print(stock_tickers)

# Add the ticker 'ZM' to the end of the stock_tickers list
stock_tickers.append("ZM")
print(stock_tickers)

# Add the ticker 'AAPL' to the beginning of the stock_tickers list.
# Add the ticker 'DELL' to it appears between 'CSCO' and 'FB'.
stock_tickers.insert(0, "AAPL")
stock_tickers.insert(3, "DELL")
print(stock_tickers)

# Remove the ticker 'INTC' from the stock_tickers list
stock_tickers.remove("INTC")
print(stock_tickers)

# Remove the ticker 'SQ' from the list using the pop() method
stock_tickers.pop(7)
print(stock_tickers)

# Slice a section of the list that inclues the tickers 'CSCO', 'DELL', 'FB', and 'GOOG'.
# Set this equal to a variable called stock_tickers_slice.
# Print the new variable to confirm your actions.
stock_tickers_slice = stock_tickers[2:6]
print(stock_tickers_slice)
