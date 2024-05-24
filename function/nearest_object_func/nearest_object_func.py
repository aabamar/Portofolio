def calc_dist(A, B):
    '''
    Function to calculate distance between two objects

    Parameters
    ----------
    A : list
        The coordinates of object A

    B : list
        The coordinates of object B

    Returns
    -------
    dist : float
        The distance between A & B
    '''

    dist = (((A[0] - B[0]) ** 2) + ((A[1] - B[1]) ** 2))**0.5 #code for calculate distance between two objects
    return dist #return dist variable

def find_nearest(current_coor, place_coor, place_name):
    '''
    Function to find nearest place object near current coordinates

    Parameters
    ----------
    current_coor : list
        The guest current coordinate

    place_coor : list
        The place object coordinates

    toursim_name : list
        The place object name

    Returns
    -------
    nearest_object : dict
        The dictionary of nearest place object
    '''
  
    list_dist = [] #define list_dist list variable
    num = 0 #define while parameter

    while num < len(place_coor): #code for calculate neaerest place object
      list_dist.append(calc_dist(current_coor, place_coor[num])) #code for add calculated distance between current coordination with place object coordination

      num += 1

    #determine nearest place object for current coordination
    nearest_dist = min(list_dist)
    nearest_object = {'object' : place_name[list_dist.index(nearest_dist)], 'dist': nearest_dist}

    return nearest_object #return nearest_object variable