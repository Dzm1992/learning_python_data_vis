from die import Die
import pygal
import matplotlib.pyplot as plt

#Utworzenie kości typu D6.

die_1 = Die() #1
die_2 = Die() #1

#Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
results = []
for roll_num in range(1000): #2
	result = die_1.roll() + die_2.roll()
	results.append(result)

#Analiza wyników.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

#Wizualizacja wyników.
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Wynik rzucania dwiema kości D6."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
	
print(frequencies)


x_values_1 = hist.x_labels
y_values_2 = frequencies 

plt.scatter(x_values_1, frequencies, s=40)
plt.plot(x_values_1, frequencies, linewidth=1)

plt.title("Rozkład rzutu kośćmi")
plt.xlabel("Wyniki")
plt.ylabel("Częstotliwość")
plt.figure(dpi=128, figsize=(10, 6)

plt.show()


from random_walk import RandomWalk
while True:
	#Przygotowanie danych błądzenia losowego i wyświetlenie punktów.
	rw = RandomWalk(50000)
	rw.fill_walk()
	
	
	#Określenie wielkości okna wykresu.
	plt.figure(dpi=128, figsize=(10, 6))
	
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1)
		
	#Podkreślenie pierwsze i ostatniego puntku błądzenia losowego.
	plt.scatter(0, 0, c='green', edgecolor='none', s=100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)
		
	#Ukrycie osi.
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	
	plt.show()
	keep_running = input("Utworzyć kolejne błądzenie losowe? (t/n): ")
	if keep_running == 'n':
		break
		




