import matplotlib.pyplot as plt

years = [2000, 2005, 2010, 2015, 2020, 2023]
population = [5, 5.5, 6.5, 8, 10, 11]

plt.figure()

plt.plot(years, population, marker='o')

plt.title("Jordan Population is Rapidly Increasing")
plt.xlabel("Year")
plt.ylabel("Population (Millions)")

plt.savefig('chart.png', dpi=150, bbox_inches='tight')
plt.close()