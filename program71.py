import csv
f=open('program70','w+')
insert=csv.writer(f)
fields=input("enter the separated with comma").split(',')
insert.writerow(fields)
n=int(input("enter the no of rows to insert"))
for i in range(0,n):
    print('row',i+1,':')
    rows=input("enter the values separated with comma").split(',')
    insert.writerow(rows)
f.close()
