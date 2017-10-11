import matplotlib.pyplot as plt

# Data to plot
labels = 'Win First', 'Win Second', 'Draw'
sizes = [460, 439, 101]
colors = ['gold', 'yellowgreen', 'lightcoral']
explode = (0.01, 0.01, 0.01)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()