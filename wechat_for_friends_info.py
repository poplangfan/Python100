# -*- coding: utf-8 -*-
# 统计好友的男女比例
import itchat
import matplotlib.pyplot as plt
from pandas import DataFrame

itchat.auto_login()
friends = itchat.get_friends(update=True)[:]
total = len(friends) - 1
male = female = other = 0
for friend in friends[1:]:
    print(friend)
    sex = friend["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
print("男性好友：%.2f%%" % (float(male) / total * 100))
print("女性好友：%.2f%%" % (float(female) / total * 100))
print("其他：%.2f%%" % (float(other) / total * 100))
# labels = ['man', 'female', 'unknow']
# X = [male, female, other]
# fig = plt.figure()
# plt.pie(X, labels=labels, autopct='%1.2f%%')  # 画饼图（数据，数据对应的标签，百分数保留两位小数点）
# plt.title("Pie chart")
# plt.show()
# plt.savefig("PieChart.jpg")


# 提取好友的昵称，性别，省份，城市，个性签名（按需求）并存在CSV文件里
def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable


NickName = get_var("NickName")
Sex = get_var('Sex')
Province = get_var('Province')
City = get_var('City')
Signature = get_var('Signature')
data = {'NickName': NickName, 'Sex': Sex, 'Province': Province,
        'City': City, 'Signature': Signature}
frame = DataFrame(data)
frame.to_csv('data.csv', index=True)
