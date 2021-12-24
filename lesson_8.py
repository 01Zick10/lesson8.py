# 1 
# while True: 
#     symbol = input("Enter a number: ") 
#     if symbol.isnumeric() is True: 
#         break 
 
 
# 2 
# file = open("data.txt", "rt") 
# data = file.read() 
# words = data.split() 
# 
# print('Number of words in text file :', len(words)) 
 
 
# 3 
# a = open('12.png.jpg', 'br') 
# b = open('123.png', 'wb') 
# for x in a: 
#     b.write(x) 
# a.close() 
# b.close() 
 
# 4 
# print('ДИСКЛЕЙМЕР!' 
#       'Этот эксперемент выполнен профессионалами.В домашних условиях не повторять,' 
#       '\n а так же ни при каких обстоятельствах. Слабонервным не смотреть' 
#       '\n В последующих сценах ни один Жасур не грохнул Фареса... Наверное' 
#       '\n Ну а если вы готовы, то приятного просмотра' 
#       '\n') 
# print( 
#     ' 1.Просмотр баланса \n 2.Внесение денег \n 3.Обналичивание денег \n 4.Оплата по реквезитам \n 0.Завершить оперпцию') 
# 
# data = "" 
# balance = 0 
# account = {'balance': 0} 
# 
# 
# def check(data): 
#     a = open("test.txt", "w", encoding='UTF-8') 
#     a.write(data) 
#     a.close() 
# 
# 
# def replenishment_balance(): 
#     global data 
#     deposit = int(input('Введите сумму: ')) 
#     komissiya = deposit * 0.01 
#     deposit -= komissiya 
#     account['balance'] += deposit 
# 
# 
#     print(f'\n Поздравляю тебя. Больше Жасур не отимеет твой кошелёк, ведь ты пользуешься банкоматом от Фареса так что это сделаю я' 
#           f'\n Я одарю твою карту, прямо как боженька. На целых {int(deposit)}$.' 
#           f'\n Ты спросишь а где ещё деньги, а я отвечу, что у меня в кармане') 
#     data += "Внесение суммы " + str(deposit) + ". Комиссия " + str(komissiya) + "\n" 
#     check(data=f'На вашу банковскую карту добавлено {int(deposit)}$' 
#                f'\n Спасибо что выбрали банкомат сделанный Фаресом.' 
#                f'\n Теперь Жасур будет сидеть в печали т.к теперь он не будет иметь проценты с моего банкомата ') 
# 
# 
# def output_money(): 
#     global data 
#     output = int(input('Введите сумму: ')) 
#     komissiya = output * 0.01 
#     output += komissiya 
#     account['balance'] -= output 
#     print(f'Шахриёр. Может хватит опусташать кошельки? Как вы за секунду потратили{int(output)}$?!') 
#     data += "Обналичивание суммы " + str(output) + "Комиссия " + str(komissiya) + "\n" 
#     check(data=f'С вашей раты списаны средства в размере {int(output)}$' 
#                f'\n Спасибо что выбрали банкомат сделанный Фаресом.' 
#                f'\n Удачи.И хорошего для меня дня). НУ так уш и быть. Для вас тоже') 
# 
# 
# def transfer_money(): 
#     global data 
#     credit_card = int(input('Введите реквезиты карты: ')) 
#     transfer_amount = int(input('Введите сумму для перевода: ')) 
#     komissiya = transfer_amount * 0.01 
#     transfer_amount += komissiya 
#     account['balance'] -= transfer_amount 
#     print(f'Вы перевели {int(transfer_amount)}$ по этим реквезитам -> {int(credit_card)} ' 
#           f'\n О нет! Кажется Жасур учуил добычу и выходит на охоту') 
#     data += "Перевод по реквезитам " + str(transfer_amount) + "Комиссия " + str(komissiya) + "\n" 
#     check(data=f'Первод на сумму {int(transfer_amount)}$ по этим реквезитам-> {int(credit_card)} выполнен успешно.' 
#                f'\n Я уже чувствую что Жасур меня грохнет после увиденного') 
# 
# 
# 
# while 1: 
#     a = int(input(': ')) 
# 
#     if a == 1: 
#         print(account) 
#     elif a == 2: 
#         replenishment_balance() 
#     elif a == 3: 
#         output_money() 
#     elif a == 4: 
#         transfer_money() 
#     elif a == 0: 
#         print('Спасибо, что перед моей смертью вы воспользовались моим банкоматом. Удачи вам') 
#         break 
 
 
#5 
# try: 
#     list = [] 
# 
#     user_input = int(input('Number: ')) 
#     list.append(user_input) 
#     print(list) 
# 
# except ValueError: 
#     print('Скажи ка мне: как ты до такой жизни докатился?')


#6 
# try: 
# 
#     number1 = int(input('По братски не напрягай меня. Просто впиши число. Я даже для тебя стрелочку сделал -> ')) 
#     number2 = int(input('Здесь тоже не тормози -> ')) 
#     print(number1/number2) 
# 
# except ZeroDivisionError: 
#     print('Слушай. А ты в каком классе? Всмычле уже школу закончил?! Так как ты не знаешь, что на 0 делить нельзя?')


#P.S Шахриёр. У меня проблемы с созданием ролика на платформу YOUTUBE, т.к у меня нет своего компьютера или ноутбука. Могу ли я вам в лицо рассказать о своём проекте?
