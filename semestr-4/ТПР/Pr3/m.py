s1 =1 + 3 + 1 + 3
s2 = 1/3 + 1 + 3 + 1 
s3 = 1 + 1/3 + 1 + 3
s4 =1/3 + 1 + 1/3 + 1 
p1 = s1 * 0.127
p2= s2 * 0.232
p3= s3 * 0.260
p4= s4 * 0.381

print(s1, p1)
print(s2, p2)
print(s3, p3)
print(s4, p4)

P_SUM = p1 + p2 + p3 + p4 
print("akfa p = ", P_SUM)

i = (P_SUM - 4) / ( 4 - 1)

print(i)

print("Вот это =  ", i/0.90 )