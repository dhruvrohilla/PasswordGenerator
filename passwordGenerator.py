import random as rn

length = 12
charAZ = [chr(x) for x in range(65,91)]
charaz = [chr(x) for x in range(97,123)]
chardec = [chr(x) for x in range(48,58)]
charspc = ['/','_','.','@','&','#']

combinedchar = charAZ+charaz+chardec+charspc
temp_pass = ''
for x in range(length):
    temp_pass = temp_pass + rn.choice(combinedchar)


print(temp_pass)
