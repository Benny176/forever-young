for i in range(1,25,1):
    am = 'AM'
    pm = 'PM'
    if i <12 :
        print('{} {}'. format(i, am))
    else:
        print('{} {}'. format(i, pm))
