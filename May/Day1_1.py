## https://www.hackerrank.com/challenges/ginorts
##You are given a string .
# contains alphanumeric characters only.
# Your task is to sort the string  in the following manner:

#All sorted lowercase letters are ahead of uppercase letters.
#All sorted uppercase letters are ahead of digits.
#All sorted odd digits are ahead of sorted even digits.
#------code-----

df = list(input())
b = []
c = []
d = []
e = []
for i in df:
    if i in ('1','3','5','7','9'):
        b.append(i)
    if i in ('2','4','6','8','0'):
        c.append(i)
    if i.islower():
        d.append(i)
    if i.isupper():
        e.append(i)
b = sorted(b)
c = sorted(c)
d = sorted(d)
e = sorted(e)
r = d+e+b+c
print("".join(r))
