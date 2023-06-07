# Restaurant Test Case

## Описание
Это тестовое задание, которое представляет из себя вэб-приложение, предоставляющее api для представления меню
ресторана.
Приложение имеет следующие сущности:
- Категория блюд (FoodCategory)
- Блюдо (Food)

## Стек
+ Python 3.10
+ Django 4.2
+ Django Rest Framework 3.14

## API
- '/api/v1/foods' - список категорий с блюдами. Из списка исключены категории, в которых нет ни одного блюда
или все блюда которых скрыты от публикации.

## Установка
1. Скопируйте проект: `git clone https://github.com/sergeytompson/restaurant_test_case`
2. Установите переменные окружения: удалите постфикс _sample у файла .env_sample, отредактируйте файл,
установив значение секретного ключа Django для переменной SECRET_KEY.
3. Запустите проект: `docker-compose up`

## Фикстуры
Для удобства ознакомления с проектом, при его запуске БД будет автоматически заполнена данными о нескольких
категориях и блюдах.

## Контакты
+ Telegram: @sergeytompson
+ Email: gfhfahfp@gmail.com