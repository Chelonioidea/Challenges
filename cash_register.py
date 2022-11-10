import math

cid = [["HUNDRED", 100, 100.00], ["TWENTY", 20, 60.00], ["TEN", 10, 50.00], ["FIVE", 5, 50.00], ["ONE", 1, 100.00], 
['QUARTER', .25, 10.00], ["DIME", .10, 5.00], ["NICKLE", .05, 2.05], ["PENNY", .01, 1.01]]

def change_due(customer_due, cid):
    change = []

    for bill_name, bill_size, amount  in cid:
        bills = math.floor(customer_due / bill_size)
        if (bills * bill_size) > amount:
            chg_tnd_so_far = amount
            bills = amount / bill_size
            #if : See if change can be made with the next x bills
        #       pass    
        else: 
            chg_tnd_so_far = (bills * bill_size)
        customer_due = round(customer_due - chg_tnd_so_far, 2)
        change.append([bill_name, bills]) 
    return(change)


def drawer_sum(cid):
    drawer_sum = 0

    for _, _, amount in cid:
        drawer_sum += amount
    return drawer_sum

def run_transaction(price, cash_tendered, cid):
    drawer_total = drawer_sum(cid)
    customer_due = cash_tendered - price

    if cash_tendered < price:
        return "Insufficient Funds Tendered"
    elif cash_tendered == price:
        return "No change due"
    elif (customer_due) > drawer_total:
        return "insufficient Funds in Drawer"
    else:
        return change_due(customer_due, cid)
        

print(run_transaction(600, 700, cid))
