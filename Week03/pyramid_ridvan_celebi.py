def calculate_pyramid_height(numofblocks):
    height = 0
    used_blocks = 0

    while used_blocks + (height + 1) <= numofblocks:
        height += 1
        used_blocks += height

    return height


print(calculate_pyramid_height(11))



