import csv
import os
import random
import filecmp 
def read(filename):
    fd = open(filename, "r")
    reader = csv.reader(fd, delimiter="\t")
    for row in reader:
        print(row)
    fd.close()
    print("зчитування файлу виконано")
def write(filename):
    fd = open(filename, "w")
    for i in range(5):
        A = i*16
        fd.write("%i\t%.1f\n" % (i, A))
    fd.close()
    print("запис файлу виконано")
def append(filename): 
    fd = open(filename, "a")
    for i in range(5):
        A = random.randint(30,40)
        fd.write("%i\t%.1f\n" % (i, A))
    fd.close()
    print("дозапис у кінець файлу виконано") 
def rename(filename):
    os.rename("E:\ICS-\Lab-5\mydirectorya.txt", "E:\ICS-\Lab-5\directorya.txt") 
    print("Перейменування файлу завершено")
def bust(filename):
    for filename in os.listdir("E:\ICS-\Lab-5"):
      print(filename)  
    print("перебір файлів в каталозі завершено") 
def comparison(filename):
    similar = filecmp.cmp("E:\ICS-\Lab-5\mydirectorya.txt", "E:\ICS-\Lab-5\directorya.txt") 
    print(similar) 
    print("Порівняння файлів завершено")
filename = "mydirectorya.txt"
x=int(input("виберіть режим роботи з файлом: 1 - читати з файлу 2 - записати у файл 3 - дозапис у файл 4 - Перейменування файлу 5 - перебір файлів в каталозі 6 - Порівняння файлів" ))          

mode=' '
if x==1:
    read(filename)
elif x==2:
    write(filename)
elif x==3:
    append(filename)    
elif x==4:
    rename(filename)
elif x==5:
    bust(filename)
elif x==6:
    comparison(filename)
else:
    print("Такого вибору немає")