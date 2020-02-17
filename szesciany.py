import matplotlib.pyplot as plt

x_values = list(range(5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Reds, s=40)

#Tytuł wykresu i etykiety osi.
plt.title("Sześciany liczb", fontsize=24)
plt.xlabel("Wartość", fontsize=14)
plt.ylabel("Szesciany wartosci", fontsize=14)

#Zdefiniowanie wielkości etykiet.
plt.tick_params(axis='both', labelsize=14)

#Zakres dla każdej osi.
plt.axis([0, 1100, 0, 1000000000])

plt.show()
	
