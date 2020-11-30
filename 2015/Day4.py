import hashlib
m = hashlib.md5()
num = 1
string = 'iwrupvqb' + str(num)
m.update(string.encode(encoding='utf-8'))
psw = m.hexdigest()
while not psw.startswith("000000"):
    num += 1
    string = 'iwrupvqb' + str(num)
    m = hashlib.md5()
    m.update(string.encode(encoding='utf-8'))
    psw = m.hexdigest()
print(psw, num)
