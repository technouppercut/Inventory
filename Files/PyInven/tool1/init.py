import csv
from itertools import zip_longest

Items = ['a', 'b', 'c', 'd', 'e']

Quantity = ['f', 'g', 'i', 'j']

d = [Items, Quantity]

export_data = zip_longest(*d, fillvalue = '')
with open('fiber.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Items", "Quantity"))
      wr.writerows(export_data)
myfile.close()
