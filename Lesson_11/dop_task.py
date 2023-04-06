# Задача 2. Робота з файлами через map.
#
# В директорії titanic_data ви можете знайти файл titanic_data.csv.
#
# Напишіть програму, що видаляє другу колонку з цієї таблиці та зберігає оновлену таблицю
# у файл titanic_data_1.csv.
#
# Бажано використовувати map для якомога більшої долі операцій.
#
# Hint: ви можете зробити за допомогою map все, окрім власне роботи з файлами

# import csv
# with open('titanic_data.csv', 'r') as input_file, open('titanic_data_1.csv', 'w', newline='') as output_file:
#     reader = csv.reader(input_file)
#     writer = csv.writer(output_file)
#
#     for row in map(lambda x: [x[0], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11]], reader):
#         writer.writerow(row)

# без використання "import csv"
with open('titanic_data.csv', 'r') as input_file, open('titanic_data_2.csv', 'w') as output_file:
    output_lines = map(lambda line: ','.join(line.split(',')[0:1] + line.split(',')[2:]), input_file.readlines())

    output_file.writelines(output_lines)


