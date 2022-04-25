x = int(input())
n = list()

for i in range(10):
    if i == 0:
        n.append(x)
    else:
        x = x * 2
        n.append(x)
    print(f'N[{i}] = {x}')
