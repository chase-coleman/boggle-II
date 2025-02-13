
# using shake() returns:
line1 = 'LKNE'
line2 = 'QAHH'
line3 = 'VKPC'
line4 = 'EVXE'
horizontal_lines = [line1, line2, line3, line4]

h1_reversed = line1[::-1]
h2_reversed = line2[::-1]
h3_reversed = line3[::-1]
h4_reversed = line4[::-1]

v1 = "".join(line1[0] + line2[0] + line3[0] + line4[0])
v2 = "".join(line1[1] + line2[1] + line3[1] + line4[1])
v3 = "".join(line1[2] + line2[2] + line3[2] + line4[2])
v4 = "".join(line1[3] + line2[3] + line3[3] + line4[3])
print(line1)
print(line1[::-1])
print(v1)
print(v1[::-1])

if 'LKNE' in horizontal_lines:
    print('yes')
