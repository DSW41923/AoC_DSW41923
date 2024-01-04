input_string = open('inputs/2015/input-D14.txt', 'r')
reindeer_data_string = input_string.readlines()
input_string.close()
reindeer_data = []
for x in reindeer_data_string:
    words = x.split(' ')
    reindeer_data.append({
        'name': words[0],
        'speed': int(words[3]),
        'runtime': int(words[6]),
        'resttime': int(words[-2])})

race_time = 2503
max_reindeer_distance = 0
for reindeer in reindeer_data:
    runresttime = reindeer['runtime'] + reindeer['resttime']
    run_round = race_time // runresttime
    reindeer_distance = reindeer['runtime'] * reindeer['speed'] * run_round
    last_round_time = race_time % runresttime
    if last_round_time >= reindeer['runtime']:
        reindeer_distance += reindeer['runtime'] * reindeer['speed']
    else:
        reindeer_distance += last_round_time * reindeer['speed']

    if reindeer_distance > max_reindeer_distance:
        max_reindeer_distance = reindeer_distance
print(max_reindeer_distance)

reindeer_realtime_distances = [0] * len(reindeer_data)
reindeer_realtime_scores = [0] * len(reindeer_data)
for time in range(race_time):
    for reindeer_id, reindeer in enumerate(reindeer_data):
        runresttime = reindeer['runtime'] + reindeer['resttime']
        if time % runresttime < reindeer['runtime']:
            reindeer_realtime_distances[reindeer_id] += reindeer['speed']
    max_distance = max(reindeer_realtime_distances)
    for reindeer_id, distance in enumerate(reindeer_realtime_distances):
        if distance == max_distance:
            reindeer_realtime_scores[reindeer_id] += 1
print(max(reindeer_realtime_scores))