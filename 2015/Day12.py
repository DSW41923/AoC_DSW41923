import re
import json

string = open('../AoC_Inputs/2015/input-D12.txt', 'r')
input_string = string.read()
string.close()

number_sum = 0
numbers = re.findall(r'-?\d+', input_string)
number_sum += sum(map(int, numbers))
print(number_sum)

def remove_red_objects(objects):
    clean_objects = []
    for json_object in objects:
        if type(json_object) == list:
            clean_objects.append(remove_red_objects(json_object))
        elif type(json_object) == dict:
            if any(v == 'red' for v in json_object.values()):
                continue
            else:
                clean_objects.append(remove_red_objects(json_object.values()))
        else:
            clean_objects.append(json_object)
    return clean_objects


json_objects = json.loads(input_string)
new_json_objects = remove_red_objects(json_objects)
new_json_objects_string = json.dumps(new_json_objects)
new_number_sum = 0
new_numbers = re.findall(r'-?\d+', new_json_objects_string)
new_number_sum += sum(map(int, new_numbers))
print(new_number_sum)


