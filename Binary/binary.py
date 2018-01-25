# with open("binary", "bw") as bin_file:
#     for i in range(17):
#         bin_file.write(bytes([i]))
# below is preferred
# with open("binary", "bw") as bin_file:
#     bin_file.write(bytes(range(17)))
#
# with open("binary", "br") as bin_file:
#     for b in bin_file:
#         print(b)

a = 65534 # FF FE
b = 65535 # FF FF
c = 65536 # 00 01 00 00
x = 2998302 # 02 2d c0 1e

with open("binary2", "bw") as bin_file:
    bin_file.write(a.to_bytes(2, "big"))
    bin_file.write(b.to_bytes(2, "big"))
    bin_file.write(c.to_bytes(4, "big"))
    bin_file.write(x.to_bytes(4, "big"))
    bin_file.write(x.to_bytes(4, "little"))

with open("binary2", "br") as binFile:
    e = int.from_bytes(binFile.read(2), "big")
    print(e)
    f = int.from_bytes(binFile.read(2), "big")
    print(f)
    g = int.from_bytes(binFile.read(4), "big")
    print(g)
    h = int.from_bytes(binFile.read(4), "big")
    print(h)
    i = int.from_bytes(binFile.read(4), "big") # 515910912 as opposed to 2998302 with little
    print(i)
