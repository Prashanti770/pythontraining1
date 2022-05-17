#exception handling

# a/0 #zerodivision error
list1=[1,2,3,4,5]
try:
    a=list1[3] #if no error it will execute else, otherwise it will execute exception
except IndexError:
    print("index should be lessthan 4")

else:
    print("result :",a)

finally: #irrespective of error, it will be executed
    print("exceptions are handled")
