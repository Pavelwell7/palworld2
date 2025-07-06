infitation = "Золотой билет!"
email_from = "pavel.palpatinov@yandex.by"
email_to= "pascha.bugayov@yandex.by"
friend_name = "Суба"
my_name = "Павел Бугаёв"
website = "https://dvmn.org/profession-ref-program/pavelbugaev303/DBszV/"
letter = """\
From: {email_from}
To: {email_to}
Subject: {infitation}
Content-Type: text/plain; charset="UTF-8";

Привет, {friend_name}! {my_name} приглашает вас на сайт {website}!

{website} — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачу. Получаем отзывы от преподавателей.

Как будет проходить ваше обучение на {website}?

→ Попрактикуешься на своих кейсах.
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей.
Задачи не «сгорят» и не уйдут в раунд. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решения наших задач — можно ссылаться на твоём GitHub. Работодатели такое оценят.

Регистрируйся → {website}  
На курсы, которые еще не вышли, можно подписаться и получить о релизе сразу на имейл.""".format(infitation=infitation,email_from=email_from,email_to=email_to,friend_name=friend_name,my_name=my_name,website=website)

letter = letter.encode("UTF-8")

print(letter)
