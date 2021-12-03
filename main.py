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

today = datetime.today()

tmp_file = open("tmp.txt","r")
has_input = False

milk_qt = 0
sold_milk = 0
avail_milk = 0
total_waste = 0

tmp_data = tmp_file.read().split()

if tmp_data[0] == "1":
    has_input = True

tmp_file.close()

if has_input == False:
    # getting first input
    milk_qt = float(input("Milk came: "))
    write_file(f"1 {milk_qt}","tmp.txt")

if has_input == True:
    # retriving the first input
    tmp_file = open("tmp.txt",'r')
    tmp_data = tmp_file.read().split() 
    milk_qt = float(tmp_data[1])
    tmp_file.close()

    # reseting the tmp file
    write_file("0","tmp.txt")

    # getting second input
    sold_milk = float(input("How much milk you sold: "))
    avail_milk = float(input("How much milk has left: "))

    total_waste = (milk_qt - sold_milk) - avail_milk

    tmp_file = open("data.csv","a")
    tmp_file.write(f"{today},{total_waste}\n")
    tmp_file.close()

    df = pandas.read_csv("data.csv")

    print(f"[-] Total milk wasted in liters: {total_waste}")
    print(f"\n\n{df}")