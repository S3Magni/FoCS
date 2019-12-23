# -*- coding: utf-8 -*-

# https://gdv.github.io/foundationsCS/2019-project

import pandas
import tqdm
import time

path = "C:/Users/Lenovo/Desktop/Nuova cartella/"
n = 1000
n = 0

class Main :
    def reader(self, fname, nrows, com='read_csv', sep=','):
        self.fname = fname
        self.nrows=nrows
        x = {}
        if nrows>0:
            exe = "import pandas ; f = pandas." + com + "('" + fname + "'," + "sep='" + sep + "', nrows=" + str(nrows) + ")"
        else:
            exe = "import pandas ; f = pandas." + com + "('" + fname + "'," + "sep='" + sep + "')"
        exec(exe, x)
        return x['f']


Mn=Main()


### POUNTO 1
fname_ll = path + "loans_lenders.csv"
loans_lender = Mn.reader(fname=fname_ll, nrows=n); del fname_ll
print(list(loans_lender.columns))

m=max(n, len(loans_lender))
lenders = loans_lender.iloc[0:m, 1]
col1_N = []
count_lenders_number = []
for el in tqdm.tqdm(lenders):
    l = el.split(",")
    col1_N.append(l[0])
    count_lenders_number.append(len(l))
del el; del l; del lenders
loans_lender_Nl = {list(loans_lender.columns)[0]: loans_lender.iloc[0:m, 0], list(loans_lender.columns)[1]: col1_N}
del col1_N
loans_lender_N = pandas.DataFrame(data=loans_lender_Nl)
del loans_lender_Nl
print(loans_lender_N.head())
count_lenders_number_ID = {list(loans_lender.columns)[0]: loans_lender.iloc[0:m, 0], "number_of_lenders": count_lenders_number}
count_lenders_number_ID = pandas.DataFrame(data=count_lenders_number_ID)

### PUNTO 2
fname_l = path + "loans.csv"
loans_ = Mn.reader(fname=fname_l, nrows=n); del fname_l
print(list(loans_.columns))
print(loans_.head())

import datetime

#dur=loans_.iloc[:, [0,19,20]]
#Mn.dater(file=dur, ncol=1)
#Mn.dater(file=dur, ncol=2)

#for el in tqdm.tqdm(range(0,len(dur.iloc[:, 0]))):
#    if type(dur.iloc[el, 1])== str:
#        l = dur.iloc[el, 1].split(" ")[0]
#        dur.iloc[el, 1] = datetime.datetime.strptime(l, '%Y-%m-%d').date()
#    if type(dur.iloc[el, 2])== str:
#        r = dur.iloc[el, 2].split(" ")[0]
#        dur.iloc[el, 2] = datetime.datetime.strptime(r, '%Y-%m-%d').date()
#    print(el)
#del el; del l; del r

#fname_dur = path + "dur.csv"
#dur=Mn.reader(fname=fname_dur, nrows=0)
#dur["planned_expiration_time"] = pandas.to_datetime(dur["planned_expiration_time"])
#dur["disburse_time"] = pandas.to_datetime(dur["disburse_time"])
#dur.insert(3, "loans_duration", dur.iloc[:, 1]-dur.iloc[:, 2], True)
#for el in tqdm.tqdm(range(0,len(dur.iloc[:, 0]))):
#    if dur.iloc[el, 3]!= int:
#        dur.iloc[el, 3] = dur.iloc[el,3].days
#del el

#dur.to_csv(path_or_buf="C:/Users/Lenovo/Desktop/Nuova cartella/dur.csv", index=False, date_format='%Y-%m-%d')

#loans_lender_ND = pandas.merge(loans_lender_N, dur.iloc[:, [0, 3]], on="loan_id", right_index=True)

### PUNTO 3
count_lenders = loans_lender_N["lenders"].value_counts()
print(count_lenders[count_lenders > 1])

### PUNTO 4
list_country = []

list_pos=[] # per punto 5

for el in tqdm.tqdm(range(0,
#                len(loans_.iloc[:, 0])
                10000)):
    if type(loans_["town_name"][el]) == float and type(loans_["borrower_genders"][el]) == float:
        list_country.append(loans_["country_name"][el])
        list_pos.append(el)
del el
count_country = {i: list_country.count(i) for i in list_country}

### PUNTO 5
country_loan = {i: 0 for i in list_country}
for el in tqdm.tqdm(list_pos):
    if loans_["country_name"][el] in list_country:
        country_loan[loans_["country_name"][el]] += loans_["loan_amount"][el]
del el

### PUNTO 6
total = loans_["loan_amount"].sum(axis=0, skipna=True)
a = list(country_loan.values())/total; a = a.tolist()
z = zip(list_country, a)
country_loan_prop = dict(z)
del a; del z; del list_country

### PUNTO 7
list_country_Y = []

#list_pos=[] # per punto 5

for el in tqdm.tqdm(range(0,
#                len(loans_.iloc[:, 0])
                10000)):
    if type(loans_["town_name"][el]) == float and type(loans_["borrower_genders"][el]) == float:
        list_country_Y.append(loans_["country_name"][el] + " " + loans_["disburse_time"][el][0:4])
del el
count_country_Y = {i: list_country_Y.count(i) for i in list_country_Y}

country_loan_Y = {i: 0 for i in list_country_Y}
for el in tqdm.tqdm(list_pos):
    if loans_["country_name"][el] + " " + loans_["disburse_time"][el][0:4] in list_country_Y:
        country_loan_Y[loans_["country_name"][el] + " " + loans_["disburse_time"][el][0:4]] += loans_["loan_amount"][el]
del el

a = list(country_loan_Y.values())/total; a = a.tolist()
z = zip(list_country_Y, a)
country_loan_prop_Y = dict(z)
del a; del z; del list_country_Y

### PUNTO 8

#dddd = pandas.merge(loans_, count_lenders_number_ID, on="loan_id", right_index=True)
