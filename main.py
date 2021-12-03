"""
1. get input about milk came (z)
2. at the end of day get input about sold out milk and current available milk (x,y)

(z - x) - y

3. store the waste data in csv file
"""

from datetime import datetime
import pandas

def write_file(data,loc):
    file = open(loc,"w")
    file.write(data)
    file.close()

# current data and time
today = datetime.today()

# opening file to check if user want to run program second time or first
tmp_file = open("tmp.txt","r")

has_input = False

milk_qt = 0
sold_milk = 0
avail_milk = 0
total_waste = 0

# getting data (file_state milk quantity)
tmp_data = tmp_file.read().split()

if tmp_data[0] == "1": # if user has opened file before
    has_input = True

# for the sack of memory
tmp_file.close()

if has_input == False: # if user hasnt open filr before 
    # getting first input
    milk_qt = float(input("Milk came: "))
    # wirting file state and milk quantity data 
    write_file(f"1 {milk_qt}","tmp.txt")

if has_input == True:
    # retriving the milk quantity data
    tmp_file = open("tmp.txt",'r')
    tmp_data = tmp_file.read().split() 
    milk_qt = float(tmp_data[1])
    tmp_file.close()

    # reseting the tmp file
    write_file("0","tmp.txt")

    # getting second input
    sold_milk = float(input("How much milk you sold: "))
    avail_milk = float(input("How much milk has left: "))

    # calculating waste
    total_waste = (milk_qt - sold_milk) - avail_milk

    # writing csv 
    tmp_file = open("data.csv","a")
    tmp_file.write(f"{today},{total_waste}\n")
    tmp_file.close()

    # showing data
    df = pandas.read_csv("data.csv")

    # log
    print(f"[-] Total milk wasted in liters: {total_waste}")
    print(f"\n\n{df}")