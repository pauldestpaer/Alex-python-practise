FD = []
with  open("single_python_files\\data\\1_1_in.txt") as file: #opens the file but only while its accessed by the chunk in with
    for line in file: #adds the line to the list for all lines in the file
        if line.strip().isnumeric():
            FD.append(int(line.strip()))

FD.sort() #sorts the list

print(sum(FD))
    
#for i in FD: #prints the whole list, since it was sorted it prints it out ascending 
    #print(i)




        
