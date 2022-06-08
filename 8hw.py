p = range(0,20)
it = iter(p)
l = [(1 + next(it)*5) for a in range(1,10)]
print(l)
it = iter(l)
while it:
    try:
        print(next(1))
    except:
        break