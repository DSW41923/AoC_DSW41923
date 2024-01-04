import re


class Instructions(object):

    def __init__(self, inputs, output_wire, operation):
        self.inputs = inputs
        self.output_wire = output_wire
        self.operation = operation

    def getInputs(self):
        return self.inputs

    def getOutputWire(self):
        return self.output_wire

    def getOperation(self):
        return self.operation

    def __str__(self):
        return str(self.inputs) + " " + str(self.operation) + " " + self.output_wire


def calculate(wires, instructions, target):
    if type(target) == int:
        return target
    elif wires[target] == 0:
        try:
            curr = instructions[target]
        except:
            return wires[target]

        operator = curr.getOperation()
        if operator == '->':
            wires[target] = calculate(wires, instructions, curr.getInputs())
        elif operator == 'AND':
            wires[target] = calculate(wires, instructions, curr.getInputs()[0]) & calculate(wires, instructions, curr.getInputs()[1])
        elif operator == 'OR':
            wires[target] = calculate(wires, instructions, curr.getInputs()[0]) | calculate(wires, instructions, curr.getInputs()[1])
        elif operator == 'NOT':
            wires[target] = ~calculate(wires, instructions, curr.getInputs()) + 65536
        elif operator[0] == 'LSHIFT':
            wires[target] = calculate(wires, instructions, curr.getInputs()) << operator[1]
        elif operator[0] == 'RSHIFT':
            wires[target] = calculate(wires, instructions, curr.getInputs()) >> operator[1]
        else:
            print("Invalid Operation!")
        return wires[target]
    else:
        return wires[target]


def parse(string):
    content = string.replace('\n', '').split(' ')
    for x in content:
        if x.isdecimal():
            content[content.index(x)] = int(x)
    end = content[-1]
    if content[0] == 'NOT':
        operation = content[0]
        start = content[1]
    elif content[1] == 'AND' or content[1] == 'OR':
        operation = content[1]
        start = (content[0], content[2])
    elif content[1] == 'LSHIFT' or content[1] == 'RSHIFT':
        operation = (content[1], content[2])
        start = content[0]
    else:
        operation = "->"
        start = content[0]
    return Instructions(start, end, operation)


input_string = open('inputs/2015/input-D7.txt', 'r')
input_string = input_string.readlines()
wires = {}
instructions = {}
for line in input_string:
    content = parse(line)
    instructions[content.getOutputWire()] = parse(line)
    related_wires = re.findall(r'[a-z]{1,2}', line)
    for x in related_wires:
        if x not in wires.keys():
            wires[x] = 0
print("a = " + str(calculate(wires, instructions, 'a')))
