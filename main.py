originalBalance = 999999
annualInterest = 0.18
monthlyInterest = annualInterest/12
monthlyPaymentLower = round(originalBalance/12,2)
monthlyPaymentUpper = round((originalBalance*(1+monthlyInterest)**12)/12,2)
balance = originalBalance


while balance > 0.1 or balance < -0.1:
  balance = originalBalance
  for months in range(12):
    balance = balance - monthlyPaymentLower
    balance = balance*(1 + monthlyInterest)
  monthlyPaymentLower = monthlyPaymentLower + 0.01
  #print(round(balance, 1))
  monthlyPayment = monthlyPaymentLower - 0.01
  balance = originalBalance
  for months in range(12):
    balance = balance - monthlyPaymentUpper
    balance = balance*(1 + monthlyInterest)
  monthlyPaymentUpper = monthlyPaymentUpper - 0.01
  #print(round(balance, 1))
  monthlyPayment = monthlyPaymentUpper + 0.01
print(round(monthlyPayment,2))
