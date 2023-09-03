import pandas as pd
import os
import json
import re

#%%

def data_aggregated_transaction_total(path='data/aggregated/transaction/'):
    data_list = [ ] 
    for d,i,f in os.walk(path):
        if 'state' not in d:
            for file in f:
                if file.endswith('.json'):
                    data_json = json.load(open(d+'/'+file))
                    year_dir = int(re.sub('[^0-9]','',d))
                    for dt in data_json['data']['transactionData']:
                        row_dict = {
                            'Name': dt['name'],
                            'Transaction_Year': year_dir,
                            'Quarters': int(file.split('.')[0]),
                            'Transaction_Type': dt['paymentInstruments'][0]['type'],
                            'Transaction_Count': dt['paymentInstruments'][0]['count'],
                            'Transaction_Amount': dt['paymentInstruments'][0]['amount']
                        }
                        data_list.append(row_dict)
                        
    data = pd.DataFrame(data_list)
    data = data.drop_duplicates()
    null_counts = data.isnull().sum()
    print(null_counts)
    return data


def data_aggregated_transaction_state(path='data/aggregated/transaction/country/india/state/'):
    data_list = [ ] 
    for d,i,f in os.walk(path):
        for file in f:
            if file.endswith('.json'):
                data_json = json.load(open(d+'/'+file))
                year_dir = int(re.sub('[^0-9]','',d))
                state_dir = d.split('\\')[-2].split('/')[-1]
                for dt in data_json['data']['transactionData']:
                    row_dict = {
                        'Name': dt['name'],
                        'States': state_dir,
                        'Transaction_Year': year_dir,
                        'Quarters': int(file.split('.')[0]),
                        'Transaction_Type': dt['paymentInstruments'][0]['type'],
                        'Transaction_Count': dt['paymentInstruments'][0]['count'],
                        'Transaction_Amount': dt['paymentInstruments'][0]['amount']
                    }
                    data_list.append(row_dict)

    data = pd.DataFrame(data_list) 
    data = data.drop_duplicates()
    null_counts = data.isnull().sum()
    print(null_counts)
    return data
    

#%%

def data_aggregated_user_total(path='data/aggregated/user/country/india/'):
    data_list = [ ] 
    for d,i,f in os.walk(path):
        if 'state' not in d:
            for file in f:
                if file.endswith('.json'):
                    data_json = json.load(open(d+'/'+file))
                    year_dir = int(re.sub('[^0-9]','',d))
                    if data_json['data']['usersByDevice'] is not None:
                        for dt in data_json['data']['usersByDevice']:
                            row_dict = {
                                'registeredUsers': data_json['data']['aggregated']['registeredUsers'],
                                'appOpens': data_json['data']['aggregated']['appOpens'],
                                'Transaction_Year': year_dir,
                                'Quarters': int(file.split('.')[0]),
                                'brand': dt['brand'],
                                'Transaction_Count': dt['count'],
                                'percentage': dt['percentage']
                            }
                            data_list.append(row_dict)
                        
    data = pd.DataFrame(data_list) 
    data = data.drop_duplicates()
    null_counts = data.isnull().sum()
    print(null_counts)
    return data


def data_aggregated_user_state(path='data/aggregated/user/country/india/state/'):
    data_list = [ ] 
    for d,i,f in os.walk(path):
        for file in f:
            if file.endswith('.json'):
                data_json = json.load(open(d+'/'+file))
                year_dir = int(re.sub('[^0-9]','',d))
                state_dir = d.split('\\')[-2].split('/')[-1]
                if data_json['data']['usersByDevice'] is not None:
                    for dt in data_json['data']['usersByDevice']:
                        row_dict = {
                            'States': state_dir,
                            'registeredUsers': data_json['data']['aggregated']['registeredUsers'],
                            'appOpens': data_json['data']['aggregated']['appOpens'],
                            'Transaction_Year': year_dir,
                            'Quarters': int(file.split('.')[0]),
                            'brand': dt['brand'],
                            'Transaction_Count': dt['count'],
                            'percentage': dt['percentage']
                        }
                        data_list.append(row_dict)

    data = pd.DataFrame(data_list)
    data = data.drop_duplicates()
    null_counts = data.isnull().sum()
    print(null_counts)
    return data


#%%

