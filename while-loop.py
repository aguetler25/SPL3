# while schleifen

ende = False
c = 0
while (ende == False):
    c += 1
    pwd = input("password please: ")
    if (pwd == "hallo"):
        ende = True
    else:
        print ("wrong password - please try again...")
        print ("bad logins", c)

print ("login ok.")
