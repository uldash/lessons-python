import random as rnd

answers = [
    'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать',
    'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Бесспорно',
    'Предрешено', 'Никаких сомнений', 'Определённо да',
    'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего',
    'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Даже не думай',
    'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие',
    'Весьма сомнительно'
]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как твое имя? ').capitalize()
print(f'Привет {name}')

while True:
    print(
        f'{name} мысленно загадай вопрос, на который хочешь получить ответ и нажми Enter'
    )
    input()
    print(rnd.choice(answers))
    if input(f'Имеешь ли ты {name} еще вопросы (y/n) ').lower() == 'n':
        break
print('Возвращайся если возникнут вопросы!')
