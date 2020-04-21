#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

# Program file from parsing CLI
# argv_program_counter = 1  # for all file implementation
program = sys.argv[1]

cpu.load(program)
cpu.run()