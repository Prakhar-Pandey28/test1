# Accept the date in DD-MM-YYYY format as input and print the year as output
date = input("Enter date: ")

#year = date[0:10]
# date[start: end] 28-11-2000
# start = 0 index , 2 is starting in date and end 10 lastindex which is equal to 0.
#output 28-11-2000

year = date[-4:]

#date[-4:]
#[end:start] means starting from backside
#output 2000

#year = date[-4:-1]
#output 200

print(year)
