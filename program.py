a_dictionary = {}
a_file = open("input2.txt",'r')
count = 0
for line in a_file:
    if count == 0:
        key, value = line.split(':')
        emp = int(value)
    if count>3:
        key, value = line.split(':')
        a_dictionary[key] = int(value)
    count +=1
a_dictionary = dict(sorted(a_dictionary.items(), key=lambda item: item[1]))
ord_val= list(a_dictionary.values())
loop = len(ord_val)-emp
diff = []
for i in range(loop):
    diff.append(ord_val[i+emp-1]-ord_val[i])
req = min(diff)
st = diff.index(min(diff))
bino = list(a_dictionary.items())[st:st+emp]
f = open("output2.txt", "a")
f.write('The goodies selected for distribution are:\n\n')
for i in bino:
    f.write(i[0])
    f.write(':')
    f.write(str(i[1]))
    f.write('\n')
f.write('\n')
f.write('And the difference between the chosen goodie with highest price and the lowest price is ')
f.write(str(req))
f.close()
