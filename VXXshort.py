import pandas as pd

def initialize(context):
    #global variables here
    context.security = symbol('VXX')

# Will be called on every trade event for the securities you specify. 
def handle_data(context, data):

    exchange_time = pd.Timestamp(get_datetime()).tz_convert('US/Eastern') 
    #current_price = data[context.security].price
    #stopLoss = data[context.security].open_price*(1.02)
    
    if exchange_time.hour == 9 and exchange_time.minute == 31:
        number_of_shares = 10000
        #entryPrice = data[context.security].price
        order(context.security, number_of_shares) 
        #buyTime = data[context.security].datetime
        log.info("Shorting  %s" % (context.security.symbol))
        #log.info("entered at %s" % (exchange_time))
        #print buyTime
 
    elif exchange_time.hour == 15 and exchange_time.minute == 14:
        order_target(context.security, 0)
        log.info("Covering %s" % (context.security.symbol))
        #log.info("covered at %s" % (exchange_time))
       
    else:
        return
        
        
   #if current_price > 1.01*data[context.security]
    #print data
    #for stock in data:
     #   print stock.symbol
