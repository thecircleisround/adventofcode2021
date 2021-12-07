import time

start = time.time()

class Plotter:
    def __init__(self,input_file):
        self.movement = {}
        self.all_coords = [self.make_coords(line) for line in input_file]

    def start_moving(self,diagonal=False):
        for coords in self.all_coords:
            x1, y1, x2, y2 = coords
            if x1 == x2:
                _y1, _y2 = sorted([y1,y2])
                self.make_move(_y1,_y2,x1,invert=True)

            elif y1==y2: 
                _x1, _x2 = sorted([x1, x2])
                self.make_move(_x1,_x2,y1)

            elif diagonal:
                sorted_coords = sorted([(x1,y1),(x2,y2)], key=lambda x: x[0])
                _x1, _y1, _x2, _y2 = [y for x in sorted_coords for y in x]
                mod = -1 if _y1 > _y2 else 1
                self.make_move(_x1,_x2,_y1,base_mod=mod)

        return len([x for x in self.movement.values() if x >= 2])

    def make_move(self,start, end, base_point, invert=False, base_mod=None):
        for point in range(start, end+1):
            move = f'{base_point},{point}' if invert else f'{point},{base_point}'

            if base_mod:
                base_point += base_mod
            if move in self.movement:
                self.movement[move] += 1
            else: 
                self.movement[move] = 1

    def make_coords(self, line):
        coords = line.split(',')
        coords[1:2] = coords[1].split(' -> ')
        coords = [int(coord) for coord in coords]
        return coords

input_file = open('input.txt').read().splitlines()

print(f'part one: {Plotter(input_file).start_moving()}')
print(f'part two: {Plotter(input_file).start_moving(diagonal=True)}')
print(f'Ran in {time.time()-start:.2}s')
