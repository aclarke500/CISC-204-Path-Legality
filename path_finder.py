# To do: implement time functionality, red lights, make boolean logic more apparent.
# Stretch goals: implement speed, speed limits, traffic.

from node import Node

o = "out"
i = "in"



#setting up the grid from the image

n=[
    [Node("00", False, i, i, False), Node("01", False, o, False, o), Node("02", False, o, False, i), Node("03", False, False, i, i)],
    [Node("10", o, False, o, False), Node("11", False, False, False, False), Node("12", False, False, False, False), Node("31", o, False, o, False)],
    [Node("20", i, i, i, False), Node("21", False, o, o, o), Node("22", False, o, i, i), Node("23", i, False, o, i,)],
    [Node("30", o, o, False, False), Node("31", i, o, False, i), Node("32", o, o, False, i), Node("33", i, False, False, i)],
]

#nodes to set null: 11, 12


# for i in range(0, 4):
#     print("******")
#     for j in range(0, len(n)):
#      print(n[j][i].north)


path_1=[n[3][0],n[3][1], n[3][2], n[2][2]]

for node in path_1:
    print(node.name)

def direction(node_A, node_B):
    name_A = node_A.name  
    name_B = node_B.name  
    if name_A[1] > name_B[1]:
        return node_B.west
    elif name_A[1] < name_B[1]:
        return node_B.east
    elif name_A > name_B:
        return node_B.north
    else:
        return node_B.south

def verify(A, B, C):
    if direction(A, B) == i:
        if direction(B, C) == o: # Could be better represented with boolean logic.
            return True
        return False
    return False
