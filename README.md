# Обрезка ссылок с помощью Битли

Данный скрипт создает сокращенную ссылку (битлинк) при помощи сервиса [Bitly](https://bitly.com) и подсчитывает количество переходов по битлинку.

### Как установить

1)Для запуска скрипта нужна учётная запись [Bitly](https://bitly.com) и токен (ключ) вида cba1232b3b4v3b2b3b3223bbvab3. 
Токен создается на странице с [настройками ](https://app.bitly.com/settings/api/) вашего профиля.
Его надо поместить в файл .env, находящийся в каталоге со скриптом. Токен записывается в файл следующим образом:

```
BITLY_TOKEN='cba1232b3b4v3b2b3b3223bbvab3'
```

2)Python3 должен быть уже установлен. 
3)Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).