import matplotlib.pyplot as plt

# Данные для варианта №25
x_vals = [3.50, 3.55, 3.60, 3.65, 3.70, 3.75, 3.80, 3.85, 3.90, 3.95, 4.00, 4.05]
y_vals = [33.1154, 34.8133, 36.5982, 38.4747, 40.4473, 42.5211, 44.7012, 46.9931, 49.4024, 51.9354, 54.5982, 57.3975]

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, 'o-', label='Данные', color='b')

# Оформление графика
plt.title('График зависимости y от x', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True)
plt.legend()
plt.show()