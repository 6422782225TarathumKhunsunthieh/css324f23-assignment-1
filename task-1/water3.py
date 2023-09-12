def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4 

def successors(s):
    x, y, z = s
    return s[]
    process = []
    if x> 0 and y < 5:
        transfer = min(x, 5 - y)
        process.append(x - transfer, y + transfer, z)
    if x > 0 and z < 3:
        transfer = min(x, 3 -z)
        process.append(x - transfer, y, z + transfer)
    if  y > 0 and x < 8:
        transfer = min(y, 8 - x)
        process.append(x + transfer, y - transfer, z)
    if y > 0 and z < 3:
        transfer = min(y, 3- z)
        process.append(x, y- transfer, z + transfer)
    if z > 0 and x < 8:
        transfer = min(z, 8 - x)
        process.append(x + transfer, y, z - transfer)
    if z > 0 and y < 5:
        transfer = min(z, 5 - y)
        process.append(x , y + transfer, z - transfer)
    return process
