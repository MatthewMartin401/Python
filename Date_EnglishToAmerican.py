# Eng datatime to American datetime.

import datetime
from datetime import date

while True:
    d = int(input("day: "))
    m = int(input("month: "))
    y = int(input("year: "))
    try:
        main = datetime.date(y, m, d)
        print(main)

        eng = main.strftime("%d %m %y")

        amer = eng.strftime("%x") #  inputed directive changes the format.
        print(amer)
        
        print(main)
        break
    except:
        print("Invalid date")
