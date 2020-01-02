def brain_luck(code, input):
    input_array = list(input)

    data_pointer = 0
    memory = [0] * 30_000
    input_pointer = 0
    output = ''
    start_loop = 0
    end_loop = 0
    ip = 0

    while ip < len(code):
        if code[ip] == '>':
            data_pointer += 1
        elif code[ip] == '<':
            data_pointer -= 1
        elif code[ip] == '+':
            memory[data_pointer] = (memory[data_pointer] + 1) % 256
        elif code[ip] == '-':
            memory[data_pointer] = (memory[data_pointer] - 1) % 256
        elif code[ip] == '.':
            output += (chr(memory[data_pointer]))
        elif code[ip] == ',':
            memory[data_pointer] = ord(input_array[input_pointer])
            input_pointer += 1
        elif code[ip] == '[':
            start_loop = ip
            if memory[data_pointer] == 0:
                ip = end_loop
        elif code[ip] == ']':
            end_loop = ip
            if memory[data_pointer] != 0:
                ip = start_loop
        else:
            raise Exception('Invalid instruction')
        ip += 1

    return output