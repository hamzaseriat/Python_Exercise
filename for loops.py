creditc = "1234-5678-3521-6754"

for counter in range(0,19):
    index = counter
    if creditc[index] == '-':
      continue
    else:
     print(creditc[counter])