# Assembler
This is an assembler for a processor designed according to the specifications below. Instruction set architecture for this processor
is shown below.

|                  | [15:12] opcode | [11:8] | [7:4] |   [3:0]  |
|------------------|--------|-------|-------|------|
| OR               | 0000   | DST   | SRC1  | SRC2 |
| ORI              | 0001   | DST   | SRC1  | IMM  |
| AND              | 0010   | DST   | SRC1  | SRC2 |
| ANDI             | 0011   | DST   | SRC1  | IMM  |
| ADD              | 0100   | DST   | SRC1  | SRC2 |
| ADDI             | 0101   | DST   | SRC1  | IMM  |
| JUMP             | 0110   | ADDR  |       |      |
| LD               | 0111   | DST   | ADDR  |      |
| ST               | 1000   | SRC   | ADDR  |      |
| PUSH             | 1001   | SRC1  |       |      |
| POP              | 1010   | SRC1  |       |      |

The immediate values for ORI, ANDI, and ADDI, and the address value for JUMP can be negative.
This assembler creates two output files. One of them will be used as input of logisim design 
and the other one will be used as the input of verilog design.
