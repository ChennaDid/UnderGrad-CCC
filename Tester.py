import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as patches
import math

fibre_list = [[6, 36, 3.5], [25, 95, 3.5], [55, 54, 3.5], [54, 36, 3.5], [68, 63, 3.5], [75, 51, 3.5], [51, 88, 3.5], [2, 43, 3.5], [107, 43, 3.5], [33, 89, 3.5], [12, 92, 3.5], [32, 9, 3.5], [77, 99, 3.5], [36, 27, 3.5], [60, 93, 3.5], [83, 77, 3.5], [69, 25, 3.5], [20, 51, 3.5], [23, 58, 3.5], [20, 21, 3.5], [47, 48, 3.5], [61, 25, 3.5], [53, 18, 3.5], [79, 62, 3.5], [10, 51, 3.5], [39, 100, 3.5], [18, 44, 3.5], [33, 54, 3.5], [61, 81, 3.5], [40, 65, 3.5], [41, 93, 3.5], [78, 85, 3.5], [2, 60, 3.5], [107, 60, 3.5], [38, 4, 3.5], [90, 8, 3.5], [49, 27, 3.5], [97, 47, 3.5], [103, 87, 3.5], [-2, 87, 3.5], [88, 23, 3.5], [11, 10, 3.5], [20, 71, 3.5], [29, 2, 3.5], [29, 107, 3.5], [83, 14, 3.5], [47, 78, 3.5], [5, 100, 3.5], [96, 12, 3.5], [14, 83, 3.5], [64, 51, 3.5], [76, 19, 3.5], [92, 41, 3.5], [27, 79, 3.5], [95, 31, 3.5], [64, 18, 3.5], [60, 68, 3.5], [101, 19, 3.5], [39, 41, 3.5], [74, 42, 3.5], [82, 1, 3.5], [82, 106, 3.5], [8, 24, 3.5], [69, 103, 3.5], [69, -2, 3.5], [97, 97, 3.5], [14, 57, 3.5], [22, 14, 3.5], [69, 75, 3.5], [31, 17, 3.5], [75, 32, 3.5], [15, 104, 3.5], [15, -1, 3.5], [34, 76, 3.5], [82, 45, 3.5], [89, 62, 3.5], [25, 32, 3.5], [51, 67, 3.5], [91, 88, 3.5], [14, 35, 3.5], [63, 32, 3.5], [40, 52, 3.5], [57, 6, 3.5], [11, 75, 3.5], [19, 7, 3.5], [99, 4, 3.5], [46, 6, 3.5], [67, 96, 3.5], [97, 79, 3.5]]
void_list = [[85, 11, 3, 2], [57, 60, 3, 2], [5, 95, 3, 2], [100, 30, 3, 2], [88, 26, 3, 2], [34, 88, 3, 2], [94, 60, 3, 2], [25, 64, 3, 2], [6, 73, 3, 2], [38, 14, 3, 2], [80, 59, 3, 2], [35, 25, 3, 2], [20, 29, 3, 2], [83, 81, 3, 2], [74, 18, 3, 2], [11, 37, 3, 2], [95, 51, 3, 2], [30, 40, 3, 2], [98, 10, 3, 2], [29, 71, 3, 2], [39, 94, 3, 2], [96, 3, 3, 2], [96, 35, 3, 2], [51, 71, 3, 2], [73, 60, 3, 2], [72, 44, 3, 2], [25, 56, 3, 2], [38, 35, 3, 2]]
void_shape = "ellipse"
RVE_bounds = (105, 105)

width = RVE_bounds[0]
height = RVE_bounds[1]

fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, projection='3d')
plt.axis([-0.5 * width, 1.5 * width, -0.5 * height , 1.5 * height]) # sets axis value display limits
plt.axis("equal") # makes both axis equal display values
plt.show()

plt.suptitle("Generated RVE", fontsize=25)
rect = patches.Rectangle((0, 0), width, height, linewidth=1, edgecolor='r', facecolor='none')
plt.gca().add_artist(rect)

# Draw fibres
for fibre in fibre_list:
    c = plt.Circle((fibre[0], fibre[1]), radius = fibre[2], color='blue')
    plt.gca().add_artist(c)

if void_shape == "circle":
    # Draw circular voids
    for void in void_list:
        c = plt.Circle((void[0], void[1]), radius = void[2], color='black')
        plt.gca().add_artist(c)

if void_shape == "ellipse":
# Draw elliptical voids
    for void in void_list:
        ellipse = patches.Ellipse(xy=(void[0], void[1]), width=void[2] * 2, height=void[3] * 2, color='black')
        plt.gca().add_artist(ellipse)

plt.show()
