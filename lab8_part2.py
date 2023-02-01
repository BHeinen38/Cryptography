#this is the look up table  for sub byte
def SubByte(string):
    res = ""
    for i in range(len(string)):
        if(string[i] == "0"):
            res += "a"
        if(string[i] == "1"):
            res += "4"
        if(string[i] == "2"):
            res += "3"
        if(string[i] == "3"):
            res += "b"
        if(string[i] == "4"):
            res += "8"
        if(string[i] == "5"):
            res += "e"
        if(string[i] == "6"):
            res += "2"
        if(string[i] == "7"):
            res += "c"
        if(string[i] == "8"):
            res += "5"
        if(string[i] == "9"):
            res += "7"
        if(string[i] == "a"):
            res += "6"
        if(string[i] == "b"):
            res += "f"
        if(string[i] == "c"):
            res += "0"
        if(string[i] == "d"):
            res += "1"
        if(string[i] == "e"):
            res += "9"
        if(string[i] == "f"):
            res += "d"
        if(res == ""):
            return "Failed"
        
    return res

#we need to pass these in as binary
def XOR(text, key):
    res = ""
    for i in range(16):
       if(text[i] == key[i]): res += "0" #if they are equal it is 0
       
       if(text[i] != key[i]): res += "1" #if they are not equal it is 1

    return res

#this is the mixer matrix
def MixerMatrix():
    return [[1,0,1,0,0,0,1,1], [1,1,0,1,0,0,0,1], [1,1,1,0,1,0,0,0],
    [0,1,0,1,0,1,1,1], [0,0,1,1,1,0,1,0], [0,0,0,1,1,1,0,1], [1,0,0,0,1,1,1,0],
    [0,1,1,1,0,1,0,1]]

