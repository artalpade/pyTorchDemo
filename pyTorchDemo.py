import numpy as np

G = np.array([1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1],[1,1,0,0,1],[1,1,1,0,0],[1,0,1,1,0],[1,0,0,1,1])
H = np.array([1,1,0,0,1,1,0,0,0],[1,1,1,0,0,0,1,0,0],[1,0,1,1,0,0,0,1,0],[1,0,0,1,1,0,0,0,0,1])
lD = {' ': np.array(( (0),(0),(0),(0),(0) )), 'A': np.array(( (0),(0),(0),(0),(1) )), 'B': np.array(( (0),(0),(0),(1),(0) )), 'C': np.array(( (0),(0),(0),(1),(1) )), 'D': np.array(( (0),(0),(1),(0),(0) )), 'E': np.array(( (0),(0),(1),(0),(1) )), 'F': np.array(( (0),(0),(1),(1),(0) )), 'G': np.array(( (0),(0),(1),(1),(1) )), 'H': np.array(( (0),(1),(0),(0),(0) )), 'I': np.array(( (0),(1),(0),(0),(1) )), 'J': np.array(( (0),(1),(0),(1),(0) )), 'K': np.array(( (0),(1),(0),(1),(1) )), 'L': np.array(( (0),(1),(1),(0),(0) )), 'M': np.array(( (0),(1),(1),(0),(1) )),'N': np.array(( (0),(1),(1),(1),(0) )), 'O': np.array(( (0),(1),(1),(1),(1) )), 'P': np.array(( (1),(0),(0),(0),(0) )), 'Q': np.array(( (1),(0),(0),(0),(1) )), 'R': np.array(( (1),(0),(0),(1),(0) )), 'S': np.array(( (1),(0),(0),(1),(1) )),'T': np.array(( (1),(0),(1),(0),(0) )),'U': np.array(( (1),(0),(1),(0),(1) )), 'V': np.array(( (1),(0),(1),(1),(0) )), 'W': np.array(( (1),(0),(1),(1),(1) )), 'X': np.array(( (1),(1),(0),(0),(0) )), 'Y': np.array(( (1),(1),(0),(0),(1) )), 'Z': np.array(( (1),(1),(0),(1),(0) ))}
flipDict = { 0: np.array(( (1), (1), (1),(1))), 1: np.array(( (1), (1), (0),(0))), 3: np.array(( (0), (0), (1),(1))), 4: np.array(( (1), (0), (0),(1))), 5: np.array(( (1), (0), (0),(0))), 6: np.array(( (0), (1), (0),(0))), 7: np.array(( (0), (0), (1),(0))), 8: np.array(( (0), (0), (0),(1)))}
iA = ['010010001', '000000000', '111001010', '010000101', '010110111', '001011011','010000000','011001010','010010100', '011101001', '001010111','000011101','100101100','100000000','100110101','101101001','011111000', '101101100','010011010','001001001','011011111','011001010','011001110','010010101','011101101','001111101', '000010000', '000011000','000010000', '010001010','011010000','101000001','001000000','101110101','101001101','001010111','000001111','010001101','001011111','011101101','100000000','000110101','110001111','010010001','001011110','111001010','000100001','001011110','100101101','000111100']
for key in lD:
    temp = np.mod(np.matmul(G,lD[key]),2)
    lD[key] = temp
    inputMatrices = []
    finalString = ""
    for inp in inputArray:
        temp = np.array(( (int(inp[0])),(int(inp[1])),(int(inp[2])),(int(inp[3])), (int(inp[4])), (int(inp[5])), (int(inp[6])), (int(inp[7])), (int(inp[8]))  ))
        hOutput = np.matmul(Hbig, temp)
        hOutput = np.mod(hOutput,2)
        for col in flipDict:
            if np.array_equal(flipDict[col], hOutput):
                if inp[col] == '0':
                    inp = inp [:col] +'1' + inp[col+1:]
                else:
                    inp = inp[:col] + '0' + inp[col+1:]
                temp = np.array(( (int(inp[0])),(int(inp[1])),(int(inp[2])),(int(inp[3])), (int(inp[4])), (int(inp[5])), (int(inp[6])), (int(inp[7])), (int(inp[8]))  ))

                for letter in lD:
                    if np.array_equal(lD[letter].temp):
                        finalString +=letter

        print(finalString)
