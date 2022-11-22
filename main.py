######### 1-masala   parolni 3marta xato tersak 10gacha 5 marta xato tersak 15gacha sanaydi va yana qaytadan 3ta xato qilsa shu davom etaveradi
# import time
# k=0
# a=0
# j=0
# while True:
#     parolcha = input("Parolcha:")
#     if parolcha == "1234":
#         print("Tug'ri ee butaloqq")
#         break
#     else:
#         print("Qaytadan omadingni sinab ko'r10 daqiqa kut")
#         k+=1
#         if k == 3:
#             while a<10:
#                 a+=1
#                 time.sleep(.2)
#                 print(a)
#         elif k == 5:
#             for x in range(1,16):
#                 time.sleep(0.2)
#                 print(x)
#                 a=0
#                 k=0
        

#######################################################################################

# 2 -masala
# import time
# listcha = [5,6,7,8]
# for x in listcha:
#         for a in range(1,x+1):
#             time.sleep(1)
#             print(a) 


## 2-masala 2-usul
# for x in listcha:
#     if x == listcha[0]:
#         for a in range(1,x+1):
#             time.sleep(.5)
#             print(a) 
#     elif x == listcha[1]:
#         for a in range(1,x+1):
#             print(a) 
#             time.sleep(.5)
#     elif x == listcha[2]:
#         for a in range(1,x+1):
#             print(a) 
#             time.sleep(.5)
#     elif x == listcha[3]:
#         for a in range(1,x+1):
#             print(a) 
#             time.sleep(.5)
#     else:
#         for a in range(1,x+1):
#             print(a) 
#             time.sleep(.5)
     
######################################################################################

## 3-masala

# list = [2,5,8,3,5,90,56]

# for x in list:
#     if x % 2 == 0:
#         print(str(x) + " soni juftdir")
#     else:
#         print(str(x) + " soni toqdir")

#######################################################################################

#### 4-masala

# a = float(input("Sonchani kirit butaloq:"))

# if a % 2 ==0:
#     print(a," juft son bu")
# elif a % 2 ==1:
#     print(a," toq son bu")
# else:
#     print(a," vapshee bardakkku bu yerda")


k = [10, 20, 5, 30, 15] 
print(k[-1])