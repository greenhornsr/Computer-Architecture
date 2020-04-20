# Write a program in Python that runs programs.

PRINT_BEEJ = 1
HALT = 2
SAVE_REGISTER = 3 # Store a value in a register (in the LS8 called LDI)
PRINT_REGISTER = 4 # Corresponds to PRN in the LS8

# STORE INSTRUCTIONS IN LIST
memory = [
    PRINT_BEEJ,
    SAVE_REGISTER,  # Save R0,37     # Store 37 in R0    # this is the OP Code
    0, #R0      # This is the ("argument")
    37, #37     # This is the Operand
    PRINT_BEEJ,

    PRINT_REGISTER,  # PRINT_REGISTER R0
    0, #R0  

    HALT
]

register = [0] * 8 # like variables limited to R0-R7(8 total registers); aka variables at our disposal.  Is based on the computer spec.  If computer only has 8 registers, you can only make a register array with 8...

pc = 0 # PROGRAM COUNTER, the address of the current instruction
running = True

while running:
    inst = memory[pc]

    if inst == PRINT_BEEJ:
        print('Beej!')
        pc += 1

    elif inst == SAVE_REGISTER:
        reg_num = memory[pc+1]
        value = memory[pc+2]
        register[reg_num] = value
        pc+=3
    
    elif inst == PRINT_REGISTER:
        reg_num = memory[pc+1]
        value = register[reg_num]
        print(value)
        pc+=2

    elif inst == HALT:
        running = False

    else: 
        print(f"Unknown Instruction")
        running = False