scores = [20,94,10,32,5,9,18,20,13,19,110]
print(f"Number of players: {len(scores)}.")
for score in scores:
    print(f"{score}")


#sum
total = 0
for score in scores:
    total = total + score
print(f"Total score of the team is {total}.")    


#highest score
highest = scores[0]
for score in scores:
    if highest < score:
       highest = score
print(f"Highest score in the team is {highest}.")



#lowest score
lowest = scores[0]
for score in scores:
    if lowest > score:
       lowest = score
print(f"Lowest score in the team is {lowest}.")



#yaha pr ek chiz notice karne vali hai ki 'scores' list hai to ham 'sum','max','min' function ka bhi use kar sakte hai