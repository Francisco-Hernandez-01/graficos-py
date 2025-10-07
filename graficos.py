import matplotlib.pyplot as plt

#  Gráfico de líneas: horas dormidas anoche
personas = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10"]
horas_dormidas = [6, 8, 5, 7, 9, 6, 8, 7, 5, 6]

# 2️Gráfico de barras: tazas de café al día
tazas_cafe = [1, 2, 0, 3, 1, 2, 2, 1, 4, 3]


# Gráfico de líneas

plt.figure(figsize=(6, 4))
plt.plot(personas, horas_dormidas, marker='o', color='blue')
plt.title("Horas dormidas anoche (10 personas)")
plt.xlabel("Personas")
plt.ylabel("Horas dormidas")
plt.grid(True)
plt.show()



#  Gráfico de barras

plt.figure(figsize=(6, 4))
plt.bar(personas, tazas_cafe, color='orange')
plt.title("Tazas de café al día (10 personas)")
plt.xlabel("Personas")
plt.ylabel("Tazas de café")
plt.show()




