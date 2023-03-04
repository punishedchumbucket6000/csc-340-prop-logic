import ttg

# prop_vars = [
#     'p', # It's rainy outside
#     'q'  # I am inside
              
# ]

# prop_expressions = ['p and q',
#                     'p or q',
#                     '~p',
#                     'p => q',
#                     'p = q'
                    
# ]

# prop_vars = [
#     'P11', #Pit in location(1,1)
#     'B11', 
#     'P21',
#     'B21',
#     'P22',
#     'P31'
    

# ]

# prop_expressions = [
#     '~P11', #There is no pit in location(1,1)
#     'B11 = (P11 or P21)',    #There is a breeze in location(1,1) if only if there is a pit in location(1,1) ...
#     'B21 = (P11 or P22 or P31)'
    

# ]

# print(ttg.Truths(prop_vars, prop_expressions))
# #prints every possible combo

# perceptrons = [
#     "~B11",
#     "B21"
# ]

# prop_expressions = prop_expressions + perceptrons

# print(ttg.Truths(prop_vars, prop_expressions))

# * If it is rainy outside I am inside
# * If I am inside I am NOT outside and vice versa.
# * If I am outside I am either in my car are on a walk
# * If I am in my car, I am NOT on a walk and vice versa.
# * IF I go on a walk I wear a sweater

# NOT Rainy Outside
# I am on a walk

prop_vars = [
    "RainyOutside",
    "Inside",
    "Outside",
    "InCar",
    "OnWalk",
    "WearSweater"


]

prop_expressions = [
    'RainyOutside => Inside',
    'Inside = ~Outisde',
    'Outside => (InCar or OnWalk)',
    'InCar = ~OnWalk', # * If I am in my car, I am NOT on a walk and vice versa.
    'OnWalk => WearSweater' # * IF I go on a walk I wear a sweater
    


]

perceptrons = [
    "~RainyOutside",
    "OnWalk"
]

prop_expressions = prop_expressions + perceptrons

print(ttg.Truths(prop_vars, prop_expressions))