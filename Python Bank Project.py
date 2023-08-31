import math
import string
#Q1
class Bank:
    def __init__ (self, principal, years, rate):
        self.principal = principal
        self.years = years
        self.rate = rate

    def simple_interest(self):
        return(self.principal*self.years*(self.rate/100))

    def compound_interest(self):
        return(self.principal*pow((1+(self.rate/100)), self.years))

#Q2
def dictionary_operations():
    dict1 = {}
    dict1 = { 'Id_1': {'Name': 'XYZ', 'Contact_Number' : {'Work': '666-666-6666'}},
                'Id_2': {'Name': 'PQR', 'Contact_Number' : {'Work' : '888-888-8888', 'Home': '111-111-1111'}},
                'Id_3' : {'Name' : 'ABC', 'Contact_Number' : {'Work' : '777-777-7777', 'Cell' : '222-222-2222'}}}
    print("ID: Id_1")
    print("Name:", dict1['Id_1']['Name'])
    print("Contact_Number:")
    print("Work:", dict1['Id_1']['Contact_Number']['Work'])
    print("\n")
    print("ID: Id_2")
    print("Name:", dict1['Id_2']['Name'])
    print("Contact_Number:")
    print("Work:", dict1['Id_2']['Contact_Number']['Work'])
    print("Home:", dict1['Id_2']['Contact_Number']['Home'])
    print("\n")
    print("ID: Id_3")
    print("Name:", dict1['Id_3']['Name'])
    print("Contact_Number:")
    print("Work:", dict1['Id_3']['Contact_Number']['Work'])
    print("Home:", dict1['Id_3']['Contact_Number']['Cell'])
    print("\n")

    dict1['Id_4'] = {'Name' : 'QWE', 'Contact_Number' : {'Work' : '567-890-1234'}}
    print(dict1)
    print("\n")

    x = 0
    while(x == 0):
        n = input("Enter contact number: ")
        if(n[3] == '-' and n[7] == '-' and len(n) == 12):
            dict1['Id_2']['Contact_Number']['Work'] = n
            x=1
        else:
            print("Invalid number.")

    print(dict1)
    print("\n")

    del dict1['Id_3']['Contact_Number']
    print(dict1)

#Q3
def identical_pairs(number_list):
    count = 0
    in_list = []
    for x in range(0, len(number_list)-1):
        for y in range (x+1, len(number_list)):
            if(number_list[x] == number_list[y]):
                in_list.append((x, y))
                count=count+1

    return(count, in_list)

#Q4
def sum_of_dice_rolls():
    sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    total_rolls = 0
    for w in range(1, 7):
        for x in range(1, 7):
            for y in range(1, 7):
                for z in range(1, 7):
                    total_rolls+=1

                    if(w+x == 2 or w+y == 2 or w+z == 2 or x+y == 2 or x+z == 2 or y+z == 2):
                        sums[0]+=1
                    if(w+x == 3 or w+y == 3 or w+z == 3 or x+y == 3 or x+z == 3 or y+z == 3):
                        sums[1]+=1
                    if(w+x == 4 or w+y == 4 or w+z == 4 or x+y == 4 or x+z == 4 or y+z == 4):
                        sums[2]+=1
                    if(w+x == 5 or w+y == 5 or w+z == 5 or x+y == 5 or x+z == 5 or y+z == 5):
                        sums[3]+=1
                    if(w+x == 6 or w+y == 6 or w+z == 6 or x+y == 6 or x+z == 6 or y+z == 6):
                        sums[4]+=1
                    if(w+x == 7 or w+y == 7 or w+z == 7 or x+y == 7 or x+z == 7 or y+z == 7):
                        sums[5]+=1
                    if(w+x == 8 or w+y == 8 or w+z == 8 or x+y == 8 or x+z == 8 or y+z == 8):
                        sums[6]+=1
                    if(w+x == 9 or w+y == 9 or w+z == 9 or x+y == 9 or x+z == 9 or y+z == 9):
                        sums[7]+=1
                    if(w+x == 10 or w+y == 10 or w+z == 10 or x+y == 10 or x+z == 10 or y+z == 10):
                        sums[8]+=1
                    if(w+x == 11 or w+y == 11 or w+z == 11 or x+y == 11 or x+z == 11 or y+z == 11):
                        sums[9]+=1
                    if(w+x == 12 or w+y == 12 or w+z == 12 or x+y == 12 or x+z == 12 or y+z == 12):
                        sums[10]+=1

    max = sums[0]
    min = sums[0]
    max_sum = 0
    min_sum = 0
    for a in range(0, len(sums)):
        if(sums[a]>=max):
            max = sums[a]
            max_sum = a+2

        if(sums[a]<=min):
            min = sums[a]
            min_sum = a+2

    print("Total number of rolls:", total_rolls)
    print("Number of rolls of sum 2:", sums[0])
    print("Percent of rolls of sum 2:", 100*(sums[0]/total_rolls), "%")
    print("Number of rolls of sum 3:", sums[1])
    print("Percent of rolls of sum 3:", 100*(sums[1]/total_rolls), "%")
    print("Number of rolls of sum 4:", sums[2])
    print("Percent of rolls of sum 4:", 100*(sums[2]/total_rolls), "%")
    print("Number of rolls of sum 5:", sums[3])
    print("Percent of rolls of sum 5:", 100*(sums[3]/total_rolls), "%")
    print("Number of rolls of sum 6:", sums[4])
    print("Percent of rolls of sum 6:", 100*(sums[4]/total_rolls), "%")
    print("Number of rolls of sum 7:", sums[5])
    print("Percent of rolls of sum 7:", 100*(sums[5]/total_rolls), "%")
    print("Number of rolls of sum 8:", sums[6])
    print("Percent of rolls of sum 8:", 100*(sums[6]/total_rolls), "%")
    print("Number of rolls of sum 9:", sums[7])
    print("Percent of rolls of sum 9:", 100*(sums[7]/total_rolls), "%")
    print("Number of rolls of sum 10:", sums[8])
    print("Percent of rolls of sum 10:", 100*(sums[8]/total_rolls), "%")
    print("Number of rolls of sum 11:", sums[9])
    print("Percent of rolls of sum 11:", 100*(sums[9]/total_rolls), "%")
    print("Number of rolls of sum 12:", sums[10])
    print("Percent of rolls of sum 12:", 100*(sums[10]/total_rolls), "%")
    print("Sum that appears minimum number of times:", min_sum)
    print("Sum that appears maximum number of times:", max_sum)

#Q1
p = float(input("Enter principal: "))
y = float(input("Enter years: "))
r = float(input("Enter rate: "))
b1 = Bank(p, y, r)
print("Simple interest: ",b1.simple_interest())
print("Compound interest: ",b1.compound_interest())
print("\n")

#Q2
dictionary_operations()
print("\n")

#Q3
number_list = [-1,4,5,7,2,1,2,2,3,-1,7]
print(identical_pairs(number_list))
print("\n")

#Q4
sum_of_dice_rolls()