def data_map_transaction_total(path='data/map/transaction/hover/country/india/'):
    data_list = [ ] 
    for d,i,f in os.walk(path):
        if 'state' not in d:
            for file in f:
                if file.endswith('.json'):
                    data_json = json.load(open(d+'/'+file))
                    year_dir = int(re.sub('[^0-9]','',d))
                    for dt in data_json['data']['hoverDataList']:
                        row_dict = {
                            'States': dt['name'],
                            'Transaction_Year': year_dir,
                            'Quarters': int(file.split('.')[0]),
                            'Transaction_Type': dt['metric'][0]['type'],
                            'Transaction_Count': dt['metric'][0]['count'],
                            'Transaction_Amount': dt['metric'][0]['amount']
                        }
                        data_list.append(row_dict)                         
    data = pd.DataFrame(data_list) 
    data = data.drop_duplicates()
    null_counts = data.isnull().sum()
    print(null_counts)
    return data


def data_map_transaction_state(path='data/map/transaction/hover/country/india/state/'):
    data_list = [ ] 
    for d,i,f in os.walk(path):
        for file in f:
            if file.endswith('.json'):
                data_json = json.load(open(d+'/'+file))
                year_dir = int(re.sub('[^0-9]','',d))
                state_dir = d.split('\\')[-2].split('/')[-1]
                for dt in data_json['data']['hoverDataList']:
                    row_dict = {
                        'States': state_dir,
                        'District': dt['name'].replace(' district',''),
                        'Transaction_Year': year_dir,
                        'Quarters': int(file.split('.')[0]),
                        'Transaction_Type': dt['metric'][0]['type'],
                        'Transaction_Count': dt['metric'][0]['count'],
                        'Transaction_Amount': dt['metric'][0]['amount']
                    }
                    data_list.append(row_dict)   

    data = pd.DataFrame(data_list)
    data = data.drop_duplicates()
    null_counts = data.isnull().sum()
    print(null_counts)
    return data

#%%

def data_map_user_total(path='data/map/user/hover/country/india/'):
    data_list = [ ] 
    for d,i,f in os.walk(path):
        if 'state' not in d:
            for file in f:
                if file.endswith('.json'):
                    data_json = json.load(open(d+'/'+file))
                    year_dir = int(re.sub('[^0-9]','',d))
                    dd = data_json['data']['hoverData']
                    for dt in dd:
                        row_dict = {
                            'States': dt,
                            'registeredUsers': dd[dt]['registeredUsers'],
                            'appOpens': dd[dt]['appOpens'],
                            'Transaction_Year': year_dir,
                            'Quarters': int(file.split('.')[0]),
                        }
                        data_list.append(row_dict)
                        
    data = pd.DataFrame(data_list) 
    data = data.drop_duplicates()
    null_counts = data.isnull().sum()
    print(null_counts)
    return data


def data_map_user_state(path='data/map/user/hover/country/india/state/'):
    data_list = [ ] 
    for d,i,f in os.walk(path):
        for file in f:
            if file.endswith('.json'):
                data_json = json.load(open(d+'/'+file))
                year_dir = int(re.sub('[^0-9]','',d))
                state_dir = d.split('\\')[-2].split('/')[-1]
                dd = data_json['data']['hoverData']
                for dt in dd:
                    row_dict = {
                        'States': state_dir,
                        'District': dt.replace(' district',''),
                        'registeredUsers': dd[dt]['registeredUsers'],
                        'appOpens': dd[dt]['appOpens'],
                        'Transaction_Year': year_dir,
                        'Quarters': int(file.split('.')[0]),
                    }
                    data_list.append(row_dict)

    data = pd.DataFrame(data_list)
    data = data.drop_duplicates()
    null_counts = data.isnull().sum()
    print(null_counts)
    return data

#%%

