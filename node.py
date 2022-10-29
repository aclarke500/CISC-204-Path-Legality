class Node:

    #Class attributes
    
    #To be implemented: light status (red/green)

    '''
    args are name + clockwise
    parameter
        north: o / i ("out" or "in" )
        east: o / i ("out" or "in" )
        south: o / i ("out" or "in" )
        west: o / i ("out" or "in" )
        name: String (name of node)
    '''
    def __init__(self, name, north, east, south, west):
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.name = name
        self.is_obstacle = False
        
        # the status of the light would go here
        # it would be checked in the main code, and if it is red it would alter the status of the directions one may exit the node in.

    def is_obstacle(self):
        self.north = False
        self.south = False
        self.east = False
        self.west = False
        self.is_obstacle = True
