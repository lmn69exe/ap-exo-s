# I am not sure of the conditions here, so I included both versions jusssttt iiinnn ccaaassseeee (first is based on whats stated in the repo and second from the lecture notes)

#year = int(input("Please type in a year: "))

#if (year%4 == 0) or (year%100 == 0 and year%400 == 0):
##    print("The year is a leap year")
#else:
#    print("The year is not a leap year")

year = int(input("Please type in a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year")
else:
    print("The year is not a leap year")
