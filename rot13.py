import string
rot13 = str.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz://.%?=-", 
    "NOPQRSTUVWXYZnopqrstuvwxyz://.%?=-ABCDEFGHIJKLMabcdefghijklm")

str.translate("This used to be classed as encryption.", rot13)

rot13-reverse = str.maketrans(
    "",
    "")

str.translate("(u19I)", rot13-reverse)
str.translate("uLLHKfhhLrnzKizvpJGKGsLipGzh_#hqvKpGarJ m MKr wGvF Lrnz bvLu pGqr", rot13-reverse)
