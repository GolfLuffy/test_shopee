import pandas as pd

table=pd.read_excel('03 Python test and Dataset.xlsx',sheet_name='pricing_project_dataset')

order_table=dict()
result=dict()

#Get all shopee_order of each record(by each region)
for i in range(len(table)):
    if table.grass_region[i] not in order_table:
        order_table[table.grass_region[i]]=[]
        order_table[table.grass_region[i]].append(table.shopee_order[i])
        #Add region key and value in result
        result[table.grass_region[i]] = 0
    else:
        order_table[table.grass_region[i]].append(table.shopee_order[i])

for i in order_table:
    order_table[i].sort()
    highest_order=highest_order=order_table[i][-1]
    for j in range(len(order_table[i])):
        #top 30% of model (70% above)
        if order_table[i][j]>=(highest_order*0.7):
            result[i]+=1

final=[]
#Display result
for i in result:
    final.append([i,result[i]])

df=pd.DataFrame(final,columns=['Region','# of items'])
print(df)


