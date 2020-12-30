def nikhil():
    v = float(input("Enter the wind speed: "))
    t = float(input("Enter the temp: "))
    if(0 <= v <= 4):
        wci = t
        print(wci)
    elif(v >= 45):
        wci = 1.6 * t - 55
        print(wci)
    else:
        wci = 91.4 + (91.4 - t)*(0.0203 * v - 0.304 * (v) * 1/2 - 0.474)  
        print(wci)      
print("haui")
nikhil()
