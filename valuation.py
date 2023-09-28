def Ereal(Enomial,Eppp):
    return round(Enomial/Eppp,2)

def Enominal(Cdomestic,Cforeign):
    # the published exchange rate: how much of domestic currency for 1 unit of foreign currency
    return Cdomestic/Cforeign

def Eppp(Pdomestic,Pforeign):
    # the ratio of domestic price to foreign price
    return Pdomestic/Pforeign

def valuation():
    domestic_currency = float(input("Domestic Currency Value of the Exchange Rate: "))
    foreign_currency = float(input("Foreign Currency Value of the Exchange Rate: "))
    domestic_price = float(input("Domestic Price of Commodity: "))
    foreign_price = float(input("Foreign Price of Commodity: "))
    nominal = Enominal(domestic_currency,foreign_currency)
    ppp = Eppp(domestic_price,foreign_price)
    real = Ereal(nominal,ppp)
    percentage = abs(round((real-1)*100))
    if(real > 1):
        print("Evaluation: The Foreign Currency is {}% overvalued relative to the Domestic Currency.".format(percentage))
        print("Interpretation: This indicates a significant deviation from purchasing power parity.")
        print("Remedy: The domestic currency should be appreciated to bring the exchange rate back into equilibrium.")
    elif(real < 1):
        print("Evaluation: The Foreign Currency is {}% under-valued relative to the Domestic Currency.".format(percentage))
        print("Interpretation: This indicates a significant deviation from purchasing power parity.")
        print("Remedy: The domestic currency should be depreciated to bring the exchange rate back into equilibrium.")
    else:
        print("Evaluation: The Foreign Currency is neither under-valued nor over-valued relative to the Domestic Currency.")
        print("Interpretation: The currency is aligned with its fundamental value as suggested by the purchasing power parity.")

if __name__ == "__main__":
    valuation()