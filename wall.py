def least_bricks(n):

    max_bricks_5 = n // 5
    
    
    for bricks_5 in range(max_bricks_5, -1, -1):
        
        remaining_height = n - 5 * bricks_5
        
        
        if remaining_height % 2 == 0:
            bricks_2 = remaining_height // 2
            return bricks_5 + bricks_2
            
    
    return -1


wall_height = 28
result = least_bricks(wall_height)
if result != -1:
    print("The least amount of a combination of bricks of height 5 and 2 is:", result)
else:
    print("It is not possible to form the wall height", wall_height, "with bricks of height 5 and 2.")
