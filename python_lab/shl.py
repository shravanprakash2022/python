def productsAtNegativeTemp(temperature):
    negative_temp_products = []
    for temp in temperature:
        if temp <= 0:
            negative_temp_products.append(temp)
    return negative_temp_products

def main():
    # Input for temperature
    temperature = []
    temperature_size = int(input("enter numbers : "))
    temperature = list(map(int, input().split()))
    
    result = productsAtNegativeTemp(temperature)
    print(result)

if __name__ == "__main__":
    main()