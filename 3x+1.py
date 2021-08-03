from matplotlib import pyplot as plt
plt.style.use("ggplot")

count = 0
evens = 0
odds = 0
numbers = []
counts = []

number = int(input("Enter integer: "))

while number != 1:
	if number % 2 == 0:
		evens += 1
		number = int(number / 2)
	else:
		odds += 1
		number = int(number * 3 + 1)
	count += 1
	counts.append(count)
	numbers.append(number)
	
plt.plot(counts, numbers, color="k", linestyle="--", marker="o", label="Numbers")

plt.xlabel(f"Numbers\nSteps: {count}")
plt.ylabel(f"Results\nEvens: {evens} | Odds: {odds}")
plt.title("3x + 1 Illustration")
plt.grid(True)
plt.legend()
plt.show()

