def brain_luck(code, input):
    input_array = list(input)

    data_pointer = 0
    memory = [0] * 30_000
    input_pointer = 0
    output = ''
    ip = 0

    while ip < len(code):
        instr = code[ip]
        if instr == '>':
            data_pointer += 1
        elif instr == '<':
            data_pointer -= 1
        elif instr == '+':
            memory[data_pointer] = (memory[data_pointer] + 1) % 256
        elif instr == '-':
            memory[data_pointer] = (memory[data_pointer] - 1) % 256
        elif instr == '.':
            output += (chr(memory[data_pointer]))
        elif instr == ',':
            memory[data_pointer] = ord(input_array[input_pointer])
            input_pointer += 1
        elif instr == '[':
            if memory[data_pointer] == 0:
                loop = 1
                while loop > 0:
                    ip += 1
                    if code[ip] == '[':
                        loop += 1
                    elif code[ip] == ']':
                        loop -= 1
        elif instr == ']':
            loop = 1
            if memory[data_pointer] != 0:
                while loop > 0:
                    ip -= 1
                    if code[ip] == '[':
                        loop -= 1
                    elif code[ip] == ']':
                        loop += 1
        else:
            raise Exception('Invalid instruction')
        ip += 1

    return output

print(brain_luck(',>+>>>>++++++++++++++++++++++++++++++++++++++++++++>++++++++++++++++++++++++++++++++<<<<<<[>[>>>>>>+>+<<<<<<<-]>>>>>>>[<<<<<<<+>>>>>>>-]<[>++++++++++[-<-[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<[>>>+<<<-]>>[-]]<<]>>>[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<+>>[-]]<<<<<<<]>>>>>[++++++++++++++++++++++++++++++++++++++++++++++++.[-]]++++++++++<[->-<]>++++++++++++++++++++++++++++++++++++++++++++++++.[-]<<<<<<<<<<<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<-[>>.>.<<<[-]]<<[>>+>+<<<-]>>>[<<<+>>>-]<<[<+>-]>[<+>-]<<<-]', chr(10)))