import sys
import getopt
import re
import copy


def replace_leftmost(string, replaced, replacement):
    replace_index = string.index(replaced)
    return string[:replace_index] + replacement + string[replace_index + len(replaced):]

def eval_expression(expression):
    if '(' in expression or ')' in expression:
        print("Too complicated!")
        return
    else:
        while re.search(r'\d+\s[*+]\s\d+', expression):
            expression_to_evaluate = re.search(r'\d+\s[*+]\s\d+', expression).group(0)
            value = str(eval(expression_to_evaluate))
            expression = replace_leftmost(expression, expression_to_evaluate, value)
        return expression

def new_eval_expression(expression):

    while re.search(r'\d+\s\+\s\d+', expression):
        expression_to_evaluate = re.search(r'\d+\s\+\s\d+', expression).group(0)
        value = str(eval(expression_to_evaluate))
        expression = replace_leftmost(expression, expression_to_evaluate, value)

    while re.search(r'\d+\s\*\s\d+', expression):
        expression_to_evaluate = re.search(r'\d+\s\*\s\d+', expression).group(0)
        value = str(eval(expression_to_evaluate))
        expression = replace_leftmost(expression, expression_to_evaluate, value)

    return expression

# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_18.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_18.py [-h | --help]')
            print('Advent of Code 2020 Day 18')
            sys.exit()

    file_input = open('inputs/2020/Input_18.txt', 'r')
    expressions = file_input.readlines()
    file_input.close()
    evaluations = copy.deepcopy(expressions)
    while any('(' in e for e in evaluations):
        new_evaluations = []
        for index, evaluation in enumerate(evaluations):
            parentheses_expressions = re.findall(r'\(([\d\s+*]+)\)', evaluation)
            if parentheses_expressions:
                new_expression = evaluation
                for expression in parentheses_expressions:
                    value = eval_expression(expression)
                    replacing_expression = '({})'.format(expression)
                    new_expression = new_expression.replace(replacing_expression, value)
                new_evaluations.append(new_expression)
            else:
                new_evaluations.append(evaluation)
        evaluations = new_evaluations
    for index, evaluation in enumerate(evaluations):
        evaluations[index] = eval_expression(evaluation)

    print(sum(list(map(int, evaluations))))

    part2_evaluations = copy.deepcopy(expressions)
    while any('(' in e for e in part2_evaluations):
        new_evaluations = []
        for index, evaluation in enumerate(part2_evaluations):
            parentheses_expressions = re.findall(r'\(([\d\s+*]+)\)', evaluation)
            if parentheses_expressions:
                new_expression = evaluation
                for expression in parentheses_expressions:
                    value = new_eval_expression(expression)
                    replacing_expression = '({})'.format(expression)
                    new_expression = new_expression.replace(replacing_expression, value)
                new_evaluations.append(new_expression)
            else:
                new_evaluations.append(new_eval_expression(evaluation))
        part2_evaluations = new_evaluations

    for index, evaluation in enumerate(part2_evaluations):
        part2_evaluations[index] = new_eval_expression(evaluation)
    print(sum(list(map(int, part2_evaluations))))

if __name__ == "__main__":
    main(sys.argv[1:])