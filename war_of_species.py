#Exercise 10
# reads through a filled 2d array in the form of a list (environment) and checks all of the surrounding characters (neighbours). The array will then change based on which neighbours surround others, based on rules defined beforehand (see description).
def warOfSpecies(environment):

    initial_environment_string = "".join(environment)
    final_environment = ""
    final_environment_list = []
    species_x = "X"
    species_o = "O"
    empty = "."

    height = 0
    width = 0
    for x in (environment):
        width += 1
        for y in x:
            height += 1

    height = int(height / width)

    for i in range (len(initial_environment_string)):
        species_x_neighbours = 0
        species_o_neighbours = 0
        empty_neighbours = 0
    # Top-left neighbour
        if i > height and i != (height*2)-1:
            if initial_environment_string[i-(height+1)] == empty:
                empty_neighbours += 1
            elif initial_environment_string[i-(height+1)] == species_x:
                species_x_neighbours += 1
            elif initial_environment_string[i-(height+1)] == species_o:
                species_o_neighbours += 1

    # Top neighbour
        if i not in [0,height,height*2]:
            if initial_environment_string[i-1] == empty:
                empty_neighbours += 1
            elif initial_environment_string[i-1] == species_x:
                species_x_neighbours += 1
            elif initial_environment_string[i-1] == species_o:
                species_o_neighbours += 1
    # Top-right neighbour
        if i < height*2 and i not in [0,height]:
            if initial_environment_string[i+(height-1)] == empty:
                empty_neighbours += 1
            elif initial_environment_string[i+(height-1)] == species_x:
                species_x_neighbours += 1
            elif initial_environment_string[i+(height-1)] == species_o:
                species_o_neighbours += 1
    # Left neighbour
        if i > height-1:
            if initial_environment_string[i-height] == empty:
                empty_neighbours += 1
            elif initial_environment_string[i-height] == species_x:
                species_x_neighbours += 1
            elif initial_environment_string[i-height] == species_o:
                species_o_neighbours += 1
    # Right neighbour
        if i < height*2:
            if initial_environment_string[i+height] == empty:
                empty_neighbours += 1
            elif initial_environment_string[i+height] == species_x:
                species_x_neighbours += 1
            elif initial_environment_string[i+height] == species_o:
                species_o_neighbours += 1
    # Bottom-left neighbour
        if i > height-1 and i not in [(height*2)-1,(height*width)-1]:
            if initial_environment_string[i-(height-1)] == empty:
                empty_neighbours += 1
            elif initial_environment_string[i-(height-1)] == species_x:
                species_x_neighbours += 1
            elif initial_environment_string[i-(height-1)] == species_o:
                species_o_neighbours += 1
    # Bottom neighbour
        if i not in [height-1,(height*2)-1,(height*width)-1]:
            if initial_environment_string[i+1] == empty:
                empty_neighbours += 1
            elif initial_environment_string[i+1] == species_x:
                species_x_neighbours += 1
            elif initial_environment_string[i+1] == species_o:
                species_o_neighbours += 1
     # Bottom-right neighbour
        if i < (height*2)-1 and i not in [height-1,(height*width)-1]:
             if initial_environment_string[i+(height+1)] == empty:
                 empty_neighbours += 1
             elif initial_environment_string[i+(height+1)] == species_x:
                 species_x_neighbours += 1
             elif initial_environment_string[i+(height+1)] == species_o:
                 species_o_neighbours += 1

        if initial_environment_string[i] == empty and species_x_neighbours >= 2 or initial_environment_string[i] == empty and species_o_neighbours >= 2:
                    if species_x_neighbours > species_o_neighbours:
                        most_common_neighbour = species_x
                        final_environment += most_common_neighbour
                    elif species_o_neighbours > species_x_neighbours:
                        most_common_neighbour = species_o
                        final_environment += most_common_neighbour


        elif initial_environment_string[i] != empty and species_o_neighbours + species_x_neighbours > 6:
            final_environment += empty

        elif initial_environment_string[i] == species_x and species_x_neighbours < 3:
            final_environment += empty

        elif initial_environment_string[i] == species_x and species_x_neighbours < species_o_neighbours:
            final_environment += empty


        elif initial_environment_string[i] == species_o and species_o_neighbours < 3:
            final_environment += empty

        elif initial_environment_string[i] == species_o and species_o_neighbours < species_x_neighbours:
            final_environment += empty


        else:
            final_environment += initial_environment_string[i]

    while final_environment:
        final_environment_list.append(final_environment[:height])
        final_environment = final_environment[height:]

    return final_environment_list
