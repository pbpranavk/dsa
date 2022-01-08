class Meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos

def max_meetings(l, n):
    ans = []

    l = sorted(l, key=lambda x : x.end)
    ans.append(l[0].pos)
    time_limit = l[0].end

    for i in range(1, n):
        if l[i].start > time_limit:
            ans.append(l[i].pos)
            time_limit = l[i].end
    print([x + 1 for x in ans])


s = [ 1, 3, 0, 5, 8, 5 ]
f = [ 2, 4, 6, 7, 9, 9 ]
n = len(s)
l = []
for i in range(n):
    l.append(Meeting(s[i], f[i], i))

max_meetings(l, n)