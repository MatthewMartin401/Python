# Binary Main

from AsciiCode_to_string import asciiVal_to_letter;
from Binary_to_val import list_binary_to_octal;
from Hexadecimal_val import hex_to_deci;
import os


val = "48656c6c6f"

print(hex_to_deci(val))
print(len(hex_to_deci(val)) / 8)
print(list_binary_to_octal(hex_to_deci(val)))
print(asciiVal_to_letter(list_binary_to_octal(hex_to_deci(val))))

# os.system('cls')
print(bin(ord("A")))
print(hex(ord("A")))
print(oct(ord("A")))

print("====")
val2 = "Hello"
print("".join(([str((bin(ord(x)))[2:]) for x in val2])))
hex_val = "".join(([str((hex(ord(x)))[2:]) for x in val2]))
print(hex_val)
print(hex_val == val)

# print(chr(97))
# print(ord("a"))
# print(bin(255))
# print(ascii(255))
# print(oct(255))
# print(hex(255))