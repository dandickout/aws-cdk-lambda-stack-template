# Description: Conversion factors for various units
Distance = ["kilometers","meters","inches","feet","yards","miles","nautical miles"]
Volume = ["cubic meters","liters","milliliters","UK gallons","US gallons","cubic feet","fluid ounces"]
Energy = ["megawatt hours","kilowatt hours","watt hours","british thermal units","kilojoules","joules"]
EnergyByCV = ["kWh (Gross CV)", "kWh (Net CV)"]
Money = ["USD", "CAD", "EUR", "GBP"]
Mass = ["gigatonnes","megatonnes","tonnes","kilograms","grams","milligrams","US tons","UK tons","pounds","ounces"]


def currency_conversion_factor_from_to(from_currency: str, to_currency: str):
    #taken from 2021 of IRS average yearly foreign exchange rates
    #https://www.irs.gov/individuals/international-taxpayers/yearly-average-currency-exchange-rates
    #X-Axis is years, Y-Axis is currencies as defined above

    conversion_factors = [
        [1.000,	1.254,	0.846,	0.727,],
        [0.798,	1.000,	0.675,	0.580,],
        [0.846, 1.482,	1.000,	0.859,],
        [0.727, 1.725,	1.164,	1.000,]
    ]

    from_cur = Money.index(from_currency)
    #print(year_index)
    to_cur = Money.index(to_currency)
    #print(currency_index)
    return conversion_factors[from_cur][to_cur]

#print(1 * currency_conversion_factor_from_to("USD", "CAD"))

def volume_conversion_factor_from_to(from_volume: str, to_volume: str):
    conversion_factors = [
        [	1.0,	    1000.0,	1000000.0,	219.969,	35.315,	    264.172,	33814.0,],
        [	0.001,	    1.0,	1000.0,	    0.220,	    0.035,	    0.264,	    33.814,	],
        [	0.000001,	0.001,	1.0,	    0.000220,	0.0000353,	0.000264,	0.0338,	],
        [	0.00455,	4.546,	4546.095,	1.0,	    0.161,	    1.201,	    153.722,],
        [	0.0283,	    28.317,	28316.879,	6.229,	    1.0,	    7.481,	    957.507,],
        [	0.00379,	3.785,	3785.416,	0.833,	    0.134,	    1.0,	    128.0,	],
        [	0.0000296,	0.0296,	29.574,	    0.00651,	0.00104,	0.00781,	1.0,	],

    ]

    from_vol = Volume.index(from_volume)
    #print(from_vol)
    to_vol = Volume.index(to_volume)
    #print(to_vol)
    return conversion_factors[from_vol][to_vol]

#print(1 * volume_conversion_factor_from_to("m3", "usgal"))