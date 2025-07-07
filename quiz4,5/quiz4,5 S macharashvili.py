import sqlite3


conn = sqlite3.connect('stranger_things_database.sqlite3')
c = conn.cursor()

# 3
# პირველი სეზონის სერიები

# c.execute("SELECT * FROM episodes")
# Firstseason = c.fetchmany(8)
# for F1 in Firstseason:
#     print(F1)
#


#4
# ამ ფუნქციას შეუძლია მომხმარებველს შემოატანინოს ახალი ეპიზოდის სახელები.

#
# def Uinput_episode():
#     print('ახალი ეპიზოდის სათაურის დამატება')
#     newEpisode = str(input('შეიყვანეთ ახალი ეპიზოდი, გემუდრებით:( : '))
#     newSeason = str(input('შეიყვანე ახალი სეზონი'))
#
#     c.execute ("INSERT INTO episodes (season, title) VALUES (?, ?)",
#               (newSeason, newEpisode))
#
#
#     conn.commit()
#     print("ინფორმაცია წარმატებით დაემატა ბაზაში.")
#
#
# Uinput_episode()

# N5
# ეს კოდი ააპდეითებს პროგრამას
#
# def UpdateInfo():
#     freshName = str(input('გთხოვთ შეცვალეთ ეპიზოდის სახელი'))
#     freshSeason = str(input('გთხოვთ შეცვალოთ სეზონი'))
#
#
#
#     c.execute('''
#            UPDATE episodes
#            SET title=?
#            WHERE season=? AND title=?
#        ''', (freshSeason, freshName))
#
#     conn.commit()
#     print("მონაცემები წარმატებით განახლდა.")
#
# UpdateInfo()

# 7
# დიაგრამა ირველი და მეორე ეპიზოდის შფარდება
import matplotlib.pyplot as plt
labels= 'სეზონი1','სეზონი2'
sizes=[8, 9]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels , autopct='%1.1f%%',startangle=90)
plt.show()


labels='სეზონი1','სეზონი3'
sizes=[8, 8]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels , autopct='%1.1f%%',startangle=90)
plt.show()



labels='სეზონი 1',"სეზონი 4"
sizes=[8, 9]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels , autopct='%1.1f%%',startangle=90)
plt.show()
(conn.close())
