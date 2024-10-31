#Python progress to print a star pattern based on the nunber of rows  specified by the user
#Got the number of rows from user
n=int(input("Enter the number of rows:   "))
#outer loop for ech row
for i in range(1, n+1):
    # Inner loop for each column in the row
    for z in range(i):
        #print star and with space instead of new line
        print('*',end=' ')
        #After each row,print a new line
    print()
