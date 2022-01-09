class ItemValue:
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt

    def __lt__(self, other):
        return self.cost < other.cost

def get_max_val(wt, val, capacity):
    i_val = []

    for i in range(len(wt)):
        i_val.append(ItemValue(wt[i], val[i], i))

    i_val.sort(reverse=True)

    total_val = 0
    for i in i_val:
        curr_wt = int(i.wt)
        curr_val = int(i.val)

        if capacity - curr_wt > 0:
            capacity -= curr_wt
            total_val += curr_val
        else:
            fraction = capacity / curr_wt
            total_val += curr_val * fraction
            capacity = int(capacity - (curr_wt * fraction))
            break
    return total_val
wt = [10, 40, 20, 30]
val = [60, 40, 100, 120]
capacity = 50

print(get_max_val(wt, val, capacity))