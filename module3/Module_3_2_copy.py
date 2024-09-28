#Задача "Рассылка писем":
print("Задача 'Рассылка писем'")
print()
def send_email(message, recipient, sender = "university.help@gmail.com"):
    if "@" not in recipient or "@" not in sender or \
        not sender.endswith((".com", ".ru" ,".net")) or not recipient.endswith((".com", ".ru" ,".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")




send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


# , ".com", ".ru", ".net" , sender



# if  in send_email(recipient) or
#     print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
#сли же sender и recipient совпадают

# if send_email(recipient) == send_email(sender):
#     print("Нельзя отправить письмо самому себе!")


#Вопросы
# lогика постановки * для именованных аргументов, все и так выполняется
# and и or в условиях имен писем


