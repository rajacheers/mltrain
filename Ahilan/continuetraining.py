x = [11, 22, 33, 44, 55]
print ("the number which is not a multiple of 11 is shown")
for n in range(1, 100):
    if n in x:
        continue
    print (n)
