#Currency Formatting US Dollars Using the locale Module

import locale
a=locale.setlocale(locale.LC_ALL, '')
print(a)
#'English_United States.1252'

b=locale.currency(762559748.49)
print(b)
#'$762559748.49'


c=locale.currency(762559748.49, grouping=True) 
print(c)
#'$762,559,748.49'
