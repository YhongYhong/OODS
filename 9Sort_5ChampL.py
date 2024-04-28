def bubble(l, v1, v2):
    for last in range(len(l)-1, 0, -1):
        swaped = False
        for i in range(last):
            if compare(v1, v2, i):
                l[i], l[i+1] = l[i+1], l[i]
                swaped = True
            
        if not swaped:
            break
    for i in range(len(l)):
        p = "{" + "'points': " + str(v1[i]) + "}"
        gd = "{" + "'gd': " + str(v2[i]) + "}"
        print(f"['{l[i][0]}', {p}, {gd}]")
    return l

def compare(v1, v2, i):
    if int(v1[i]) < int(v1[i+1]):
        v1[i], v1[i+1] = v1[i+1], v1[i]
        v2[i], v2[i+1] = v2[i+1], v2[i]
        return True
    else:
        if int(v1[i]) == int(v1[i+1]) and int(v2[i]) < int(v2[i+1]):
            v1[i], v1[i+1] = v1[i+1], v1[i]
            v2[i], v2[i+1] = v2[i+1], v2[i]
            return True
        return False

def getPointandGD(l):
    points = 3 * int(l[1]) + 0 * int(l[2]) + 1 * int(l[3])
    gd = int(l[4]) - int(l[5])
    return points, gd

inp = input("Enter Input : ").split('/')
team = []
p = []
gd = []
for i in inp:
    team_score = i.split(',')
    team.append(team_score)
    p.append(getPointandGD(team_score)[0])
    gd.append(getPointandGD(team_score)[1])
print('== results ==')
bubble(team, p, gd)