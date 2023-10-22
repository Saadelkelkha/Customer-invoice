def facture(s,n):
    f=s+(s/100)*15-(s/100)*2
    print("Total to be paid to the customer",n,"is :",f,"DH")

n1=str(input("Give the first ana last name of customer n1 :"))
y=int(input("Give thr number of items for the customer n1 :"))
s1=0
for i in range (1,y+1):
        p=float(input("Give the price of the item :"))
        s1=s1+p
n2=str(input("give the first ana last name of customer n2 :"))
y=int(input("Give thr number of items for the customer n2 :"))
s2=0
for i in range (1,y+1):
        p=float(input("Give the price of the item :"))
        s2=s2+p
n3=str(input("give the first ana last name of customer n3 :"))
y=int(input("Give thr number of items for the customer n3 :"))
s3=0
for i in range (1,y+1):
        p=float(input("Give the price of the item :"))
        s3=s3+p
facture(s1,n1)
facture(s2,n2)
facture(s3,n3)