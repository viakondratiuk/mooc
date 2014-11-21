def paying_the_minimum(balance, annualInterestRate, monthlyPaymentRate):
    totalPaid = 0
    for m in range(1, 13):
        minMonth = round(balance *  monthlyPaymentRate, 2)
        totalPaid += minMonth
        unpaidBalance = balance - minMonth
        balance = round(unpaidBalance + unpaidBalance * annualInterestRate / 12.0, 2)
        
        print("Month: " + str(m))
        print("Minimum monthly payment: " + str(minMonth))
        print("Remaining balance: " + str(balance))
        
    print("Total paid: " + str(totalPaid))
    print("Remaining balance: " + str(balance))
    
def paying_debt_in_year(balance, annualInterestRate):
    startBalance = balance
    dirtyMinMonthPayment = int(startBalance / 12)
    minMonthPayment =  dirtyMinMonthPayment - dirtyMinMonthPayment % 10
    monthInterestRate = annualInterestRate / 12.0
    month = 1
    
    while True:
        if month > 12:
            if balance < 0:
                break;
            else:
                month = 1
                balance = startBalance
                minMonthPayment += 10
        monthUnpaidBalance = round(balance - minMonthPayment, 2)        
        balance = round(monthUnpaidBalance + monthInterestRate * monthUnpaidBalance, 2)
        month += 1
    
    print('Lowest Payment: ' + str(minMonthPayment))
    
def paying_debt_in_year_bisect(balance, annualInterestRate):
    startBalance = balance
    monthInterestRate = annualInterestRate / 12.0
    
    lo = startBalance / 12
    hi = (startBalance * (1 + monthInterestRate) ** 12) / 12.0
    minMonthPayment = round((lo + hi) / 2, 2)    
    month = 1
    
    while True:
        if month > 12:            
            if abs(balance) <= 0.1:
                break
            else:
                if balance > 0:
                    lo = minMonthPayment
                else:
                    hi = minMonthPayment
                    
                minMonthPayment = round((lo + hi) / 2, 2)                
                month = 1
                balance = startBalance
    
        monthUnpaidBalance = round(balance - minMonthPayment, 2)        
        balance = round(monthUnpaidBalance + monthInterestRate * monthUnpaidBalance, 2)
        month += 1
        
    print('Lowest Payment: ' + str(minMonthPayment))

balance = 4773
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

paying_the_minimum(balance, annualInterestRate, monthlyPaymentRate)

balance = 3926
annualInterestRate = 0.2

paying_debt_in_year(balance, annualInterestRate)

balance = 999999
annualInterestRate = 0.18

paying_debt_in_year_bisect(balance, annualInterestRate)