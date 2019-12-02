def invoice(unitPrice, quantity, shipping = 10, handling = 5):
    cost = unitPrice * quantity
    total = cost + shipping + handling
    print('Cost (unitPrice x quantity) =:',cost,'\nShipping =:',shipping,'\nHandling :', handling,'\nTotal =', total)
    
def main():
    invoice(15, 3, handling = 15)
if __name__=='__main__': 
    main()
    
    
    
def printGroupMembers (groupName, *name):
    print('Members of',groupName)
    for i in name:  # no*
        print(i)
    
def main():
    groupB = ["Group B", "Sasha", "Migel", "Tanya", "Hiroto"]
    printGroupMembers("Group A", "Li", "Audry", "Jia")
    printGroupMembers(*groupB)
if __name__=='__main__':
    main()   


    
def buildBell(row):
    list1 = [[1]]                                               
    for i in range(1,row):
        temp = []
        temp.append(list1[i-1][i-1])
        for j in range(1,i+1):
            temp.append(list1[i-1][j-1] + temp[j-1])
        list1.append(temp)
    return(list1)
    
def printBell(temp):
    for i in range(len(temp)):
       for j in range(len(temp[i])):
           print(str(temp[i][j]).rjust(4), end = ' ')
       print()
        
def main():
    bell = buildBell(8)
    printBell(bell)
    
if __name__ == '__main__':
  main()