#this is my calculation of the mixer matrix  
def CalculateMixerMatrix(shiftRow, mixer):
    results = ""
    h0 = str(bin(int(shiftRow[0], 16))[2::].zfill(4))
    h1 = str(bin(int(shiftRow[1], 16))[2::].zfill(4))
    h2 = str(bin(int(shiftRow[2], 16))[2::].zfill(4))
    h3 = str(bin(int(shiftRow[3], 16))[2::].zfill(4))
    
    h00 = ((int(h0[0]) * mixer[0][0]) + (int(h0[1]) * mixer[0][1]) + (int(h0[2]) * mixer[0][2]) + (int(h0[3]) * mixer[0][3])
    + (int(h1[0]) * mixer[0][4]) + (int(h1[1]) * mixer[0][5]) + (int(h1[2]) * mixer[0][6]) + (int(h1[3]) * mixer[0][7])) % 2

    h01 = ((int(h0[0]) * mixer[1][0]) + (int(h0[1]) * mixer[1][1]) + (int(h0[2]) * mixer[1][2]) + (int(h0[3]) * mixer[1][3])
    + (int(h1[0]) * mixer[1][4]) + (int(h1[1]) * mixer[1][5]) + (int(h1[2]) * mixer[1][6]) + (int(h1[3]) * mixer[1][7])) % 2

    h02 = ((int(h0[0]) * mixer[2][0]) + (int(h0[1]) * mixer[2][1]) + (int(h0[2]) * mixer[2][2]) + (int(h0[3]) * mixer[2][3])
    + (int(h1[0]) * mixer[2][4]) + (int(h1[1]) * mixer[2][5]) + (int(h1[2]) * mixer[2][6]) + (int(h1[3]) * mixer[2][7])) % 2

    h03 = ((int(h0[0]) * mixer[3][0]) + (int(h0[1]) * mixer[3][1]) + (int(h0[2]) * mixer[3][2]) + (int(h0[3]) * mixer[3][3])
    + (int(h1[0]) * mixer[3][4]) + (int(h1[1]) * mixer[3][5]) + (int(h1[2]) * mixer[3][6]) + (int(h1[3]) * mixer[3][7])) % 2

    h10 = ((int(h0[0]) * mixer[4][0]) + (int(h0[1]) * mixer[4][1]) + (int(h0[2]) * mixer[4][2]) + (int(h0[3]) * mixer[4][3])
    + (int(h1[0]) * mixer[4][4]) + (int(h1[1]) * mixer[4][5]) + (int(h1[2]) * mixer[4][6]) + (int(h1[3]) * mixer[4][7])) % 2

    h11 = ((int(h0[0]) * mixer[5][0]) + (int(h0[1]) * mixer[5][1]) + (int(h0[2]) * mixer[5][2]) + (int(h0[3]) * mixer[5][3])
    + (int(h1[0]) * mixer[5][4]) + (int(h1[1]) * mixer[5][5]) + (int(h1[2]) * mixer[5][6]) + (int(h1[3]) * mixer[5][7])) % 2

    h12 = ((int(h0[0]) * mixer[6][0]) + (int(h0[1]) * mixer[6][1]) + (int(h0[2]) * mixer[6][2]) + (int(h0[3]) * mixer[6][3])
    + (int(h1[0]) * mixer[6][4]) + (int(h1[1]) * mixer[6][5]) + (int(h1[2]) * mixer[6][6]) + (int(h1[3]) * mixer[6][7])) % 2

    h13 = ((int(h0[0]) * mixer[7][0]) + (int(h0[1]) * mixer[7][1]) + (int(h0[2]) * mixer[7][2]) + (int(h0[3]) * mixer[7][3])
    + (int(h1[0]) * mixer[7][4]) + (int(h1[1]) * mixer[7][5]) + (int(h1[2]) * mixer[7][6]) + (int(h1[3]) * mixer[7][7])) % 2

    h20 = ((int(h2[0]) * mixer[0][0]) + (int(h2[1]) * mixer[0][1]) + (int(h2[2]) * mixer[0][2]) + (int(h2[3]) * mixer[0][3])
    + (int(h3[0]) * mixer[0][4]) + (int(h3[1]) * mixer[0][5]) + (int(h3[2]) * mixer[0][6]) + (int(h3[3]) * mixer[0][7])) % 2

    h21 = ((int(h2[0]) * mixer[1][0]) + (int(h2[1]) * mixer[1][1]) + (int(h2[2]) * mixer[1][2]) + (int(h2[3]) * mixer[1][3])
    + (int(h3[0]) * mixer[1][4]) + (int(h3[1]) * mixer[1][5]) + (int(h3[2]) * mixer[1][6]) + (int(h3[3]) * mixer[1][7])) % 2

    h22 = ((int(h2[0]) * mixer[2][0]) + (int(h2[1]) * mixer[2][1]) + (int(h2[2]) * mixer[2][2]) + (int(h2[3]) * mixer[2][3])
    + (int(h3[0]) * mixer[2][4]) + (int(h3[1]) * mixer[2][5]) + (int(h3[2]) * mixer[2][6]) + (int(h3[3]) * mixer[2][7])) % 2

    h23 = ((int(h2[0]) * mixer[3][0]) + (int(h2[1]) * mixer[3][1]) + (int(h2[2]) * mixer[3][2]) + (int(h2[3]) * mixer[3][3])
    + (int(h3[0]) * mixer[3][4]) + (int(h3[1]) * mixer[3][5]) + (int(h3[2]) * mixer[3][6]) + (int(h3[3]) * mixer[3][7])) % 2

    h30 = ((int(h2[0]) * mixer[4][0]) + (int(h2[1]) * mixer[4][1]) + (int(h2[2]) * mixer[4][2]) + (int(h2[3]) * mixer[4][3])
    + (int(h3[0]) * mixer[4][4]) + (int(h3[1]) * mixer[4][5]) + (int(h3[2]) * mixer[4][6]) + (int(h3[3]) * mixer[4][7])) % 2

    h31 = ((int(h2[0]) * mixer[5][0]) + (int(h2[1]) * mixer[5][1]) + (int(h2[2]) * mixer[5][2]) + (int(h2[3]) * mixer[5][3])
    + (int(h3[0]) * mixer[5][4]) + (int(h3[1]) * mixer[5][5]) + (int(h3[2]) * mixer[5][6]) + (int(h3[3]) * mixer[5][7])) % 2

    h32 = ((int(h2[0]) * mixer[6][0]) + (int(h2[1]) * mixer[6][1]) + (int(h2[2]) * mixer[6][2]) + (int(h2[3]) * mixer[6][3])
    + (int(h3[0]) * mixer[6][4]) + (int(h3[1]) * mixer[6][5]) + (int(h3[2]) * mixer[6][6]) + (int(h3[3]) * mixer[6][7])) % 2

    h33 = ((int(h2[0]) * mixer[7][0]) + (int(h2[1]) * mixer[7][1]) + (int(h2[2]) * mixer[7][2]) + (int(h2[3]) * mixer[7][3])
    + (int(h3[0]) * mixer[7][4]) + (int(h3[1]) * mixer[7][5]) + (int(h3[2]) * mixer[7][6]) + (int(h3[3]) * mixer[7][7])) % 2

    results = str(h00)+str(h01)+str(h02)+str(h03)+str(h10)+str(h11)+str(h12)+str(h13)+str(h20)+str(h21)+str(h22)+str(h23)+str(h30)+str(h31)+str(h32)+str(h33)
    return results


