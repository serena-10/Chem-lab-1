#This code produces the bar graph for the measurements lab
import matplotlib.pyplot as plt
import numpy as np

# Measurements from the lab
volume = [10.0, 18.0, 27.0, 35.0, 43.0]
mass = [52.522, 61.485, 70.034, 78.752, 86.671]

# Calculate the average mass
average_mass = np.mean(mass)

# Calculate density using the slope of mass vs. volume
density = np.polyfit(volume, mass, 1)[0]

# Create the bar graph
plt.figure(figsize=(10, 6))

bars = plt.bar(
    ["10.0 mL", "18.0 mL", "27.0 mL", "35.0 mL", "43.0 mL"],
    mass,
    label="Mass (g)"
)

# Add average mass line
plt.axhline(
    average_mass,
    linestyle="--",
    label=f"Average Mass = {average_mass:.3f} g"
)

# Add density information to the graph
plt.axhline(
    density * np.mean(volume),
    linestyle=":",
    label=f"Density = {density:.3f} g/mL"
)

# Add the mass values above each bar
for bar, value in zip(bars, mass):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.5,
        f"{value:.3f}",
        ha="center"
    )

# Title and axis labels
plt.title("The Density of Water Using a Graduated Cylinder at 21.5°C")
plt.xlabel("Measurements")
plt.ylabel("Mass (g)")

# Add legend
plt.legend()

# Add grid lines
plt.grid(axis="y", linestyle="--", alpha=0.3)

# Display the graph
plt.tight_layout()
plt.show()
