#26 mins with music

amt = float(input("Enter the amount that you would like to be converted into change: "))
dollar_2, dollar_1, cent_25, cent_2, cent_1 = 0, 0, 0, 0, 0

while amt > 0:
    if amt >= 2:
        amt -= 2
        dollar_2 += 1

    elif amt >= 1:
        amt -= 1
        dollar_1 += 1

    elif amt >= 0.25:
        amt -= 0.25
        cent_25 += 1

    elif amt >= 0.02:
        amt -= 0.02
        cent_2 += 1 

    elif amt >= 0.01:
        amt -= 0.01
        cent_1 += 1
   	
    else:
    	break
        
print(f"You would need {dollar_2} of $2, {dollar_1} of $1, {cent_25} of ¢25, {cent_2} of ¢2 and {cent_1} of ¢1")