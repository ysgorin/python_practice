from os import strerror

try:
    bf = open('file.bin', 'rb')
    # Method 1
    # data = bytearray(10)
    # Note use of method for reading bytes
    # bf.readinto(data)

    # Method 2
    data = bytearray(bf.read())

    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))