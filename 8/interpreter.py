INPUT_FILE = 'my_input.txt'

def get_instructions(filename):
    instructions = []
    with open(INPUT_FILE) as fp:
        for line in fp:
            instructions.append(line.strip())
    return instructions

def evaluate(instructions, fix_corruption, cur_line = 0, accumulator = 0):
    lines_executed = {}
    while cur_line < len(instructions):
        instruction = instructions[cur_line]
        lines_executed[cur_line] = True
        cmd, str_value = instruction.split(' ')
        value = int(str_value)
        if cmd == 'acc':
            accumulator += value
            cur_line += 1
        elif cmd == 'jmp':
            if fix_corruption:
                print('JMP!!!!!!!!', cur_line)
                new_instructions = instructions[:]
                new_instructions[cur_line] = 'nop ' + str_value
                new_acc = accumulator
                new_accumulator, has_loop = evaluate(new_instructions, False, cur_line, new_acc)
                if not has_loop:
                    return new_accumulator, has_loop
            cur_line += value
        elif cmd == 'nop':
            if fix_corruption:
                print('NOP!!!!!!!', cur_line)
                new_instructions = instructions[:]
                new_instructions[cur_line] = 'jmp ' + str_value
                new_acc = accumulator
                new_accumulator, has_loop = evaluate(new_instructions, False, cur_line, new_acc)
                if not has_loop:
                    return new_accumulator, has_loop
            cur_line += 1
        if cur_line in lines_executed:
            return accumulator, True
    return accumulator, False

instructions = get_instructions(INPUT_FILE)
acc, has_loop = evaluate(instructions, True, 0)
print(acc, has_loop)