def data_top_transaction_total(path='data/top/transaction/country/india/'):
    data_list = [ ] ;    data_list1 = [ ] ;    data_list2 = [ ] 
    for d,i,f in os.walk(path):
        if 'state' not in d:
            for file in f:
                if file.endswith('.json'):
                    data_json = json.load(open(d+'/'+file))
                    year_dir = int(re.sub('[^0-9]','',d))
                    for dt,pi,sta in zip(data_json['data']['districts'],
                                         data_json['data']['pincodes'],
                                         data_json['data']['states']):
                        row_dict = {
                            'District': dt['entityName'],
                            'Transaction_Year': year_dir,
                            'Quarters': int(file.split('.')[0]),
                            'Transaction_Type': dt['metric']['type'],
                            'Transaction_Count': dt['metric']['count'],
                            'Transaction_Amount': dt['metric']['amount']
                        }
                        data_list.append(row_dict)    
                        row_dict1 = {
                            'Pincodes': dt['entityName'],
                            'Transaction_Year': year_dir,
                            'Quarters': int(file.split('.')[0]),
                            'Transaction_Type': pi['metric']['type'],
                            'Transaction_Count': pi['metric']['count'],
                            'Transaction_Amount': pi['metric']['amount']
                        }
                        data_list1.append(row_dict1) 
                        row_dict2 = {
                            'States': sta['entityName'],
                            'Transaction_Year': year_dir,
                            'Quarters': int(file.split('.')[0]),
                            'Transaction_Type': sta['metric']['type'],
                            'Transaction_Count': sta['metric']['count'],
                            'Transaction_Amount': sta['metric']['amount']
                        }
                        data_list2.append(row_dict2) 
    data_dis = pd.DataFrame(data_list) 
    data_pi = pd.DataFrame(data_list1) 
    data_sta = pd.DataFrame(data_list2) 
    
    data_dis = data_dis.drop_duplicates()
    null_counts = data_dis.isnull().sum()
    print(null_counts)
    data_pi = data_pi.drop_duplicates()
    null_counts = data_pi.isnull().sum()
    print(null_counts)
    data_sta = data_sta.drop_duplicates()
    null_counts = data_sta.isnull().sum()
    print(null_counts)
    return data_dis,data_pi,data_sta


def data_top_transaction_state(path='data/top/transaction/country/india/state/'):
    data_list = [ ] ;    data_list1 = [ ] ;    data_list2 = [ ] 
    for d,i,f in os.walk(path):
        for file in f:
            if file.endswith('.json'):
                data_json = json.load(open(d+'/'+file))
                year_dir = int(re.sub('[^0-9]','',d))
                state_dir = d.split('\\')[-2].split('/')[-1]
                
                for dt,pi in zip(data_json['data']['districts'],
                                     data_json['data']['pincodes']):
                    row_dict = {
                        'States': state_dir,
                        'District': dt['entityName'],
                        'Transaction_Year': year_dir,
                        'Quarters': int(file.split('.')[0]),
                        'Transaction_Type': dt['metric']['type'],
                        'Transaction_Count': dt['metric']['count'],
                        'Transaction_Amount': dt['metric']['amount']
                    }
                    data_list.append(row_dict)    
                    row_dict1 = {
                        'States': state_dir,
                        'Pincodes': dt['entityName'],
                        'Transaction_Year': year_dir,
                        'Quarters': int(file.split('.')[0]),
                        'Transaction_Type': pi['metric']['type'],
                        'Transaction_Count': pi['metric']['count'],
                        'Transaction_Amount': pi['metric']['amount']
                    }
                    data_list1.append(row_dict1) 

    data_dis = pd.DataFrame(data_list) 
    data_pi = pd.DataFrame(data_list1)     
    
    data_dis = data_dis.drop_duplicates()
    null_counts = data_dis.isnull().sum()
    print(null_counts)
    data_pi = data_pi.drop_duplicates()
    null_counts = data_pi.isnull().sum()
    print(null_counts)
    
    return data_dis,data_pi


#%%

def data_top_user_total(path='data/top/user/country/india/'):
    data_list = [ ] ;    data_list1 = [ ] ;    data_list2 = [ ] 
    for d,i,f in os.walk(path):
        if 'state' not in d:
            for file in f:
                if file.endswith('.json'):
                    data_json = json.load(open(d+'/'+file))
                    year_dir = int(re.sub('[^0-9]','',d))
                    for dt,pi,sta in zip(data_json['data']['districts'],
                                         data_json['data']['pincodes'],
                                         data_json['data']['states']):
                        row_dict = {
                            'District': dt['name'],
                            'Transaction_Year': year_dir,
                            'Quarters': int(file.split('.')[0]),
                            'registeredUsers': dt['registeredUsers']
                        }
                        data_list.append(row_dict)    
                        row_dict1 = {
                            'Pincodes': pi['name'],
                            'Transaction_Year': year_dir,
                            'Quarters': int(file.split('.')[0]),
                            'registeredUsers': pi['registeredUsers']
                        }
                        data_list1.append(row_dict1) 
                        row_dict2 = {
                            'States': sta['name'],
                            'Transaction_Year': year_dir,
                            'Quarters': int(file.split('.')[0]),
                            'registeredUsers': sta['registeredUsers']
                        }
                        data_list2.append(row_dict2) 
    data_dis = pd.DataFrame(data_list) 
    data_pi = pd.DataFrame(data_list1) 
    data_sta = pd.DataFrame(data_list2) 
    
    data_dis = data_dis.drop_duplicates()
    null_counts = data_dis.isnull().sum()
    print(null_counts)
    data_pi = data_pi.drop_duplicates()
    null_counts = data_pi.isnull().sum()
    print(null_counts)
    data_sta = data_sta.drop_duplicates()
    null_counts = data_sta.isnull().sum()
    print(null_counts)
    
    return data_dis,data_pi,data_sta


