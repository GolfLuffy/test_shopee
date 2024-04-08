import pandas as pd

#read file from excel

table=pd.read_excel('03 Python test and Dataset.xlsx',sheet_name='pricing_project_dataset')

old_table=dict()
cpt_status=dict()
new_table=dict()

#get the information in old table and cpt status
for i in range(len(table)):
    if table.shopee_item_id[i] not in old_table:
        old_table[table.shopee_item_id[i]]=[]
        cpt_status[table.shopee_item_id[i]]=[]
        old_table[table.shopee_item_id[i]].append(table.shopee_model_id[i])
        cpt_status[table.shopee_item_id[i]].append(table.shopee_model_competitiveness_status[i])
    else:
        old_table[table.shopee_item_id[i]].append(table.shopee_model_id[i])
        cpt_status[table.shopee_item_id[i]].append(table.shopee_model_competitiveness_status[i])

#Set new logic
for i in old_table:
    for j in range(len(old_table[i])):
        if 'Shopee > CPT' in cpt_status[i][j]:
            new_table[i]='Shopee > CPT'
        elif 'Shopee = CPT' in cpt_status[i][j]:
            new_table[i] = 'Shopee = CPT'
        elif 'Shopee < CPT' in cpt_status[i][j]:
            new_table[i] = 'Shopee < CPT'
        else:
            new_table[i] = 'Others'

#Display result
result=list()
for i in new_table:
    result.append([i,new_table[i]])

df=pd.DataFrame(result,columns=['item_id','shopee_model_competitiveness_status'])


print(df)
