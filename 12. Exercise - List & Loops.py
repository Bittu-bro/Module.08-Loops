countries = ['India', 'United States', 'Irak', 'Australia', 'Ireland', 'Sri Lanka', 'Nepal', 'Iceland', 'Cuba', 'Poland', 'Iran']
# count all the countries which are starting with "I"

counter = 0
list = []
for country in countries:
    if country[0] == "I":
        list.append(country) # also  print the all name of the country whose start with "I":
        counter += 1
print(counter)
print(list)