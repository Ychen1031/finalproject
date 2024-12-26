import datetime
import os

postback_data = {'方式': 'meal', 'price': 100, '詳情': '蛋炒飯'}

income_types = {
    'salary': '薪資',
    'bonus': '獎金',
    'invest': '投資'
}

if '方式' in postback_data and postback_data['方式'] in income_types:
    print(f"{income_types[postback_data['方式']]}為{postback_data['price']}元\n細項: {postback_data['詳情']}")