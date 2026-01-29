from lib_military.file_military import Soldier, Regiment, Company

print('TASK 1:')
print("---------------------------------------------------------------------------------------------------------------")

import datetime as dt
from datetime import timedelta
from datetime import date
dt_current = dt.datetime.now()
delta_three_hours_ago = timedelta(hours=3)
print(dt_current)
dt_three_hours_ago = dt_current - delta_three_hours_ago
print(dt_three_hours_ago)

print("---------------------------------------------------------------------------------------------------------------")
print('TASK 2:')
print("---------------------------------------------------------------------------------------------------------------")

import pandas

print("---------------------------------------------------------------------------------------------------------------")
print('TASK 3:')
print("---------------------------------------------------------------------------------------------------------------")

import lib_military.file_military as mil

def add_sold_to_reg(regiment, soldiers):                # добавление солдата в полк
    if not isinstance(soldiers, list):
        soldiers = [soldiers]
    regiment.reg_soldiers += [s for s in soldiers if s not in regiment.reg_soldiers]
    for s in soldiers:
        s.sold_regiment = regiment
    return regiment.reg_soldiers

def add_sold_to_comp(company, soldiers):                # добавление солдата в роту
    if not isinstance(soldiers, list):
        soldiers = [soldiers]
    company.comp_soldiers += [s for s in soldiers if s not in company.comp_soldiers]
    for s in soldiers:
        s.sold_company = company
    return company.comp_soldiers

def add_reg_to_comp(company, regiments):                # добавление полка в роту
    if not isinstance(regiments, list):
        regiments = [regiments]
    company.comp_regiments += [r for r in regiments if r not in company.comp_regiments]
    for r in regiments:
        for s in r.reg_soldiers:
            s.sold_company = company
        r.reg_company = company
    return company.comp_regiments

sold1 = Soldier('Alex', date(2000, 12, 3))
sold2 = Soldier('Andre', date(1997, 10, 2))
reg1 = Regiment(133)
comp1 = Company(9)

add_sold_to_reg(reg1, sold1)
add_reg_to_comp(comp1, reg1)
print(sold1)