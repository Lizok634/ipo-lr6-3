num=int(input("Введите количество строк "))#пользователь вводит кодичество строк
spisok=[]#создаем пустой список
text=[]#создаем еще один список
for i in range(num):#перебираем числа от 0 до числа равного количеству строк
    spisok.append (input("Введите строчку "))#добавляем строку ,введенную пользователем, в список 
for stroka in spisok:#перебираем каждую строку в списке
    text+=stroka.split()# разделяем по пробелам и добавляем к списку text каждое слово
print(spisok)#выводим сам список
print(text)#выводим все слова в списке
text=set(text)#делаем из списка множество
print(len(text))#выводим количество разных слов в списке
