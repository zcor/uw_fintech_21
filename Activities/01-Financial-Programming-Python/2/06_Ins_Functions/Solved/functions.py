# Define a hello function and a main function that accepts a string argument
def hello():
    print("Hi! This is the hello function.")


def main(stock_ticker):
    print(stock_ticker + " is booming right now!")


# Call the hello and main functions
hello()
main('AAPL')

# Define a calculate_market_cap function that returns and integer, and then call it


def calculate_market_cap(market_price, number_of_shares):
    cap = market_price * number_of_shares

    return cap


stock_ticker = "SBUX"
market_price = 76.06
number_of_shares = 1243600000

market_cap = calculate_market_cap(market_price, number_of_shares)
print(f"{stock_ticker} Market Capitalization: {market_cap}")
print(f"Data type of market_cap variable is: {type(market_cap)}")


# Capture function output and print output value and data type
def calculate_market_cap(market_price, number_of_shares):
    cap = market_price * number_of_shares

    return cap


market_price = 76.06
number_of_shares = 1243600000

market_cap = calculate_market_cap(market_price, number_of_shares)
print(f"Market Capitalization: {market_cap}")
print(f"Data type of market_cap variable is: {type(market_cap)}")
