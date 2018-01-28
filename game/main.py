from enemy import Troll, Vampyre

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

# monster = Enemy("Basic enemy")
# monster.grunt()

alucard = Vampyre("Alucard")
print(alucard)

# alucard.take_damage(12)
ugly_troll.take_damage(12)
another_troll.take_damage(9)
brother.take_damage(8)

print("-" * 40)
another_troll.take_damage(30)
print(another_troll)

# while alucard.alive:
#     alucard.take_damage(1)
#         print(alucard)

alucard.lives = 0
alucard.hit_points = 1
print(alucard)