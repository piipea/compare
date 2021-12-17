file1="list.txt"
file2="file2.txt"

with open(file1) as f1:
    for line1 in f1:
        found = False
        
        with open(file2) as f2:
            for line2 in f2:
                line1 = line1.rstrip("\n")
                line2 = line2.rstrip("\n")

                if line1 == line2:
                    found = True
                    
        if not found:
            print(line1 + " not in " + file2)

