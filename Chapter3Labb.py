#Software Sales Chapter 3 lab Programming Exercise #12 page 154
#Jeremy Bargy
#Jan. 24, 2020

#Initalize variables
userName = "" #str
numberOfPackages = 0 #int
amountOfDiscount = 0.0 #float
purchaseTotal = 0.0 #float
packageCost = 99.00 #float constant
orderAmount = 0.0 #float

#Get user name and number of packages to be purchased
userName= input('Please enter your name: \n')
numberOfPackages= int(input('Please enter the number of software packages you would like to purchase as a number value. i.e 3 for three: \n'))

#Determine discount amount.
if numberOfPackages >= 100:
    amountOfDiscount = 0.4
elif numberOfPackages >= 50:
    amountOfDiscount = 0.3
elif numberOfPackages >= 20:
    amountOfDiscount = 0.2
elif numberOfPackages >= 10:
    amountOfDiscount = 0.1
else:
    amountOfDiscount = 0.0
                     
#Calculate the order amount without discount.
orderAmount = packageCost * numberOfPackages

#Calculate the amount of the discount.
discount = orderAmount * amountOfDiscount

#Calculate the sale price.
purchaseTotal = orderAmount - discount

#Calculate savings.
savings = orderAmount - purchaseTotal

#Display results to user
print(userName, 'has a discount amount of', format(amountOfDiscount , '.0%'), 'for ordering', numberOfPackages, 'units.')
print('The total amount of the order with the discount is $',format(purchaseTotal, ',.2f'),sep='')
print('With the total discount savings of $',format(savings , ',.2f'),sep='')
print('From the normal price of $', format(orderAmount, ',.2f'),sep='')