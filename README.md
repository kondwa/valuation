# valuation
A Script for evaluating if a currency is over-valued or under-valued in relation to another.
## Usage
Ensure that you have a Python compiler installed on your computer. In the command prompt(cmd) type 
```python valuation.py```
## Example
1. So a 330ml bottle of Coca-Cola is €4.99 in Switzerland and K500 in Malawi. The current exchange rate is €1 = K1144.35.
```
C:\Code\valuation>python valuation.py
Domestic Currency Value of the Exchange Rate: 1144.35
Foreign Currency Value of the Exchange Rate: 1
Domestic Price of Commodity: 500
Foreign Price of Commodity: 4.99
Evaluation: The Foreign Currency is 1042% overvalued relative to the Domestic Currency.
Interpretation: This indicates a significant deviation from Purchasing Power Parity.
Remedy: The Domestic Currency should be appreciated to bring the Exchange Rate back into equilibrium.
```

2. A Big Mac is ¥20 in China(foreign) and $5.30 in US(domestic). The exchange rate is $1 = ¥6.80.
```C:\Code\valuation>python valuation.py
Domestic Currency Value of the Exchange Rate: 1
Foreign Currency Value of the Exchange Rate: 6.8
Domestic Price of Commodity: 5.30
Foreign Price of Commodity: 20
Evaluation: The Foreign Currency is 45% under-valued relative to the Domestic Currency.
Interpretation: This indicates a significant deviation from Purchasing Power Parity.
Remedy: The Domestic Currency should be depreciated to bring the Exchange Rate back into equilibrium.
```

3. A Big Mac is €4.50 in Germany(foreign) and $5.30 is US(domestic). The exchange rate is €1 = $1.18.
```
C:\Code\valuation>python valuation.py
Domestic Currency Value of the Exchange Rate: 1.18
Foreign Currency Value of the Exchange Rate: 1
Domestic Price of Commodity: 5.30
Foreign Price of Commodity: 4.50
Evaluation: The Foreign Currency is neither under-valued nor over-valued relative to the Domestic Currency.
Interpretation: The Domestic Currency is aligned with its fundamental value as suggested by the Purchasing Power Parity.
```
