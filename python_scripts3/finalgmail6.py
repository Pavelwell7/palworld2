import smtplib

import os
from dotenv import load_dotenv

load_dotenv()

sender = os.getenv('sender')
password = os.getenv('password')

in_fitation = "Золотой билет"
email_from = "pavel.palpatinov@yandex.ru"
email_to = "pavel.palpatinov@yandex.ru"
friend_name = "Суба"
my_name = "Павел Бугаёв"
web_site = "https://dvmn.org/profession-ref-program/pavelbugaev303/DBszV/"
let_ter = """\
From: {email_from}
To: {email_to}
Subject: {in_fitation}
Content-Type: text/plain; charset="UTF-8";

Привет, {friend_name}! {my_name} приглашает вас на сайт {web_site}!

{web_site} — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачу. Получаем отзывы от преподавателей.

Как будет проходить ваше обучение на {web_site}?

→ Попрактикуешься на своих кейсах.
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей.
Задачи не «сгорят» и не уйдут в раунд. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решения наших задач — можно ссылаться на твоём GitHub. Работодатели такое оценят.

Регистрируйся → {web_site}  
На курсы, которые еще не вышли, можно подписаться и получить о релизе сразу на имейл.""".format(in_fitation=in_fitation,email_from=email_from,email_to=email_to,friend_name=friend_name,my_name=my_name,web_site=web_site)

let_ter = let_ter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465) 
email_from = "pavel.palpatinov@yandex.ru"
email_to = "pavel.palpatinov@yandex.ru"
server.login(sender, password)
server.sendmail(email_from, email_to, let_ter)
server.quit()
