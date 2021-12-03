input_file = list(map(int,open('input.txt').read().splitlines()))

def part_one(input_file:list):
    increases = [y for x,y in enumerate(input_file[1:]) if input_file[x] < y]
    return len(increases)

def part_two(input_file):
    sliding_sums =  [input_file[i-3]<input_file[i] for i in range(3,len(input_file))]
    return sum(sliding_sums)

print(part_one(input_file))
print(part_two(input_file))



