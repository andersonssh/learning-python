def array_diff(a, b):
    return [x for x in a if x not in b]

print([f'Par detectado {i}' for i in range(10) if i % 2 == 0])
a = [1,2,3,4]

print(a.remove(1))
print(a)


def descending_order(num):
    return int(''.join(sorted(str(num),reverse=True)))

bb = [1,3,4] + [1,2,5]
print(bb)



print(descending_order(9876547321))

listakk = [{'oi': 'hi'},{'oi':'fine'}]
akk = [i['oi'] for i in listakk if i['oi']]
print(akk)
