print "FizzBuzz"
broj = raw_input("Molim stavi broj:")
broj = int(broj)
for broj in range(1,broj+1):
    if broj %3 == 0 and broj %5==0:
        print "Djeljiv sa 3 i 5"
    elif broj % 3 == 0:
        print "Djeljiv sa 3"
    elif broj % 5 == 0:
        print "Djeljiv sa 5"
    else:
        print broj

        











