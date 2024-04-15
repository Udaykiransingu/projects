from datetime import datetime

name=input("Enter your name:")
lists='''
Rice    Rs 20/kg
Sugar   Rs 30/kg
Oil     Rs 40/litr
Boost   Rs 100/1bottle
Salt    Rs 20/kg
Maggie  Rs 10/1packet
Colgate Rs 50/ 1each
'''
#Declaration
price=0
pricelist=[]
totalprice=0
finalprice=[]
ilist=[]
qlist=[]
plist=[]
items={'Rice':20,
       'Sugar':30,
       'Oil':40,
       'Boost':100,
       'Salt':20,
       'Maggie':10,
       'Colgate':50}
option=int(input("For list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(lists)):
    inp1=int(input("if you want to buy press 1:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your item:")
        quantity=int(input("enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalAmount=gst+totalprice
        else:
            print("Sorry you entered item is not available")
    else:
        print("you entered wrong number")

    inp=input("Can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalAmount!=0:
            print(25*"=","Uday supermarket",25*"=")
            print(28*" ","GUNTUR")
            print("Name:",name,30*"","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",5*' ','items',8*" ",'Quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*" ",5*" ",ilist[i],10*" ",qlist[i],14*" ",plist[i])
            print(75*'')
            print(50*"","TotalAmount:",'Rs',totalprice)
            print("gst Amount",50*"",'Rs',gst)
            print(75*"-")
            print(50*"",'finalAmount:','Rs',finalAmount)
            print(75*"-")
            print(50*"","Thanks for visitng")
            print(75*"-")

