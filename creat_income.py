import datetime
import os

postback_data = {'方式': 'meal', 'price': 100, '詳情': '蛋炒飯'}

if '方式' in postback_data:
    if postback_data['方式'] == 'salary':
        print('薪資為' + str(postback_data['price']) + '元' + '\n' + '細項: ' + postback_data['詳情'])
    elif postback_data['方式'] == 'bonus':
        print('獎金為' + str(postback_data['price']) + '元' + '\n' + '細項: ' + postback_data['詳情'])
    elif postback_data['方式'] == 'invest':
        print('投資為' + str(postback_data['price']) + '元' + '\n' + '細項: ' + postback_data['詳情'])