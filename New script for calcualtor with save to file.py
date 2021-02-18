# -*- coding: utf-8 -*-
"""
Created on Tue May 12 13:35:19 2020

@author: User1
"""

import csv

audit_bill = float(input("Enter billable audit hours: "))
tax_bill = float(input("Enter billable tax hours: "))
admin_hours = float(input("Enter nonbillable admin hours: "))
month = input("Enter month and year (full month name and year):  ")
tb = audit_bill + tax_bill
prop = audit_bill/tb
nonbill_audit = admin_hours*prop
total_audit = audit_bill + nonbill_audit
tax_nonbill = admin_hours - nonbill_audit
total_tax = tax_bill + tax_nonbill

print(("Audit:", audit_bill, nonbill_audit, total_audit, month))
print (("Tax:", tax_bill, tax_nonbill, total_tax, month))

#with open ('proportionsJorgeYTD2019.csv', 'w') as p:
    #csvwriter=csv.writer(p, delimiter= ',')
    #csvwriter.writerow (['Department', 'billable', 'nonbillable', 'total hours', 'month'])
    #csvwriter.writerow (['Audit', audit_bill, nonbill_audit, total_audit, month])
    #csvwriter.writerow (['Tax', tax_bill, tax_nonbill, total_tax, month])