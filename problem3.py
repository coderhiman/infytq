#PF-Prac-3 by Himan 
def create_new_dictionary(prices):
    new_dict={}
    for key,val in prices.items():
        if val>200:
            new_dict[key]=val
    return new_dict
    
prices = { 'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
print(create_new_dictionary(prices))
