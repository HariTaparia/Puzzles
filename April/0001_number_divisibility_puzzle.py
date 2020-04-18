/*A number of 9 digits has the following properties: • The number comprising the leftmost two digits is divisible by 2, that comprising the leftmost three digits is divisible by 3, the leftmost four by 4, the leftmost five by 5, and so on for the nine digits of the number i.e. the number formed from the first ndigits is divisible by n, 2<=n<=9.
• Each digit in the number is different i.e. no digits are repeated. • The digit 0 does not occur in the number i.e. it is comprised only of the digits 1-9 in some order.
Find the number.*/
/********code******/
import time
start_time = time.clock()

list1 = [0,2,4,6,8]
list2 = [0,5]
a1 = 0
for i in range(1,10):
    a1 = i
    for j in list1:
        a2 = j
        if(a1!=a2):
            for k in range(0,10):
                a3 = k
                if((a1!=a3) and (a2!=a3)):
                    if((a1+a2+a3)%3 == 0):
                        for l in list1:
                            a4 = l
                            if ((a1!=a4) and (a2!=a4) and (a3!=a4)):
                                if((a3*10+a4)%4==0):
                                    for m in list2:
                                        a5 = m
                                        if ((a1!=a5) and (a2!=a5) and (a3!=a5)and (a4!=a5)):
                                            for n in list1:
                                                a6 = n
                                                if ((a1!=a6) and (a2!=a6) and (a3!=a6)and (a4!=a6)and (a5!=a6)):
                                                    if((a1+a2+a3+a4+a5+a6)%3==0):
                                                        for o in range(0,10):
                                                            a7 = o
                                                            if ((a1!=a7) and (a2!=a7) and (a3!=a7)and (a4!=a7)and (a5!=a7)and (a6!=a7)):
                                                                if ((a1*1000000+a2*100000+a3*10000+a4*1000+a5*100+a6*10+a7)%7==0):
                                                                    for p in list1:
                                                                        a8 = p
                                                                        if ((a1!=a8) and (a2!=a8) and (a3!=a8)and (a4!=a8)and (a5!=a8)and (a6!=a8)and(a7!=a8)):
                                                                            if ((a6*100+a7*10+a8)%8==0):
                                                                                for q in range(0,10):
                                                                                    a9 = q
                                                                                    if ((a1!=a9) and (a2!=a9) and (a3!=a9)and (a4!=a9)and (a5!=a9)and (a6!=a9)and(a7!=a9)and(a8!=a9)):
                                                                                        if((a1+a2+a3+a4+a5+a6+a7+a8+a9)%9==0):
                                                                                            number = ((((((((a1*10)+a2)*10+a3)*10+a4)*10+a5)*10+a6)*10+a7)*10+a8)*10+a9
                                                                                            print(number)

print (time.clock() - start_time, "seconds")
