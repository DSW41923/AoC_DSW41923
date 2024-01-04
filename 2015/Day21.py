import re
import itertools


class Character(object):
    def __init__(self, hp, attack, defense):
        super(Character, self).__init__()
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def equip(self, equipment):
        self.attack += equipment[1]
        self.defense += equipment[2]

    def reset(self, base_attack=0, base_defense=0):
        self.attack = base_attack
        self.defense = base_defense

def battle(player, enemy):
    character_hp = {'player': player.hp, 'enemy': enemy.hp}
    while True:
        character_hp['enemy'] -= player.attack - enemy.defense if player.attack > enemy.defense else 1
        if character_hp['enemy'] <= 0:
            return 'Player Wins!'
        character_hp['player'] -= enemy.attack - player.defense if enemy.attack > player.defense else 1
        if character_hp['player'] <= 0:
            return 'Enemy Wins!'

def get_binary_with_length(x, length):
    text_num = bin(x).replace('0b', '')
    while len(text_num) < length:
        text_num = '0' + text_num
    return text_num


file_input = open('../inputs/2015/input-D21.txt', 'r')
input_strings = file_input.read()
file_input.close()

enemy_hp, enemy_attack, enemy_defense = re.findall(r'\d+', input_strings)
player_H = Character(hp=100, attack=0, defense=0)
boss = Character(hp=int(enemy_hp), attack=int(enemy_attack), defense=int(enemy_defense))
# Get equipments
weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
armors = [(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
rings = [(0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]
two_ring_combinations = itertools.combinations(rings, 2)
all_ring_combinations = [(0, 0, 0)]
for r1, r2 in two_ring_combinations:
    all_ring_combinations.append((r1[0]+r2[0], r1[1]+r2[1], r1[2]+r2[2]))

winning_set_cost = []
losing_set_cost = []
for w in weapons:
    for a in armors:
        for r in all_ring_combinations:
            player_H.equip(w)
            player_H.equip(a)
            player_H.equip(r)
            equipment_cost = w[0] + a[0] + r[0]
            if battle(player_H, boss) == 'Player Wins!':
                winning_set_cost.append(equipment_cost)
            else:
                losing_set_cost.append(equipment_cost)
            player_H.reset()
print(min(winning_set_cost))
print(max(losing_set_cost))