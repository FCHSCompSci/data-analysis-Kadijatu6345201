import csv
from matplotlib import pyplot as plt


filename = 'yearly-mean-sunspot-numbers/sunspotnumber.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    highs = []
    for row in reader:
        high = float(row[1])
        highs.append(high)

    print(highs)

#Get high temps from file
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')

#Format plot
plt.title("Yearly Sunspot Numbers, 1700-2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('years', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()