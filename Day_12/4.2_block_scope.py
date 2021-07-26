

# game_level = 3
# enemies = ["Skeleton","Zombie","Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]
# print(new_enemy)#Skeleton

# def create_enemy():
#     enemies = ["Skeleton","Zombie","Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
# print(new_enemy) #NameError: name 'new_enemy' is not defined

game_level = 3
def create_enemy():
    enemies = ["Skeleton","Zombie","Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
        print(enemies)#['Skeleton', 'Zombie', 'Alien']
    print(new_enemy)#Skeleton
    print(enemies)#['Skeleton', 'Zombie', 'Alien']
print(enemies)#NameError: name 'enemies' is not defined

create_enemy()
"""
The most important thing to remember from this is if you create a variable
within a function, then it's only available within that function.

But if you create a variable within an if block or a while loop or a for loop or
anything that has the indentation and the colon,
then that does not count as creating a separate local scope.
"""