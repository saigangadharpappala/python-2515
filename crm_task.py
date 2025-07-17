print("=====CRM Customer Discount Calculation ====")

# GET USER INPUT
customer_Id  = int(input("Enter customerId:"))
customer_Name  = input("Enter customerName:")
isPremium  = (input("isPremium: ?(true/false)"))
yearsPartnership = int(input("yearsPartnership:"))
dealStage  = input("dealStage: ?(Proposal/Negotiation/Closed)")
dealValue = int(input("dealValue: "))

#initial discount set
discount = 0.0

#input validation
if isPremium == 'yes':
   discount = 0.10
elif isPremium == 'no' and yearsPartnership >= 3:
   discount = 0.05
else:
   discount = 0.0

match dealStage:
   case "Proposal":
      discount+= 0.02
   case "Negotiation":
      discount+= 0.03
   case "Closed":
      discount+=0.05

discountValue = dealValue * discount
finalPrice = dealValue - discountValue
print()
print(f"discount value is:{discountValue}")
print(f"finalprice is :{finalPrice}")
    
   
   

