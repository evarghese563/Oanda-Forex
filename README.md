# Oanda Forex
A python application that uses the OANDA API to take the values from the foreign exhange market and visualize the data.



## This application:
  - Is able to read any Forex Ticker
  - Stores the the last traded price (ltp) for the ticker and store it in a JSON dump file
  - Visualizes the prices for the the selected ticker for any time frame

## Changing Values
  ### Forex Ticker
  query = {\"instruments\": \"ENTER TICKER\"}
  ### Date range
  from_time = time.mktime(pd.to_datetime(\"ENTER FROM DATE\").timetuple())
  
  to_time = time.mktime(pd.to_datetime(\"ENTER TO DATE\").timetuple())

## EUR-USD 1st Quarter Prices (January - March)

![alt text](https://github.com/evarghese563/Oanda-Forex/blob/main/Images/prices.png?raw=true)

This is a chart of all the Opening, Closing, High and Low prices for the ticker EUR-USD in the first quarter of the year.


![alt text](https://github.com/evarghese563/Oanda-Forex/blob/main/Images/Candlestick.png?raw=true)

This is a Candlestick Chart of the 1st Quarter Data of the EUR-USD ticker. This chart was plotted by using the Matplotlib Finance API.

## IMPORTANT NOTE
This code will not run without the OANDA Account ID and the API key that is given to you from OANDA by making an account with them. Due to security reason I have taken out my Account ID and API key but I have marked the locations where the key and Account ID should be placed. An Internet connection is also required to get the values from the OANDA API.
