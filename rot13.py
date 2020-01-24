import string
rot13 = str.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz://.%?=-", 
    "NOPQRSTUVWXYZnopqrstuvwxyz://.%?=-ABCDEFGHIJKLMabcdefghijklm")

str.translate("This used to be classed as encryption.", rot13)

rot13-reverse = str.maketrans(
    "",
    "")

str.translate("(2pMJ)", rot13-reverse)
str.translate("uLLHKfhhLrnzKizvpJGKGsLipGzhyhpunFFryh19j3nsp4so01r5231438onson746q5r16\
4o74j40LuJrnqiKxdHrhTrFrJnyktJGMHVql30qnpss3mr74om4433mo7pqm2045145265r5\
&LrFnFLVql76n2nr5nm9s00m4s6om95rqm5q33q77p4q61", rot13-reverse)
