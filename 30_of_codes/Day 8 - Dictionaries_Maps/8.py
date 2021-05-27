# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phonebook = dict()
for i in range(n):
    name = input()
    name = name.split()
    phonebook[name[0]] = phonebook.get(name[0], name[1])

while 1:
    try:
        q = input()
        if q in phonebook:
            print(str(q)+"="+str(phonebook[q]))
        else:
            print("Not found")
    except:
        break
