'''
Bitwise Operators
~: One's Complement
&: bitwise AND
!: bitwise OR
^: bitwise XOR
<<: Left shift
>>: Right shift
'''
print( ~ 12) 
#Returns -13
#13 in binary is 00001101
#One's complement of it is 11110010
#Two's complement of it is 11110011 which is -13 in binary
#One's complement of it is 00001100 which is 12 in binary

print(12 & 13)
#Returns 12
#13 in binary is 00001101
#12 in binary is 00001100
#Do the AND operator on each number
#Result: 00001100 which is 12 in binary

print(12 | 13)
#Returns 13
#13 in binary is 00001101
#12 in binary is 00001100
#Do the OR operator on each number
#Result: 00001101 which is 13 in binary

print(12 ^ 13)
#Returns 1
#13 in binary is 00001101
#12 in binary is 00001100
#Do the XOR operator on each number
#Result: 00000001 which is 1 in binary

print(10 << 2)
#Returns 40
#10 in binary is 00001010.0000
#<< 2 means shift left by 2 digits
#Result: 00101000 which is 40 in binary

print(10 >> 2)
#Returns 2
#10 in binary is 00001010.0000
#>> 2 means shift right by 2 digits
#Result: 00000010 (Decimals will be removed) which is 2 in binary