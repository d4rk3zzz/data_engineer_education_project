#TASK 1
#
# item_name = "ноутбук"
# price = 1200.50
# tax_rate = 0.2
#
# total_price = price + price * tax_rate
# print(f'Товар {item_name} стоит {total_price} после оплаты налога')
#
# #TASK 2
#
# server_info = {
#     "id": "srv-99",
#     "status": "maintenance",
#     "ip": "192.168.1.1",
#     "hardware": {
#         "cpu": "8 cores",
#         "ram": "32GB"
#     },
#     "tags": ["production", "east-cluster"]
# }
#
# print(server_info.get("hardware").get("ram"), server_info.get("tags")[-1])
#
#
# TASK 2.1
# raw_name = " иван иванович ИВАНОВ "
# name = raw_name.strip().upper()
#
# print(name)
#
#TASK 2.2
# tools = ["Python", "SQL", "Excel"]
# tools.remove("Excel")
# tools.append("Tableau")
# tools.append("Airflow")
# tools.remove("SQL")
#
# print(tools)
#
#
# TASK 2.3
# parts = ["2023-10-01", "ERROR", "Database connection failed"]
# log = " | ".join(parts)
# print(log)
#
#
# TASK 2.4
# base_info = {"id": 1, "name": "Alex"}
# extra_info = {"email": "alex@mail.com", "city": "Moscow"}
# full_profile = base_info
# for i in extra_info.keys():
#     full_profile[i] = extra_info.get(i)
#
# print(full_profile)
#
#
# TASK 2.5
#
# tags_str = "python,data,sql,spark"
# tags_list = tags_str.split(",")
#
# print(len(tags_list))
#
#
# TASK 3
#
# password = str(input("Введите пароль: "))
#
# if len(password) >= 8 and "@" in password:
#     print("Strong")
# elif len(password) >= 8:
#     print("Medium")
# else:
#     print("Weak")
#
#
# TASK 4
# sentence = str(input("Введите предложение: "))
#
# l_sentence = sentence.split(" ")
# l_sentence = l_sentence[::-1]
#
# l_sentence2 = "_".join(l_sentence)
#
# print(l_sentence2)
#
#
# TASK 5
#
# db = {
#     "id0001": 2500,
#     "id0002": 3200,
#     "id0003": 2400
# }
#
# str_id = "id" + str(input("Введите ID: "))
#
# if str_id in db.keys():
#     print(db.get(str_id))
# else:
#     print("User not found")
#
#
# TASK 6
# # logs = ["INFO", "ERROR", "INFO", "DEBUG", "ERROR", "WARNING"]
#
# errors_list = []
#
# for i in logs:
#     if i == "ERROR":
#         errors_list.append(i)
#
# print(errors_list)
#
#
# TASK 7
# transactions = [100, 250, 50, 500]
# sum_trans = 0
#
# for i in transactions:
#     sum_trans += i
#
# print(sum_trans)
# TASK 8
#
# count = 0
#
# while str(input("Введите слово:")) != "stop":
#     count += 1
#
# print(count)
# TASK 9
#
# raw_ids = [" 101 ", "id102", "103", "ID104", " 105", "stop_user", "106 "]
# clean_ids = []
#
# for i in raw_ids:
#     clean_id = i.strip().replace("id", "").replace("ID", "").replace("Id", "").replace("iD", "")
#     if "stop" not in clean_id:
#         clean_ids.append(clean_id)
#
# print(clean_ids)
#
#
# TASK 10
#
# data = [10, 50, 100, 2, 85, 9, 110, 3, 45]
# mx = data[0]
# mn = data[0]
#
# for i in data:
#     if mx <= i:
#         mx = i
#     if mn >= i:
#         mn = i
#
#
# print(mx, mn)
#
#
# TASK 11
#
# def convert_price(amount, currency):
#     if currency == "USD":
#         return amount * 90
#     elif currency == "EUR":
#         return amount * 100
#     else:
#         return amount
#
# print(convert_price(100, "EUR"))