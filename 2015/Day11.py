import string

INCREASING_PATTERNS = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']
BANNED_LETTERS = ['i', 'l', 'o']

def letters_to_num(letters):
    num = 0
    for letter in letters:
        num *= 26
        num += string.ascii_lowercase.index(letter)
    return num

def num_to_letters(number):
    letters = ''
    while number > 0:
        index = number % 26
        letters = string.ascii_lowercase[index] + letters
        number = number // 26
    return letters

def increment_password(password):
    password_num = letters_to_num(password)
    while True:
        password_num += 1
        next_password = num_to_letters(password_num)
        if any((l in next_password) for l in BANNED_LETTERS):
            continue
        else:
            break
    return next_password

def get_next_valid_password(password):
    while True:
        new_password_candidate = increment_password(password)
        if any((p in new_password_candidate) for p in INCREASING_PATTERNS):
            pairs_count = 0
            pair_index = 1
            while pair_index < len(password):
                if new_password_candidate[pair_index] == new_password_candidate[pair_index - 1]:
                    pairs_count += 1
                    pair_index += 2
                else:
                    pair_index += 1
            if pairs_count >= 2:
                break
        password = new_password_candidate

    return new_password_candidate


input_password = 'vzbxkghb'
next_valid_password = get_next_valid_password(input_password)
print("Next valid password is {}".format(next_valid_password))
print("Second next valid password is {}".format(get_next_valid_password(next_valid_password)))
