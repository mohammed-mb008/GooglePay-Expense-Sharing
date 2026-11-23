import numpy as np
from prettytable import PrettyTable

friends=["Arun","David","Harini","Azeem"]
expense_matrix=np.zeros((len(friends),(len(friends))))

def add_expense(payer,benficiery,amount):
    payer_index=friends.index(payer)
    share_per_prsn=amount/(len(benficiery))
    for benificeries in benficiery:
        benificeries_indx=friends.index(benificeries)
        expense_matrix[payer_index][benificeries_indx]+=share_per_prsn

def expense_calci():
    total_paid=np.sum(expense_matrix,axis=1)
    total_owes=np.sum(expense_matrix,axis=0)
    net_balance=total_paid-total_owes
    return net_balance

def display_expenses():
    settelments=expense_calci()
    table=PrettyTable()
    table.field_names=["frnds","settelments"]
   
    for i,friend in enumerate(friends):
        if settelments[i]>0:
            table.add_row([friend,f"should receive ₹{settelments[i]:.2f}"])
        elif settelments[i]<0:
            table.add_row([friend,f"owes amount of ₹{-settelments[i]:.2f}"])
        else:
            table.add_row([friend,"debt is settled"])
    print("\n Print Statement")
    print(table)
   
def suggest_amount():
    settelments=expense_calci()
    creditors=[(friends[i],amt) for i,amt in enumerate(settelments)if amt>0]
    debtors=[(friends[i],-amt) for i,amt in enumerate(settelments)if amt<0]
    transactions=[]

    while debtors and creditors:
        debtor, debt_amount = debtors.pop(0)
        creditor, credit_amount = creditors.pop(0)
        
        payment = min(debt_amount, credit_amount)

        transactions.append((debtor, creditor, payment))

        debt_amount -= payment
        credit_amount -= payment

        if debt_amount > 0:
            debtors.insert(0, (debtor, debt_amount))
        if credit_amount > 0:
            creditors.insert(0, (creditor, credit_amount))

    print("\nSuggested Transactions:")

    if transactions:
        for debtor, creditor, amount in transactions:
            print(f"{debtor} should pay ₹{amount:.2f} to {creditor}")
    else:
        print("All debt is settled!")

            
add_expense("Arun", ["Arun","David","Harini","Azeem"],1500)
add_expense("David", ["David","Harini","Azeem"],3000)
add_expense("Azeem", ["Azeem","Harini"],500)
add_expense("Harini", ["Harini","Arun","Azeem"],2000)

display_expenses()
suggest_amount()

