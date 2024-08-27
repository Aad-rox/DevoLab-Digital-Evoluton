import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def is_visible(observation_point, x_, y_):
    obs_x, obs_y = observation_point

    # Step 1: Calculate the equation of the line
    if obs_x == x_:
        # Handle vertical line separately to avoid division by zero
        return True
    else:
        slope = (obs_y - y_) / (obs_x - x_)
        intercept = obs_y - slope * obs_x

    # Step 2: Find intersection points with f(x)

    # Define symbols
    x, y = symbols('x y')

    # Define functions
    func1 = Eq(x**2, y)
    func2 = Eq(slope * x + intercept, y)

    intersection_points = solve((func1, func2), (x, y))

    if len(intersection_points) == 1:
        return True
    else:
        shortest_dist = None
        closest_point = None
        for point in intersection_points:
            dist = distance(point[0], point[1], obs_x, obs_y)
            if shortest_dist is None or dist < shortest_dist:
                shortest_dist = dist
                closest_point = point

        if closest_point == (x_, y_):
            return True
        else:
            return False

# Create a range of x values
x_values = np.arange(-10, 10, 0.01)
y_values = x_values**2  # Function y = x^2

# Observation point
observation_point = (0, 15)

# Calculate visibility for each point on the function
visible_points = []
for x, y in zip(x_values, y_values):
    if is_visible(observation_point, x, y):
        visible_points.append((x, y))

# Plot the function
plt.plot(x_values, y_values, label='Function: $y = x^2$')

# Plot the visible points
if visible_points:
    visible_x, visible_y = zip(*visible_points)
    plt.scatter(visible_x, visible_y, color='red', label='Visible Points')

# Plot the observation point
plt.scatter(observation_point[0], observation_point[1], color='black', marker='o', label='Observation Point')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Visibility of Points on the Function')
plt.legend()

# Show plot
plt.grid(True)
plt.show()
