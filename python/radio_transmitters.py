def hackerlandRadioTransmitters(x, k):
    x.sort()
    print(x)
    count = 1 # number of radio stations
    start = x[0] # radio coverage start
    radio = x[0] # radio station location
    for house in x:
        # if start is within range from current house, 
        # move the radio location to current house
        if house-start <= k: radio = house
        # if current house is out of range, add a radio station
        elif house-radio > k:
            count += 1
            start = house
            radio = house
   
    return count
