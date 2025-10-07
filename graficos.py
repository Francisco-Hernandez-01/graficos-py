import matplotlib.pyplot as plt

# ====== Datos (ajusta estos valores) ======
personas = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10"]

# 1) Horas dormidas anoche (líneas)
horas_dormidas = [5, 8, 6, 7, 6, 7, 6, 5, 6, 4]

# 2) Tazas de café al día (barras)
tazas_cafe = [0, 2, 0, 0, 4, 1, 0, 2, 6, 2]

# 3) Red social más usada (pastel)
red_social = ["WhatsApp", "Facebook", "TikTok", "TikTok", "TikTok",
              "TikTok", "TikTok", "Facebook", "Instagram", "TikTok"]

# 4) Minutos hasta la U (histograma)
minutos_uni = [75, 200, 120, 30, 10, 120, 60, 60, 40, 180 ]

# ====== 1) Gráfico de líneas: horas dormidas ======
plt.figure(figsize=(6, 4))
plt.plot(personas, horas_dormidas, marker='o', color='blue')
plt.title("Horas dormidas anoche (10 personas)")
plt.xlabel("Personas")
plt.ylabel("Horas dormidas")
plt.grid(True)
# plt.savefig("lineas_horas_dormidas.png", dpi=150)
plt.show()

# ====== 2) Gráfico de barras: tazas de café ======
plt.figure(figsize=(6, 4))
plt.bar(personas, tazas_cafe, color='orange')
plt.title("Tazas de café al día (10 personas)")
plt.xlabel("Personas")
plt.ylabel("Tazas de café")
# plt.savefig("barras_tazas_cafe.png", dpi=150)
plt.show()

# ====== 3) Gráfico de pastel: red social más usada ======
# Conteo simple sin pandas
conteo = {}
for r in red_social:
    conteo[r] = conteo.get(r, 0) + 1

labels = list(conteo.keys())
sizes  = list(conteo.values())

plt.figure(figsize=(6, 4))
plt.pie(sizes, labels=labels, autopct="%1.0f%%", startangle=90)
plt.title("Red social más usada")
plt.axis('equal')  # pastel circular
# plt.savefig("pastel_red_social.png", dpi=150)
plt.show()

# ====== 4) Histograma: tiempo hasta la universidad ======
plt.figure(figsize=(6, 4))
plt.hist(minutos_uni, bins=5, edgecolor='black', alpha=0.8)
plt.title("Tiempo para llegar a la universidad (min)")
plt.xlabel("Minutos")
plt.ylabel("Frecuencia")
plt.grid(True, axis='y', alpha=0.25, linestyle='--', linewidth=0.8)
plt.tight_layout()
# plt.savefig("histograma_tiempo_uni.png", dpi=150)
plt.show()
