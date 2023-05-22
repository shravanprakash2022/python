

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
value = crypto[4]
print(value)
value = crypto.get(4)
print(value)

crypto[4] = "Cardano"
print(crypto[4])

crypto[6] = "Monero"  
print(crypto[6])
print(crypto)

number = len(crypto)
print(number)

#del crypto[3]
print(crypto)

crypto.pop(3)
print(crypto)
check = 7 not in crypto
print(check)
crypto.clear()
print(crypto)

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
result = crypto.items()
print(result)
result = crypto.keys()
print(result)
result = crypto.values()
print(result)

add = sum(crypto)
print(add)


key = min(crypto)

crypto.popitem()
print(crypto)


