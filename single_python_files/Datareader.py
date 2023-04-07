FD = []
total = int (0)
with  open("single_python_files\\data\\1_1_in.txt") as file: #opens the file but only while its accessed by the chunk in with
    for line in file: #adds the line to the list for all lines in the file
        FD.append(line)

FD.sort() #sorts the list
    
for i in FD: #prints the whole list, since it was sorted it prints it out ascending 
    print(i)




        
