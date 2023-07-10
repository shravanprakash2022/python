auction = {}
def highest_bidder(bid_rec):
   high_bid =0
   for bidder in bid_rec:
      bid_amount = bid_rec[bidder]
      if bid_amount > high_bid:
         high_bid = bid_amount
    print(high_amount)
k = True
while k:
    name = input("name of the bidder")
    price = int(input("what is the bid price"))
    auction[name] = price
    print(auction)
    for i in auction:
    #highest_bidder_price = max(auction[i])
        print(auction)
    #print(highest_bidder_price)
    if price >100:
      k = False
   # else:
      #clear()
    #  pass