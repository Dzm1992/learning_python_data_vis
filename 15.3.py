import matplotlib.pyplot as plt

	

from random_walk import RandomWalk
while True:
	#Przygotowanie danych błądzenia losowego i wyświetlenie punktów.
	rw = RandomWalk(50000)
	rw.fill_walk()
	
	
	#Określenie wielkości okna wykresu.
	plt.figure(dpi=128, figsize=(10, 6))
	
	point_numbers = list(range(rw.num_points))
	plt.plot(rw.x_values, rw.y_values, 'c', linewidth=2)
		
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
		


