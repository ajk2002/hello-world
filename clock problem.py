minLate = int(input("how many minutes late"))

minLate2 = int(input("how many mins late"))
coeff= 60 + minLate
coeff2= 60 + minLate2
stop = True





for i in range(1,50000):

    x = ((coeff * i)% 1440)
    y = ((coeff2 * i)% 1440)
    print (x)
    print (y)
    if x == y:
        print("this is", i, "hours")
        break
hours = int(x / 60)
mins = x % 60

if hours >= 0 and hours < 10:
    
    print("the time is", "0",hours, ":", mins)
if mins < 10:
    mins = ("0",mins)
else:
    print("the time is", "0",hours, ":", mins)

    
    
            
            
        
         
        
