"""
    Environment maps for modified vacuum cleaner world
"""
#Trivial 3x3
def Trivial():
    env_map = \
    [["H", "H", "H"],
    ["H", "XA", "H"], 
    ["H", "H", "H"]] 
    return env_map

#Flooded Basement 5x5
def Flooded_Basement():
    env_map = \
    [["H", "H", "H", "H", "H"], 
    ["H", "X", "X", "X", "H"], 
    ["H", "X", "XA", "X", "H"], 
    ["H", "X", "X", "X", "H"], 
    ["H", "H", "H", "H", "H"]] 
    return env_map

#L-Living Room 9x9
def Living_Room():
    env_map = \
    [["H", "H", "H", "H", "H", "H", "H", "H", "H"], 
    ["H", "X", "O", "X", "X", "O", "O", "X", "H"], 
    ["H", "X", "O", "X", "X", "X", "X", "O", "H"], 
    ["H", "X", "O", "O", "O", "X", "X", "X", "H"], 
    ["H", "O", "O", "X", "O", "O", "X", "O", "H"], 
    ["H", "H", "X", "H", "H", "X", "O", "X", "H"], 
    ["H", "H", "X", "H", "H", "O", "X", "O", "H"], 
    ["H", "H", "X", "H", "H", "O", "X", "OA", "H"], 
    ["H", "H", "H", "H", "H", "H", "H", "H", "H"]]
    return env_map

#Dirty Closet 11x11
def Dirty_Closet():
    env_map = \
    [["H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H"], 
    ["H", "O", "O", "O", "O", "O", "O", "O", "O", "O", "H"], 
    ["H", "O", "H", "H", "H", "X", "H", "H", "H", "O", "H"], 
    ["H", "O", "H", "X", "X", "X", "X", "X", "H", "O", "H"], 
    ["H", "O", "H", "X", "X", "X", "X", "X", "H", "O", "H"], 
    ["H", "O", "H", "X", "X", "X", "X", "X", "H", "O", "H"], 
    ["H", "O", "H", "H", "H", "H", "H", "H", "H", "O", "H"], 
    ["H", "O", "O", "O", "O", "O", "O", "O", "O", "O", "H"], 
    ["H", "O", "O", "O", "O", "OA", "O", "O", "O", "O", "H"], 
    ["H", "O", "O", "O", "O", "O", "O", "O", "O", "O", "H"], 
    ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H"]] 
    return env_map