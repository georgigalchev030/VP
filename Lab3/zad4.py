start = int(input("Start num: "))
end = int(input("End num: "))
for i in range(start, end):
    counter = 0
    for x in range(i):
        if i % (x+1) == 0:
            counter+=1
    if counter==2:
        print(i)