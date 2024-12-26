postback_data = {'方式': 'meal', 'price': 100, '詳情': '蛋炒飯'}

# 定義方式對應的描述
方式描述 = {
    'salary': '薪資為',
    'bonus': '獎金為',
    'invest': '投資為'
}

# 檢查 '方式' 是否在字典中
方式 = postback_data.get('方式')
if 方式 in 方式描述:
    print(f"{方式描述[方式]}{postback_data['price']}元\n細項: {postback_data['詳情']}")
else:
    print("未知的方式")
