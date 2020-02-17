import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename_dv = 'death_valley_2014.csv'
filename_s = 'sitka_weather_2014.csv'

#Pobranie najwyższych temperatur z pliku.
with open(filename_dv) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	dates_dv, highs_dv, lows_dv = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[0], "%Y-%m-%d")
			high = int(row[1])
			highs_dv.append(high)
		except ValueError:
			print(current_date, '- brak danych.')
		else:
			dates_dv.append(current_date)
			low = int(row[3])
			lows_dv.append(low)
			
with open(filename_s) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	dates_s, highs_s, lows_s = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[0], "%Y-%m-%d")
			high = int(row[1])
			highs_s.append(high)
		except ValueError:
			print(current_date, '- brak danych.')
		else:
			dates_s.append(current_date)
			low = int(row[3])
			lows_s.append(low)
	
#Dane wykresu.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates_dv, highs_dv, c='red', alpha=0.5)
plt.plot(dates_dv, lows_dv, c='blue', alpha=0.5)
plt.fill_between(dates_dv, highs_dv, lows_dv, facecolor='blue', alpha=0.1)

plt.plot(dates_s, highs_s, c='yellow', alpha=0.8)
plt.plot(dates_s, lows_s, c='green', alpha=0.8)
plt.fill_between(dates_s, highs_s, lows_s, facecolor='green', alpha=0.4)



#Formatowanie wykresu.
plt.title("Najwyższa i najniższa temperatura dnia \n Death Valley i Sitka 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatura (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
