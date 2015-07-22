import numpy as np
# Put any initialization logic here.  The context object will be passed to
# the other methods in your algorithm.
def initialize(context):
    
    context.stocks = symbols(
                     
        'SPY'
                           
    ) 

    context.period = 10 # Last x prices
 
  
def handle_data(context, data):
    highHistory = history(context.period,'1d','high') # daily high for each day in period
    lowHistory = history(context.period,'1d','low')  # daily low for each day in period
    for stock in context.stocks:
        highList = highHistory[stock].tolist()
        lowList = lowHistory[stock].tolist()
        
        periodHigh = max(highList)
        periodLow = min(lowList)
