# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
runsscored = int(input("enter the runs scored"))
print(runsscored)
ballsfaced = int(input("enter the balls faced"))
print(ballsfaced)
fours = int(input("enter no of fours hit"))
print(fours)
six = int(input("enter no of six hit"))
print(six)
wicketstaken = int(input("enterno of wicketstaken"))
print(wicketstaken)
runcon = int(input("enter runs"))
print(runcon)
oversbowled = int(input("enter balls"))
print(oversbowled)
catchtaken = int(input("enter the no of catchtaken"))
print(catchtaken)

print("calculate batting strike rate")

batter=0
sr = (runsscored/ballsfaced)*100
print("batting strike rate is")
print(sr)

print("calculate balling economy")

bowler=0
er = runcon/oversbowled
print("balling economy is")
print(er) 

print("batting performance")
if runsscored >= 50 and sr >= 120:
    print("excellent batter")
elif runsscored >= 30 and sr >= 100:
    print("good batter")
elif runsscored >= 20:
    print("average batter")
else:
        print("poor batter")

print("balling performance")        
if wicketstaken >= 3 and er <= 6:
    print("excellent bowler")
elif wicketstaken >=2 and er <= 8:
    print("good bowler")
elif wicketstaken >= 1:
    print("average bowler")
else:
        print("poor bowler")
        
print("feilding performance")       
if catchtaken >= 2:
    print("outstanding feilder")
elif catchtaken == 1:
    print("active feilder")
else:
    print("needs improvement")
    
    print("overall allrounder decision")
    if batter == 1 and bowler == 1:
        print("star allrounder")
    elif batter == 2 and bowler == 2:
        print("strong allrounder")
    elif batter == 1 or bowler == 1:
        print("supporting allrounder")
        
    
    
    
        
        
          



