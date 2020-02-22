"""
ANH HUYNH
CECS 174
2/10/2020
"""

import math

def main():
    # input from user
    side_len = float(input("Enter Side Length of Garden (ft): "))
    itm_space = float(input("Enter Recommeneded Spacing Between Plants (ft): "))
    dep_flower_bed = float(input("Enter Depth of Flowerbed (ft): "))
    dep_filled_area = float(input("Enter Depth of Filled Area (ft): "))

    # calculate fill and soil areas
    r = side_len / 4
    soil_area = 3 * (math.pi * math.pow(r, 2))   
    filled_area = math.pow(side_len, 2) - soil_area  
    
    # calculate cubic yards of fill and soil in yards
    circle_soil = round(soil_area / 3 * dep_flower_bed / 3, 1)
    semicir_soil = round(soil_area / 6 * dep_flower_bed / 3, 1) * 4
    total_soil = round(circle_soil + semicir_soil, 1)

    total_filled = round(filled_area * dep_filled_area / 3, 1)

    # calculate needed flowers
    circle_flowers = math.trunc((soil_area / 3) // math.pow(itm_space, 2))
    semicir_flowers = math.trunc((soil_area / 6) // math.pow(itm_space, 2)) * 4
    total_flowers = circle_flowers + semicir_flowers

    # outputs
    print("\nYou'll need", circle_flowers, "flowers for the circle.")
    print("You'll need", semicir_flowers, "flowers for the semicircles.")
    print(total_flowers, "flowers in total.")

    print("\nYou'll need", circle_soil, "cubic yards of soil for the circle.")
    print("You'll need", semicir_soil, "cubic yards of soil for the semicircles.")
    print(total_soil, "cubic yards of soil in total.")
    print("\nAnd you'll need", total_filled, "cubic yards of fill in total.")
    
main()