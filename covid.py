alert = input('是否維持三級警戒(Y/N)：')
if alert == 'Y':
    print('禁止室內5人、戶外10人以上群聚')
    print('餐廳禁止內用')
    print('戶外全面配戴口罩')
else:
    print('禁止室內100人、戶外500人以上活動')
    print('餐廳內用採梅花座')
    print('乘坐大眾運輸必須配戴口罩')