from matplotlib import pyplot as plt
plt.style.use("ggplot")

# X-axis values
x_axis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Y-axis values
line_0 = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

line_1 = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

line_2 = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

# Plotting and styling of lines
plt.plot(x_axis, line_0, color="k", linestyle="--", marker="o", label="Line 0")
plt.plot(x_axis, line_1, color="b", marker="o", linewidth=3, label="Line 1")
plt.plot(x_axis, line_2, color="y", marker="o", linewidth=3, label="Line 2")

# Plot setup
plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")
plt.title("Matplotlib Demonstration")
plt.grid(True)
plt.legend()
plt.show()
