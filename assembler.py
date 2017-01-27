instruct = []   # keeps the splitted version of the instructions
filename = input("Enter the filename: ") # gets the filename as the input
print("Reading...")
with open(filename) as f:   # goes through the file line by line, and splits each line from the spaces, and adds them into instruct list
    for line in f:
        instruct.append(line.split(" "))
f.close()

# goes through the instruct list, and separates the registers and immediate values from commas, and updates instruct list
for x in range(len(instruct)):
    instruct[x][1] = instruct[x][1].split(",")

# goes through the instruct list, and separates R letter, and its number which indicates the number of the register
for x in range(len(instruct)):
    for t in range(len(instruct[x][1])):
        instruct[x][1][t] = instruct[x][1][t].split("R")

# keeps the binary values of the instructions
binary = []

# finds the instructions' opcodes, and adds them to binary list
for i in range(len(instruct)):
    if instruct[i][0] == "AND":
        binary.append("0010")
    elif instruct[i][0] == "OR":
        binary.append("0000")
    elif instruct[i][0] == "ADD":
        binary.append("0100")
    elif instruct[i][0] == "LD":
        binary.append("0111")
    elif instruct[i][0] == "ST":
        binary.append("1000")
    elif instruct[i][0] == "ANDI":
        binary.append("0011")
    elif instruct[i][0] == "ORI":
        binary.append("0001")
    elif instruct[i][0] == "ADDI":
        binary.append("0101")
    elif instruct[i][0] == "JUMP":
        binary.append("0110")
    elif instruct[i][0] == "PUSH":
        binary.append("1001")
    elif instruct[i][0] == "POP":
        binary.append("1010")

# temporary list to be used when transforming binOfNum into string
p = []

# converts the immediate values, and the register numbers into binary code, and saves it into first binOfNum, then binary lists
#goes through the instruct list
for i in range(len(instruct)):
    t=0;
    for j in range(len(instruct[i][1])):
        # if the instruction has 3 arguments, then enters here, and sets the values of binOfNum and index
        if (len(instruct[i][1]))==3 or (len(instruct[i][1])==2 and instruct[i][1][0][0] == "") and t!=1:
            binOfNum = [0, 0, 0, 0]
            index = 3
            t=1;
        # if the instruction has 2 arguments, then enters here, and sets the values of binOfNum and index
        elif len(instruct[i][1]) == 2:
            binOfNum = [0, 0, 0, 0, 0, 0, 0, 0]
            index = 7
        # if the instructions has 1 arguments, then enters here
        elif len(instruct[i][1]) == 1:
            binOfNum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            index = 11
        # if the number represents the register number, then enters here
        if instruct[i][1][j][0] == "":
            # converts the string value in the instruct list into integer
            temp = int(instruct[i][1][j][1])
            # finds the corresponding binary code for the temp number
            while temp!=0 and index>=0:
                binOfNum[index] = temp%2
                temp = int(temp/2)
                index -= 1

            # converts the binOfNum values into string, and passes it into p list, then adds it to the related binary list elements
            p = ''.join(str(e) for e in binOfNum)
            binary[i] = binary[i] + "" + p
        # if it is an immediate value, then enters here
        elif instruct[i][1][j][0] != "":
            # converts the value into integer
            temp = int(instruct[i][1][j][0])
            # if the immediate value is larger than zero, enters here
            if temp > 0:
                # converts temp into binary code
                while temp != 0 and index>=0:
                    binOfNum[index] = temp%2
                    temp = int(temp/2)
                    index -= 1
            # if the immdiate value is smaller than zero, enters here
            elif temp < 0:
                # finds its positive value
                temp2 = temp*-1
                # gets the binary code of the positive version of temp
                while temp2!=0 and index >=0:
                    binOfNum[index] = temp2%2
                    temp2 = int(temp2/2)
                    index -=1

                # two's complement process starts
                # inverts the binary code of the immediate value
                for t in range(len(binOfNum)):
                    if binOfNum[t] == 0:
                        binOfNum[t] = 1
                    elif binOfNum[t] == 1:
                        binOfNum[t] = 0
                # part where 1 is added
                # if the last bit is zero, it changes it into 1
                if binOfNum[len(binOfNum)-1] == 0:
                    binOfNum[len(binOfNum)-1] = 1
                # if it's not zero, then enters here
                else:
                    # finds the iterator value
                    ite = len(binOfNum)-1
                    # goes until it finds an element with the value of zero
                    while ite>=0 and binOfNum[ite]!=0:
                        binOfNum[ite] = 0
                        ite -= 1
                    # when it finishes its job with the loop, changes the value of current binOfNum's value
                    binOfNum[ite] = 1
            # adds it into the corresponding element of the binary list
            p = ''.join(str(e) for e in binOfNum)
            binary[i] = binary[i] + "" + p

# in this part binary values are transformed into hexadecimal values
sum = 0 # keeps the sum of 4 bits to find its hexadecimal value
hexa =[] # keeps the corresponding hexadecimal values of binary code
sumStr = "" # if the hexadecimal value is a letter, then sumStr is used

# goes through the binary list
for i in range(len(binary)):
    hexa.append("")
    # evaluates the values according to their bits
    for j in range(len(binary[i])):
        # if the current element corresponds to the leftmost bit of a 4 bit group,
        # then it multiplies that bit value with 8, and adds it to sum
        if j%4 == 0 :
            sum=0
            sum = sum + int(binary[i][j])*8
        # if the current element corresponds to the second bit from the left of a 4 bit group,
        # then it multiplies that bit value with 4, and adds it to sum
        elif j%4 == 1 :
            sum = sum + int(binary[i][j])*4
        # if the current element corresponds to the third bit from the left of a 4 bit group,
        # then it multiplies that bit with 2, and adds it to sum
        elif j%4 == 2 :
            sum = sum + int(binary[i][j])*2
        # if the current element is the last bit of a 4 bit group,
        # then it multiplies the value of that bit with 1, and adds it to sum
        elif j%4 == 3 :
            sum = sum + int(binary[i][j])*1

        # after we used the last bit of a 4 bit group, it enters here to calculate its hexadecimal equivalent
        if j%4 == 3 and j!= 0 :
            # enters here if the sum value is less than 10, and it is added to as a number
            if(sum < 10):
                hexa[i] = hexa[i] + "" +str(sum)
            # if sum is larger than 10, enters here to get its equivalent letter, and adds it as a string
            else:
                if sum==10:
                    sumStr="A"
                elif sum==11:
                    sumStr="B"
                elif sum==12:
                    sumStr="C"
                elif sum==13:
                    sumStr="D"
                elif sum==14:
                    sumStr="E"
                elif sum==15:
                    sumStr="F"
                hexa[i] = hexa[i] + sumStr
    print(hexa[i])
print("Writing...")
# creates the file for logisim, and writes hexadecimal values into it
dest = open("logisim_instructions","w")

dest.write("v2.0 raw")
dest.write("\n")
for i in range(len(hexa)):
    dest.write(hexa[i])
    dest.write(" ")
dest.close()

# creates the file for verilog, and writes hexadecimal values into it
dest2 = open("verilog_instructions.hex","w")

for i in range(len(hexa)):
    dest2.write(hexa[i])
    dest2.write(" ")
dest2.close()
