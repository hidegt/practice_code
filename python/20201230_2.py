import datetime
d_today = datetime.date.today()
week_d = d_today.weekday()

day = ["月","火","水","木","金","土","日"]

print('今日から何日後の曜日を調べますか？')
ans = input('数字を入力してください:  ')

n = week_d + int(ans) % 7
if n > len(day):
   n %= 7

td = datetime.timedelta(days=int(ans))
print(d_today + td)
print(day[n] + '曜日')