#driver code   
def main():
    print("Please Enter a 4 digit hex value that you wish to encrypt: ")
    print("Example: 2ca5")
    plainHex = input()
    h0 = plainHex[0]
    h1 = plainHex[1]
    h2 = plainHex[2]
    h3 = plainHex[3]

    print("Please enter the key that you wish to encrypt with")
    print("Example: 6b5d")
    key = input()
    k0 = key[0]
    k1 = key[1]
    k2 = key[2]
    k3 = key[3]
    
    #printing the first rd of matrixes
    plainMatrixRd1 = [[h0, h2], [h1, h3]]
    keyMatrixRd1 = [[k0, k2], [k1, k3]]
    print()
    print("Input: Plain text matrix")
    print(plainMatrixRd1)
    print()
    print("Input: Key matrix")
    print(keyMatrixRd1)

    #print("Getting binary values")

    binTextVal = bin(int(plainHex, 16))[2::].zfill(16)
    binKeyVal = bin(int(key, 16))[2::].zfill(16)

    firstXOR = XOR(binTextVal, binKeyVal)

    #print(firstXOR)

    x1 = hex(int(firstXOR[0:4], 2))[2::]
    x2 = hex(int(firstXOR[4:8], 2))[2::]
    x3  = hex(int(firstXOR[8:12], 2))[2::]
    x4 = hex(int(firstXOR[12:16], 2))[2::]

    firstRd1_1 = [[x1, x3], [x2, x4]]
    print()
    print("Round Numeber 1: ")
    print(firstRd1_1)


    rd1SubByte = SubByte(x1+x2+x3+x4)
    rd1SubBytMatrix = [[rd1SubByte[0], rd1SubByte[2]], [rd1SubByte[1], rd1SubByte[3]]]
    print()
    print("Sub Bytes Round 1: ")
    print(rd1SubBytMatrix)

    print()
    print("Shift row Round 1: ")
    rd1ShiftMatrix = [[rd1SubByte[0], rd1SubByte[2]], [rd1SubByte[3], rd1SubByte[1]]]
    rd1ShiftString = rd1SubByte[0] +  rd1SubByte[3]+ rd1SubByte[2]+ rd1SubByte[1]
    print(rd1ShiftMatrix)

    mixerMatrix = MixerMatrix()

    mixer1String = CalculateMixerMatrix(rd1ShiftString, mixerMatrix)
    print(mixer1String)

    m1 = hex(int(mixer1String[0:4], 2))[2::]
    m2 = hex(int(mixer1String[4:8], 2))[2::]
    m3  = hex(int(mixer1String[8:12], 2))[2::]
    m4 = hex(int(mixer1String[12:16], 2))[2::]

    print()
    print("Mixer Matrix Round 1: ")
    rd1MixerMatrix = [[m1, m3], [m2, m4]]
    print(rd1MixerMatrix)
    mixer = str(m1)+str(m2)+str(m3)+str(m4)
    key2 = "6538"

    binMixer = bin(int(mixer, 16))[2::].zfill(16)
    binKey2 = bin(int(key2, 16))[2::].zfill(16)

    secondXOR = XOR(binMixer, binKey2)
    
    x1 = hex(int(secondXOR[0:4], 2))[2::]
    x2 = hex(int(secondXOR[4:8], 2))[2::]
    x3  = hex(int(secondXOR[8:12], 2))[2::]
    x4 = hex(int(secondXOR[12:16], 2))[2::]

    print()
    secondRd = [[x1, x3], [x2, x4]]
    print("Second Round Start")
    print(secondRd)

    print()
    rd2SubByte = SubByte(x1+x2+x3+x4)
    rd2SubBytMatrix = [[rd2SubByte[0], rd2SubByte[2]], [rd2SubByte[1], rd2SubByte[3]]]
    print("Sub Bytes Round 2: ")
    print(rd2SubBytMatrix)

    print()
    print("Shift row Round 2: ")
    rd2ShiftMatrix = [[rd2SubByte[0], rd2SubByte[2]], [rd2SubByte[3], rd2SubByte[1]]]
    rd2ShiftString = rd2SubByte[0] +  rd2SubByte[3]+ rd2SubByte[2]+ rd2SubByte[1]
    print(rd2ShiftMatrix)

    mixer2String = CalculateMixerMatrix(rd2ShiftString, mixerMatrix)
    print(mixer2String)

    m1 = hex(int(mixer2String[0:4], 2))[2::]
    m2 = hex(int(mixer2String[4:8], 2))[2::]
    m3  = hex(int(mixer2String[8:12], 2))[2::]
    m4 = hex(int(mixer2String[12:16], 2))[2::]

    print()
    print("Mixer Matrix Round 2: ")
    rd2MixerMatrix = [[m1, m3], [m2, m4]]
    print(rd2MixerMatrix)
    mixer2 = str(m1)+str(m2)+str(m3)+str(m4)
    key3 = "1e26"

    binMixer = bin(int(mixer2, 16))[2::].zfill(16)
    binKey3 = bin(int(key3, 16))[2::].zfill(16)

    thirdXOR = XOR(binMixer, binKey3)

    x1 = hex(int(thirdXOR[0:4], 2))[2::]
    x2 = hex(int(thirdXOR[4:8], 2))[2::]
    x3  = hex(int(thirdXOR[8:12], 2))[2::]
    x4 = hex(int(thirdXOR[12:16], 2))[2::]

    thirdRd = [[x1, x3], [x2, x4]]
    print()
    print("Third Round Start")
    print(thirdRd)

    print()
    rd3SubByte = SubByte(x1+x2+x3+x4)
    rd3SubBytMatrix = [[rd3SubByte[0], rd3SubByte[2]], [rd3SubByte[1], rd3SubByte[3]]]
    print("Sub Bytes Round 3: ")
    print(rd3SubBytMatrix)

    print()
    print("Shift row Round 3: ")
    rd3ShiftMatrix = [[rd3SubByte[0], rd3SubByte[2]], [rd3SubByte[3], rd3SubByte[1]]]
    rd3ShiftString = rd3SubByte[0] +  rd3SubByte[3]+ rd3SubByte[2]+ rd3SubByte[1]
    print(rd3ShiftMatrix)

    mixer3String = CalculateMixerMatrix(rd3ShiftString, mixerMatrix)
    print(mixer3String)

    m1 = hex(int(mixer3String[0:4], 2))[2::]
    m2 = hex(int(mixer3String[4:8], 2))[2::]
    m3  = hex(int(mixer3String[8:12], 2))[2::]
    m4 = hex(int(mixer3String[12:16], 2))[2::]

    print()
    print("Mixer Matrix Round 3: ")
    rd3MixerMatrix = [[m1, m3], [m2, m4]]
    print(rd3MixerMatrix)
    mixer3 = str(m1)+str(m2)+str(m3)+str(m4)
    key4 = "7d5b"

    binMixer = bin(int(mixer3, 16))[2::].zfill(16)
    binKey3 = bin(int(key4, 16))[2::].zfill(16)

    fourthXOR = XOR(binMixer, binKey3)

    x1 = hex(int(fourthXOR[0:4], 2))[2::]
    x2 = hex(int(fourthXOR[4:8], 2))[2::]
    x3  = hex(int(fourthXOR[8:12], 2))[2::]
    x4 = hex(int(fourthXOR[12:16], 2))[2::]

    fourthRd = [[x1, x3], [x2, x4]]
    print()
    print("fourth Round Start")
    print(fourthRd)

    print()
    rd4SubByte = SubByte(x1+x2+x3+x4)
    rd4SubBytMatrix = [[rd4SubByte[0], rd4SubByte[2]], [rd4SubByte[1], rd4SubByte[3]]]
    print("Sub Bytes Round 4: ")
    print(rd4SubBytMatrix)

    print()
    print("Shift row Round 4: ")
    rd4ShiftMatrix = [[rd4SubByte[0], rd4SubByte[2]], [rd4SubByte[3], rd4SubByte[1]]]
    rd4ShiftString = rd4SubByte[0] +  rd4SubByte[3]+ rd4SubByte[2]+ rd4SubByte[1]
    print(rd4ShiftMatrix)
    
    key5 = "0358"

    binMixer = bin(int(rd4ShiftString, 16))[2::].zfill(16)
    binKey4 = bin(int(key5, 16))[2::].zfill(16)

    fifthXOR = XOR(binMixer, binKey4)

    x1 = hex(int(fifthXOR[0:4], 2))[2::]
    x2 = hex(int(fifthXOR[4:8], 2))[2::]
    x3  = hex(int(fifthXOR[8:12], 2))[2::]
    x4 = hex(int(fifthXOR[12:16], 2))[2::]

    fifthRd = [[x1, x3], [x2, x4]]
    print()
    print("Final Round Matrix")
    print(fifthRd)
    print("Regular String")
    print(str(x1)+str(x2)+str(x3)+str(x4))


if __name__ == '__main__':
    main()