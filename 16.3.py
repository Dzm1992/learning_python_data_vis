import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename_dv = 'death_valley_2014.csv'


#Pobranie najwyższych temperatur z pliku.
with open(filename_dv) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	dates_dv, highs_dv, lows_dv = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[0], "%Y-%m-%d")
			high = (row[17])
			highs_dv.append(high)
		except ValueError:
			print(current_date, '- brak danych.')
		else:
			dates_dv.append(current_date)
			low = (row[18])
			lows_dv.append(low)
			
	
#Dane wykresu.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates_dv, highs_dv, c='red', alpha=0.5)
plt.plot(dates_dv, lows_dv, c='blue', alpha=0.5)
plt.fill_between(dates_dv, highs_dv, lows_dv, facecolor='blue', alpha=0.1)


#Formatowanie wykresu.
plt.title("Najwyższa i najniższa prędkość wiatru, \n Death Valley 2014", fontsize=15)
plt.xlabel('a', fontsize=5)
fig.autofmt_xdate()
plt.ylabel("Temperatura (F)", fontsize=1)
plt.tick_params(axis='both', which='major', labelsize=7)

plt.show()
