import copy


class Character(object):
    def __init__(self, hp, mp, attack):
        super(Character, self).__init__()
        self.hp = hp
        self.mp = mp
        self.attack = attack

    def reset(self, hp, mp):
        self.hp = hp
        self.mp = mp

def get_available_actions(character_mp, timer):
    actions = []
    if character_mp >= 53:
        actions.append('M')
    if character_mp >= 73:
        actions.append('D')
    if character_mp >= 113 and timer['S'] <= 1:
        actions.append('S')
    if character_mp >= 173 and timer['P'] <= 1:
        actions.append('P')
    if character_mp >= 229 and timer['R'] <= 1:
        actions.append('R')
    return actions

def update_stat(player_action, stat):

    if stat['mode'] == 'hard':
        stat['character_hp']['player'] -= 1
        if stat['character_hp']['player'] <= 0:
            stat['status'] = 'Lose'
            return

    stat['actions'].append(player_action)

    if stat['timer']['S'] > 0:
        stat['timer']['S'] -= 1
    if stat['timer']['P'] > 0:
        stat['character_hp']['enemy'] -= 3
        stat['timer']['P'] -= 1
    if stat['timer']['R'] > 0:
        stat['character_mp'] += 101
        stat['timer']['R'] -= 1
    if stat['character_hp']['enemy'] <= 0:
        stat['status'] = 'Win'
        return

    if player_action == 'M':
        stat['character_mana_cost'] += 53
        stat['character_mp'] -= 53
        stat['character_hp']['enemy'] -= 4
    elif player_action == 'D':
        stat['character_mana_cost'] += 73
        stat['character_mp'] -= 73
        stat['character_hp']['enemy'] -= 2
        stat['character_hp']['player'] += 2
    elif player_action == 'S' and stat['timer']['S'] == 0:
        stat['character_mana_cost'] += 113
        stat['character_mp'] -= 113
        stat['timer']['S'] = 6
    elif player_action == 'P' and stat['timer']['P'] == 0:
        stat['character_mana_cost'] += 173
        stat['character_mp'] -= 173
        stat['timer']['P'] = 6
    elif player_action == 'R' and stat['timer']['R'] == 0:
        stat['character_mana_cost'] += 229
        stat['character_mp'] -= 229
        stat['timer']['R'] = 5

    if stat['timer']['S'] > 0:
        player_defense = 7
        stat['timer']['S'] -= 1
    else:
        player_defense = 0
    if stat['timer']['P'] > 0:
        stat['character_hp']['enemy'] -= 3
        stat['timer']['P'] -= 1
    if stat['timer']['R'] > 0:
        stat['character_mp'] += 101
        stat['timer']['R'] -= 1

    if stat['character_hp']['enemy'] <= 0:
        stat['status'] = 'Win'
        return
    stat['character_hp']['player'] -= (9 - player_defense) if 9 > player_defense else 1
    if stat['character_hp']['player'] <= 0:
        stat['status'] = 'Lose'
        return


enemy_hp, enemy_attack = 51, 9
player_hp, player_mp = 50, 500

min_winning_mana_cost = 10 ** 100
battle_stats = [{'character_hp': {'player': player_hp, 'enemy': enemy_hp},
                 'timer': {'S': 0, 'P': 0, 'R': 0},
                 'character_mp': player_mp,
                 'character_mana_cost': 0,
                 'status': 'continue',
                 'actions': [],
                 'mode': 'normal'
                 }]
while len(battle_stats) > 0:
    new_stats = []
    for battle_stat in battle_stats:
        available_actions = get_available_actions(battle_stat['character_mp'], battle_stat['timer'])
        for action in available_actions:
            new_round_stat = copy.deepcopy(battle_stat)
            update_stat(action, new_round_stat)
            if new_round_stat['character_mana_cost'] < min_winning_mana_cost:
                if new_round_stat['status'] == 'Win':
                    min_winning_mana_cost = new_round_stat['character_mana_cost']
                elif new_round_stat['status'] == 'continue':
                    new_stats.append(new_round_stat)
    battle_stats = new_stats
print(min_winning_mana_cost)

min_winning_mana_cost = 10 ** 100
battle_stats = [{'character_hp': {'player': player_hp, 'enemy': enemy_hp},
                 'timer': {'S': 0, 'P': 0, 'R': 0},
                 'character_mp': player_mp,
                 'character_mana_cost': 0,
                 'status': 'continue',
                 'actions': [],
                 'mode': 'hard'
                 }]
while len(battle_stats) > 0:
    new_stats = []
    for battle_stat in battle_stats:
        available_actions = get_available_actions(battle_stat['character_mp'], battle_stat['timer'])
        for action in available_actions:
            new_round_stat = copy.deepcopy(battle_stat)
            update_stat(action, new_round_stat)
            if new_round_stat['character_mana_cost'] < min_winning_mana_cost:
                if new_round_stat['status'] == 'Win':
                    min_winning_mana_cost = new_round_stat['character_mana_cost']
                    print(new_round_stat)
                elif new_round_stat['status'] == 'continue':
                    new_stats.append(new_round_stat)
    battle_stats = new_stats
print(min_winning_mana_cost)
