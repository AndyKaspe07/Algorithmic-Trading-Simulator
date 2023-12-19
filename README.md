# Algorithmic Trading Simulator

## Objectives
1. Download historical market data for a particular set of stocks using libraries such as pandas and numpy.
2. Implement a simple moving average trading strategy
3. Use data visualisation libraries such as seaborn and matplotlib to show trends in the stock price data. 

### Trading Strategy

Through the course of the simulation, 2 moving averages are calculated, MA_30 and MA_50.
I am interested in the times when the 2 MA's overlap. 

Underlying claim is that when the shorter MA (30day in this case) overtakes the longer MA, there is an upward trend. 
Therefore, these are buy signals and on the contrary, when the MA50 overtakes MA30, we consider this a sell signal. 

### Improvements

Next time, I will implement a more sophisticated strategy and backetest it to measure its effectiveness. 