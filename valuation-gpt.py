def calculate_real_exchange_rate(Enominal, Eppp):
    """Calculate the real exchange rate based on the nominal and PPP exchange rates."""
    return Enominal / Eppp

def nominal_rate(Cdomestic, Cforeign=1):
    """Calculate the nominal exchange rate."""
    return Cdomestic / Cforeign

def ppp_rate(Pdomestic, Pforeign):
    """Calculate the PPP exchange rate."""
    return Pdomestic / Pforeign

def currency_valuation(Ereal):
    """Determine the valuation of the currency based on the real exchange rate."""
    percentage = abs(round((Ereal-1)*100))

    if Ereal > 1:
        print("The domestic currency is {}% undervalued relative to the domestic currency.".format(percentage)
    elif Ereal < 1:
        print("The domestic currency is {}% overvalued relative to the domestic currency.".format(percentage))
    else:
        print("The currencies are at parity in terms of purchasing power.")

    if Ereal == 1:
        return "Currency is neither over-valued nor under-valued."
    elif Ereal < 1:
        return "Domestic currency is {}% over-valued in relation to the foreign currency.".format(percentage)
    else:
        return "Domestic currency is {}% under-valued in relation to the foreign currency.".format(percentage)

def main():
    Cdomestic = float(input("Enter the value of the domestic currency relative to the foreign currency: "))
    Pdomestic = float(input("Enter the domestic price of the commodity: "))
    Pforeign = float(input("Enter the foreign price of the same commodity: "))
    
    Enominal = nominal_rate(Cdomestic)
    Eppp = ppp_rate(Pdomestic, Pforeign)
    Ereal = calculate_real_exchange_rate(Enominal, Eppp)
    
    print(currency_valuation(Ereal))

if __name__ == "__main__":
    main()
