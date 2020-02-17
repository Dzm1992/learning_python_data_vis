from die import Die
import pygal

#Utworzenie kości typu D6.

die_1 = Die() #1
die_2 = Die() #1

#Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
results = []
for roll_num in range(1000000): #2
	result = die_1.roll() * die_2.roll()
	results.append(result)

#Analiza wyników.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

#Wizualizacja wyników.
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Wynik mnożenia 2 kości D6."
hist.x_labels = []
for number in range(1,max_result+1):
	hist.x_labels.append(number)
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"

hist.add('D6 * D6', frequencies)
hist.render_to_file('die_visual.svg')
	
print(frequencies)
