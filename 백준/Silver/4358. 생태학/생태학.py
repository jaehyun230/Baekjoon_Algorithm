import sys
 
m = {}
sum = 0
 
while True:
    name = sys.stdin.readline().strip()
    if not name:
        break
    m.setdefault(name, 0)
    m[name] += 1
    sum += 1
 
for name in sorted(m.keys()):
    print('{0} {1:0.4f}'.format(name, m[name]*100/sum))