import csv
field_name=['no','company','car model']
car=[{'no':1,'company':'Ferari','car model':'GH' },
     {'no':2,'company':'BNW','car model':'x5'},
     {'no':3,'company':'Maruti Suzuki','car model':'Swift'},
     {'no':4,'company':'Audi','car model':'Rush'},
     {'no':5,'company':'Toyota','car model':'Fortuner'}]
with open("s.csv",'w') as csvfile:
    writer=csv.DictWriter(csvfile,fieldnames=field_name)
    writer.writeheader()
    writer.writerows(car)

with open('s.csv',newline='') as csvfile:
    d=csv.reader(csvfile,delimiter='|')
    for r in d:
        print(','.join(r))
