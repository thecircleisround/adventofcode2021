input_file = open('input.txt').read().splitlines()

def part_one():
    directives = {'forward':'x+=', 'down':'y+=', 'up':'y-='}
    x = 0 
    y = 0

    for directive in input_file:
        direction, mod = directive.split()
        mod = int(mod) 
        if direction == 'forward':
            x+=mod
        elif direction == 'down':
            y+=mod
        elif direction == 'up':
            y-=mod
    return x*y

def part_two():
    x=0
    y=0
    z=0
    
    for directive in input_file:
        direction, mod = directive.split()
        mod = int(mod) 

        if direction == 'down':
            z += mod
        if direction == 'up':
            z -= mod
        if direction == 'forward':
            x += mod
            y += z*mod

    return x*y

print(part_one())
print(part_two())
