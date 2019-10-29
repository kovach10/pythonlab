# n = int(input("n="))
# if n<= 50:
#      print(".*.")
#      print("***")
#      print(".*.")
# elif n<= 100:
#      print("..*..")
#      print("..*..")
#      print("*****")
#      print("..*..")
#      print("..*..")
# elif n<= 0:
#      print("no")

# n=int(input("n="))
#a=[int(input(" el {0}:".format (i))) for i in range (n)]
# n=[1,2,3,4,5,(-1),(-2),(-3)]

# def get_total_price(a,b,c):
#     return a*b*c
# a=float(input("a= "))
# b=float(input("b= "))
# c=float(input("c= "))
#
# p= get_total_price(a,b,c)
# print("p={0}".format(p))

def get_max(a,b):    #ok
    if(a>b):
        return a
    else:
        return b
print("max={0}".format (get_max(100,1)))
