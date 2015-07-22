import numpy as np
# Put any initialization logic here.  The context object will be passed to
# the other methods in your algorithm.
def initialize(context):
    context.stocks = symbols(
                           # 'XLY',  # XLY Consumer Discrectionary SPDR Fund   
                           # 'XLF',  # XLF Financial SPDR Fund  
                           # 'XLK',  # XLK Technology SPDR Fund  
                           # 'XLE',  # XLE Energy SPDR Fund  
                           # 'XLV',  # XLV Health Care SPRD Fund  
                           # 'XLI',  # XLI Industrial SPDR Fund  
                           # 'XLP',  # XLP Consumer Staples SPDR Fund   
                           # 'XLB',  # XLB Materials SPDR Fund  
                           # 'XLU',  # XLU Utilities SPRD Fund
        'SPY'
                           
    ) 

    context.historical_bars = 100
    context.feature_window = 10 # Last x prices
 
    

def handle_data(context, data):
    prices = history(bar_count = context.historical_bars, frequency='1d', field='price')
    #cash = context.portfolio.cash
    for stock in context.stocks:
        t = context.feature_window
        price_list = prices[stock].tolist()
        while t < len(price_list)-1:   
            
            price_list = prices[stock].tolist()

            X = []
            y = []
    
            
            bar_t = price_list[t]
            bar_tplus1 = price_list[t+1]
            pricing_list = []
            xx = 0
            t += 1                 
    record('t',t)