def data_top_user_state(path='data/top/user/country/india/state/'):
    data_list = [ ] ;    data_list1 = [ ] ;    data_list2 = [ ] 
    for d,i,f in os.walk(path):
        for file in f:
            if file.endswith('.json'):
                data_json = json.load(open(d+'/'+file))
                year_dir = int(re.sub('[^0-9]','',d))
                state_dir = d.split('\\')[-2].split('/')[-1]
                for dt,pi in zip(data_json['data']['districts'],
                                     data_json['data']['pincodes']):
                    row_dict = {
                        'States': state_dir,
                        'District': dt['name'],
                        'Transaction_Year': year_dir,
                        'Quarters': int(file.split('.')[0]),
                        'registeredUsers': dt['registeredUsers']
                    }
                    data_list.append(row_dict)    
                    row_dict1 = {
                        'States': state_dir,
                        'Pincodes': dt['name'],
                        'Transaction_Year': year_dir,
                        'Quarters': int(file.split('.')[0]),
                        'registeredUsers': pi['registeredUsers']
                    }
                    data_list1.append(row_dict1) 

    data_dis = pd.DataFrame(data_list) 
    data_pi = pd.DataFrame(data_list1) 
    
    data_dis = data_dis.drop_duplicates()
    null_counts = data_dis.isnull().sum()
    print(null_counts)
    data_pi = data_pi.drop_duplicates()
    null_counts = data_pi.isnull().sum()
    print(null_counts)
    
    return data_dis,data_pi
    
#%%

if __name__ == "__main__":
    
    data1 = data_aggregated_transaction_total()
    data1.to_csv('Preprocessed Data/data_aggregated_transaction_total.csv',index=False)
    
    data2 = data_aggregated_transaction_state()
    data2.to_csv('Preprocessed Data/data_aggregated_transaction_state.csv',index=False)
    
    data3 = data_aggregated_user_total()
    data3.to_csv('Preprocessed Data/data_aggregated_user_total.csv',index=False)
    
    data4 = data_aggregated_user_state()
    data4.to_csv('Preprocessed Data/data_aggregated_user_state.csv',index=False)
    
    
    data5 = data_map_transaction_total()
    data5.to_csv('Preprocessed Data/data_map_transaction_total.csv',index=False)
    
    data6 = data_map_transaction_state()
    data6.to_csv('Preprocessed Data/data_map_transaction_state.csv',index=False)
    
    data7 = data_map_user_total()
    data7.to_csv('Preprocessed Data/data_map_user_total.csv',index=False)
    
    data8 = data_map_user_state()
    data8.to_csv('Preprocessed Data/data_map_user_state.csv',index=False)
    
    
    data_dis,data_pi,data_sta = data_top_transaction_total()
    data_dis.to_csv('Preprocessed Data/data_top_transaction_dis.csv',index=False)
    data_pi.to_csv('Preprocessed Data/data_top_transaction_pi.csv',index=False)
    data_sta.to_csv('Preprocessed Data/data_top_transaction_sta.csv',index=False)
    
    data_dis_sta,data_pi_sta = data_top_transaction_state()
    data_dis_sta.to_csv('Preprocessed Data/data_top_transaction_state_dis.csv',index=False)
    data_pi_sta.to_csv('Preprocessed Data/data_top_transaction_state_pi.csv',index=False)
    
    data_dis_user,data_pi_user,data_sta_user = data_top_user_total()
    data_dis_user.to_csv('Preprocessed Data/data_top_user_dis.csv',index=False)
    data_pi_user.to_csv('Preprocessed Data/data_top_user_pi.csv',index=False)
    data_sta_user.to_csv('Preprocessed Data/data_top_user_sta.csv',index=False)
    
    data_dis_top,data_pi_top = data_top_user_state()
    data_dis_top.to_csv('Preprocessed Data/data_top_user_state_dis.csv',index=False)
    data_pi_top.to_csv('Preprocessed Data/data_top_user_state_pi.csv',index=False)
    
    
    