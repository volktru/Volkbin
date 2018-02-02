import time
print "\n"
name=raw_input("What is your name?: ")
print "\n"
color=raw_input("What is your favorite color?: ")
time.sleep(1)
print "\n"
print "Alright, %s.  Do you like %s eggs and ham? " % (name, color)
time.sleep(2)
test=raw_input("yes or no?: ")
print "\n"
True = "yes"
if ((test) == True):
    print 'Well good then Trubo!'
else:
    print 'Well then %s! YOU SUCK!' % (name)
print "\n"
