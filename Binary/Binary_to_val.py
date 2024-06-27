binary = "0010001000100010"
#str(input("Enter binary:"))

def binary_to_octal(binary):
    val_code = {
        7 : 1,
        6 : 2,
        5 : 4,
        4 : 8,
        3 : 16,
        2 : 32,
        1 : 64,
        0 : 128}
    val = 0
    for i in range(7, -1, -1):
        #print(i, binary[i], val_code.get(i))
        if int(binary[i]) == 1:
            val += val_code.get(i)
    return val


def list_binary_to_octal(val):
    length = len(val)
    all_binary = list()
    for i in range(0, len(val), 8):
        all_binary.append(val[i:i+8])
    all_oct = list()
    for i in all_binary:
        #print(i)
        all_oct.append(binary_to_octal(i))
    return all_oct
    #for i in range(0, str().count()-1, 1):


#print(list_binary_to_octal(binary))
