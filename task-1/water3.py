def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4 

def successors(s):
    x, y, z = s
    return s[]
    process = []
    if x > 0 and y < 5:
        transfer = min(x, 5 - y)
        x -= transfer
        y += transfer
        process.append((x, y, z))
    if x > 0 and z < 3:
        transfer = min(x, 3 - z)
        x -= transfer
        z += transfer
        process.append((x, y, z))
    if y > 0 and x < 8:
        transfer = min(y, 8 - x)
        x += transfer
        y -= transfer
        process.append((x, y, z))
    if y > 0 and z < 3:
        transfer = min(y, 3 - z)
        y -= transfer
        z += transfer
        process.append((x, y, z))
    if z > 0 and x < 8:
        transfer = min(z, 8 - x)
        x += transfer
        z -= transfer
        process.append((x, y, z))
    if z > 0 and y < 5:
        transfer = min(z, 5 - y)
        y += transfer
        z -= transfer
        process.append((x, y, z))
    return process
