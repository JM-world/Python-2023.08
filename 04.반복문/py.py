a = input()
b = a.split(';')
c = list(map(int, b))
c.sort(reverse=True)
c