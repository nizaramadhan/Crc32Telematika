from array import array

poly = 0xEDB88320

table = array('L')
for byte in range(256):
    crc = 0
    for bit in range(8):
        if (byte ^ crc) & 1:
            crc = (crc >> 1) ^ poly
        else:
            crc >>= 1
        byte >>= 1
    table.append(crc)

def enkrip(string):
    bil = 0xffffffff

    for ch in string:
        bil = table[((ch) ^ bil) & 0x000000ff] ^ (bil >> 8)

    return bil

print("Program Menghitung CRC32")
print("------------------------") 
P = input("Input Hex :").encode("utf-8")

print ("Result :        0x%08x" % (enkrip(P)))
wait = input('Enter Untuk lanjut')
