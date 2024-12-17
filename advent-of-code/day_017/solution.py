import re

def extract_integers(text):
    """
    Extract all integers (including negative) from a given text string.
    
    Args:
        text (str): Input text to extract integers from.
    
    Returns:
        list: List of integers found in the text.
    """
    return [int(x) for x in re.findall(r"-?\d+", text)]


def read_input_file(file_path):
    """
    Read and parse the input file containing register values and program instructions.
    
    Args:
        file_path (str): Path to the input file.
    
    Returns:
        tuple: A tuple containing (register_values, program_instructions)
    """
    with open(file_path, "r") as file:
        raw_text = file.read().strip()
    
    # Split input into register values and program instructions
    raw_registers, raw_program = raw_text.split("\n\n")
    register_values = extract_integers(raw_registers)
    
    # Extract program instructions
    program_instructions = [int(x) for x in raw_program.split(":")[1].strip().split(",")]
    
    return register_values, program_instructions


def resolve_operand(registers, operand):
    """
    Resolve the value of the operand based on its type.
    
    Args:
        registers (list): List of register values [A, B, C].
        operand (int): Operand value.
    
    Returns:
        int: The resolved value of the operand.
    """
    if operand < 4:
        return operand
    if operand == 4:
        return registers[0]
    if operand == 5:
        return registers[1]
    if operand == 6:
        return registers[2]
    return None


def execute_instruction(registers, instruction_pointer, program):
    """
    Execute a single instruction in the program.
    
    Args:
        registers (list): List of register values [A, B, C].
        instruction_pointer (int): Current position in the program.
        program (list): List of program instructions.
    
    Returns:
        tuple: Updated register values and instruction pointer.
    """
    opcode = program[instruction_pointer]
    operand = program[instruction_pointer + 1]
    operand_value = resolve_operand(registers, operand)
    
    if opcode == 0:
        registers[0] //= pow(2, operand_value)
    elif opcode == 1:
        registers[1] ^= operand
    elif opcode == 2:
        registers[1] = operand_value % 8
    elif opcode == 3:
        if registers[0] != 0:
            instruction_pointer = operand
            return None, registers, instruction_pointer
    elif opcode == 4:
        registers[1] ^= registers[2]
    elif opcode == 5:
        return operand_value % 8, registers, instruction_pointer + 2
    elif opcode == 6:
        registers[1] = registers[0] // pow(2, operand_value)
    elif opcode == 7:
        registers[2] = registers[0] // pow(2, operand_value)
    
    return None, registers, instruction_pointer + 2


def run_program(registers, program):
    """
    Execute the entire program and collect output values.
    
    Args:
        registers (list): Initial register values [A, B, C].
        program (list): List of program instructions.
    
    Returns:
        list: Collected output values during program execution.
    """
    instruction_pointer = 0
    output_values = []
    
    while instruction_pointer < len(program) - 1:
        output, registers, instruction_pointer = execute_instruction(registers, instruction_pointer, program)
        
        if output is not None:
            output_values.append(output)
    
    return output_values


def find_optimal_input(program, cursor, current_value):
    """
    Recursively find the best input that generates a specific program output.
    
    Args:
        program (list): List of program instructions.
        cursor (int): Current position in the program to match.
        current_value (int): Current accumulated value.
    
    Returns:
        int or None: Best input value that matches program requirements.
    """
    for candidate in range(8):
        if run_program([current_value * 8 + candidate, 0, 0], program) == program[cursor:]:
            if cursor == 0:
                return current_value * 8 + candidate
            
            result = find_optimal_input(program, cursor - 1, current_value * 8 + candidate)
            if result is not None:
                return result
    
    return None


def solve(registers, program):
    """
    Solve the problem by running the program and finding the best input.
    
    Args:
        registers (list): Initial register values [A, B, C].
        program (list): List of program instructions.
    """
    # Part 1: Print program output
    print("Part 1:", ",".join(map(str, run_program(registers, program))))
    
    # Part 2: Find best input
    best_input = find_optimal_input(program, len(program) - 1, 0)
    print("Part 2:", best_input)


if __name__ == "__main__":
    registers, program = read_input_file("input.txt")
    solve(registers, program)