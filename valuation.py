def Ereal(Enomial,Eppp):
    return round(Enomial/Eppp,2)

def Enominal(Cdomestic,Cforeign):
    # the published exchange rate: how much of domestic currency for 1 unit of foreign currency
    return round(Cdomestic/Cforeign,2)

def Eppp(Pdomestic,Pforeign):
    # the ratio of domestic price to foreign price
    return round(Pdomestic/Pforeign,2)

def valuation():
    domestic_currency = float(input("Domestic Currency: "))
    foreign_currency = float(input("Foreign Currency: "))
    domestic_price = float(input("Domestic Price: "))
    foreign_price = float(input("Foreign Price: "))
    nominal = Enominal(domestic_currency,foreign_currency)
    ppp = Eppp(domestic_price,foreign_price)
    real = Ereal(nominal,ppp)
    percentage = round((real-1)*100,2)
    if(real > 1):
        print("Domestic Currency is under-valued. The Foreign Currency is {:.2f}% overvalued relative to the Domestic Currency.".format(percentage))
    elif(real < 1):
        print("Domestic Currency is over-valued. The Foreign Currency is {:.2f}% under-valued relative to the Domestic Currency.".format(percentage))
    else:
        print("Domestic Currency is correctly valued.")

if __name__ == "__main__":
    valuation()