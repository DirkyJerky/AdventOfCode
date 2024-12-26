from pathlib import Path
import numpy as np
import networkx as nx
import re
import time

def parse():
    with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
        input = input_file.readlines()

    reg_A = int(re.match(r'Register A: (\d+)', input[0]).group(1))
    reg_B = int(re.match(r'Register B: (\d+)', input[1]).group(1))
    reg_C = int(re.match(r'Register C: (\d+)', input[2]).group(1))

    program = re.match(r'Program: (.+)', input[4]).group(1)

    return (reg_A, reg_B, reg_C, program)

(reg_A, reg_B, reg_C, program) = parse()

class Computer:
    def __init__(self, A: int, B: int, C: int, memory: list[int]):
        self.A = A
        self.B = B
        self.C = C
        self.memory = memory
        self.output = []
        self.instr = 0

    def operand_literal(self, v: int) -> int:
        return v

    def operand_combo(self, v: int) -> int:
        if v <= 3:
            return v
        elif v == 4:
            return self.A
        elif v == 5:
            return self.B
        elif v == 6:
            return self.C
        else:
            raise Exception()

    def op_adv(self, oper: int):
        self.A = self.A >> self.operand_combo(oper)

    def op_bxl(self, oper: int):
        self.B ^= self.operand_literal(oper)

    def op_bst(self, oper: int):
        self.B = self.operand_combo(oper) % 8

    def op_jnz(self, oper: int):
        if self.A:
            self.instr = self.operand_literal(oper)
            return True

    def op_bxc(self, oper: int):
        self.B ^= self.C

    def op_out(self, oper: int):
        self.output.append(self.operand_combo(oper) % 8)

    def op_bdv(self, oper: int):
        self.B = self.A >> self.operand_combo(oper)

    def op_cdv(self, oper: int):
        self.C = self.A >> self.operand_combo(oper)

    def step(self):
        if (self.instr + 1 >= len(self.memory)):
            return 'STOP'

        instr_table = [
            self.op_adv,
            self.op_bxl,
            self.op_bst,
            self.op_jnz,
            self.op_bxc,
            self.op_out,
            self.op_bdv,
            self.op_cdv
        ]

        op = self.memory[self.instr]
        operand = self.memory[self.instr + 1]

        ret = instr_table[op](operand)

        if op == 3 and ret:
            pass
        else:
            self.instr += 2

        if op == 5:
            return 'OUTPUT'

        return 'CONTINUE'

    def __str__(self):
        return f'Computer(reg[{self.A}, {self.B}, {self.C}], instr={self.instr}, memory={self.memory}, output={self.output})'

    def run(self, debug: bool = False):
        if (debug):
            print(self)
        while self.step() != 'STOP':
            if (debug):
                print(self)
            # time.sleep(1)
            pass

        return self.output

    def run_b(self, debug: bool = False) -> bool:
        if (debug):
            print('start', self)
        while True:
            res = self.step()

            if res == 'CONTINUE':
                if (debug):
                    print('continue', self)
                continue

            if res == 'OUTPUT':
                if (debug):
                    print('output', self)
                for i in range(min(len(self.output), len(self.memory))):
                    if self.output[i] != self.memory[i]:
                        return False

            if res == 'STOP':
                if (debug):
                    print('stop', self)
                if len(self.output) != len(self.memory):
                    return False

                for i in range(len(self.output)):
                    if self.output[i] != self.memory[i]:
                        return False

                return True


memory = list(map(int, program.split(',')))

print('17a', ",".join(map(str, Computer(reg_A, reg_B, reg_C, memory).run())))

# for i in range(8):
#     if Computer(i, reg_B, reg_C, memory).run_b(True):
#         print('17b', i)
#         break

A = 0

for _ in range(len(memory)):
    for app in range(8):
        A_alt = (A << 3) + app

        out = Computer(A_alt, 0, 0, memory).run()
        # print(out)

        found_val = False

        min_len = min(len(out), len(memory))

        if out[::-1][0:min_len] == memory[::-1][0:min_len]:
            A = A_alt
            # print(A, out, memory)
            break

print('17b', A)
