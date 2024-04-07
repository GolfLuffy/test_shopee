import pandas as pd

#read file from excel
table=pd.read_excel('03 Python test and Dataset.xlsx',sheet_name='pricing_project_dataset')
table1=pd.read_excel('03 Python test and Dataset.xlsx',sheet_name='platform_number')

region_and_product=dict()
region_and_total_order=dict()
net_cpt_shopee_win=dict()
net_cpt_cpt_win=dict()
net_cpt_total=dict()
net_cpt=dict()

#distinct region
for i in range(len(table)):
    if table.grass_region[i] not in region_and_product:
        region_and_product[table.grass_region[i]]=[]
        region_and_total_order[table.grass_region[i]]=[]
        net_cpt_shopee_win[table.grass_region[i]] = []
        net_cpt_cpt_win[table.grass_region[i]] = []
        net_cpt_total[table.grass_region[i]] = []
        net_cpt[table.grass_region[i]] = []

#Each region distinct cluster items
for j in range(len(table)):
    for k in region_and_product:
        if table.grass_region[j]==k:
            if table.category_group[j] not in region_and_product[k]:
                region_and_product[k].append(table.category_group[j])
                #Set value following index of cluster item
                region_and_total_order[k].append(0)
                net_cpt_shopee_win[k].append(0)
                net_cpt_cpt_win[k].append(0)
                net_cpt_total[k].append(0)
                net_cpt[k].append(0)

for k in region_and_product:
    region_and_product[k].sort()

#To calculate to find total order in each region and each cluster
for i in range(len(table)):
    for j in region_and_product:
        for k in range(len(region_and_product[j])):
                if table.grass_region[i] == j and table.category_group[i]==region_and_product[j][k]:
                    region_and_total_order[j][k]=region_and_total_order[j][k]+table.shopee_order[i]

#To calculate to find order coverage in each region and each cluster
#total order divided by platform order (by region)
for i in region_and_total_order:
    for j in range(len(table1)):
        for k in range(len(region_and_total_order[i])):
            if table1.region[j]==i:
                region_and_total_order[i][k]=region_and_total_order[i][k]/table1.platform_order[j]
                region_and_total_order[i][k]=f"{region_and_total_order[i][k]:.2%}"

#To find each entity to calculate net cpt
for i in range(len(table)):
    for j in region_and_product:
        for k in range(len(region_and_product[j])):
            if table.grass_region[i] == j and table.category_group[i]==region_and_product[j][k]:
                #Shopee > CPT
                if table.shopee_model_competitiveness_status[i]=='Shopee > CPT':
                    net_cpt_shopee_win[j][k]+=1
                    net_cpt_total[j][k]+=1
                # Shopee < CPT
                elif table.shopee_model_competitiveness_status[i]=='Shopee < CPT':
                    net_cpt_cpt_win[j][k] += 1
                    net_cpt_total[j][k] += 1
                # Shopee = CPT
                else:
                    net_cpt_total[j][k] += 1

#To calculate net cpt
for i in region_and_product:
    for j in range(len(region_and_product[i])):
        net_cpt[i][j]=((net_cpt_cpt_win[i][j]-net_cpt_shopee_win[i][j])/net_cpt_total[i][j])
        net_cpt[i][j] = f"{net_cpt[i][j]:.2%}"

#Display result
result=list()
for i in region_and_product:
    for j in range(len(region_and_product[i])):
        result.append([i,region_and_total_order[i][j],net_cpt[i][j],region_and_product[i][j]])

df=pd.DataFrame(result,columns=['Region','Order Coverage','Net Competitiveness','# of Item'])

print(df)

