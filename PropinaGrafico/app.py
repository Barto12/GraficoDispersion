import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el conjunto de datos 'tips'
tips = sns.load_dataset("tips")

# Crear un gráfico de dispersión con una línea de regresión
sns.lmplot(x="total_bill", y="tip", data=tips)

# Personalizar el gráfico
plt.title("Relación entre la cuenta total y la propina")
plt.xlabel("Cuenta Total ($)")
plt.ylabel("Propina ($)")

# Mostrar el gráfico
plt.show()
