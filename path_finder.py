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


def verify(A, B):
    # use the .name method to figure out relation between nodes
    # i.e 30 -> 31 is going right
    return
