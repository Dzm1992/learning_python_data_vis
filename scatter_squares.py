import matplotlib.pyplot as plt

x_values = list(range(1, 101))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=40)

#Zdefiniowanie tytułu wykresu i etykiet osi.
plt.title("Kwadraty liczb", fontsize=24)
plt.xlabel("Wartość", fontsize=14)
plt.ylabel("Kwadraty wartości", fontsize=14)

#Zdefiniowanie wielkości etykiet.
plt.tick_params(axis='both', which='major', labelsize=14)

#Zdefiniowanie zakresu dla każdej osi.
plt.axis([0, 100, 0, 10000])

plt.show()

