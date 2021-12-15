# countries and cities

city_dict = {}

fp = open('city.txt','r')

for line in fp:
    city, country = line.strip().split(',')
    if country in city_dict:
        city_dict[country]+= 1
    else:
        city_dict[country] = 1

for country, count in list(city_dict.items()):
    print(country, count)



