sval = '123'
ival = int(sval)
print(type(ival))
print(ival + 1)

#string does not contain numeric characters
nsv = 'hello bob'

niv = int(nsv)
print(type(niv))
print(niv + 1)      #except ValueError:
                    # print("Cannot convert 'hello bob' to an integer.")
