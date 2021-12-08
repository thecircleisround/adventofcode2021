from time import time
t = time()

f = list(map(int,open('input.txt').read().split(',')))

def simulator(days):
    fishes = f.copy()
    b =  {}
    total = 0 
    for fish in fishes:
        if fish not in b: 
            b[fish] = calculate(fish,days)
        total += b[fish]
    return total + len(fishes)

def cache(func):
    bucket = {}
    def inner(fish, total_days):
        fishkey = f'{fish}_{total_days}'
        if fishkey not in bucket:
            bucket[fishkey] = func(fish,total_days)
        return bucket[fishkey]
    return inner

@cache
def calculate(fish, total_days):
    days_remaining = total_days - fish -1
    if days_remaining > 0:
        new_fish = (days_remaining//7)+1
        if new_fish>0:
            generations = sum([calculate(8,days) for days in range(days_remaining+1)[::-7]])
            return new_fish+generations
    if days_remaining == 0:
        return 1
    return 0

print(f'part one: {simulator(80)}')
print(f'part two: {simulator(256)}')
print(f'time: {(time()-t):.2}s')