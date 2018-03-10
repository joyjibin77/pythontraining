#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      RGCET
#
# Created:     10/03/2018
# Copyright:   (c) RGCET 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


x=int(input("Enter a number: "))
mod=x % 2
if mod>0:
    print("This is an odd number.")
elif x==0:
    print("value is not even or odd")
else:
    print("This is an even number.")
