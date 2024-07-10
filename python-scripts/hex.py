import binascii

hex_string = "4d617276656c2047756c616e65"
original_string = binascii.unhexlify(hex_string).decode()
print(original_string)

name = "Joe Din"
hex_representation = binascii.hexlify(name.encode())
print("0x" + hex_representation.decode())
