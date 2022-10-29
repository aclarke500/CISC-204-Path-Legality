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

    def is_obstacle(self):
        self.north = False
        self.south = False
        self.east = False
        self.west = False
        self.is_obstacle = True
