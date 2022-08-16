def Ereal(Enomial,Eppp):
    return round(Enomial/Eppp,2)

def Enominal(Cdomestic,Cforeign):
    # the published exchange rate: how much of domestic currency for 1 unit of foreign currency
    return Cdomestic/Cforeign

def Eppp(Pdomestic,Pforeign):
    # the ratio of domestic price to foreign price
    return Pdomestic/Pforeign

def valuation():
    domestic_currency = float(input("Domestic Currency: "))
    foreign_currency = float(input("Foreign Currency: "))
    domestic_price = float(input("Domestic Price: "))
    foreign_price = float(input("Foreign Price: "))
    nominal = Enominal(domestic_currency,foreign_currency)
    ppp = Eppp(domestic_price,foreign_price)
    real = Ereal(nominal,ppp)
    percentage = abs(round((real-1)*100))
    if(real > 1):
        print("The Foreign Currency is {}% overvalued relative to the Domestic Currency.".format(percentage))
    elif(real < 1):
        print("The Foreign Currency is {}% under-valued relative to the Domestic Currency.".format(percentage))
    else:
        print("The Foreign Currency is neither under-valued nor over-valued relative to the Domestic Currency.")

if __name__ == "__main__":
    valuation()