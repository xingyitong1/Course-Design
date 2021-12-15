# countries and capitals

capital_dict = {}

country,capital = input("Enter a country and a capital comma separated (Q,Q to quit): ").split(',')

while (country,capital) != ('Q','Q'):
    capital_dict[country]=capital
    country,capital = input("Enter a country and a capital comma separated (Q,Q to quit): ").split(',')

print(sorted([capital for capital in list(capital_dict.values())]))
 
