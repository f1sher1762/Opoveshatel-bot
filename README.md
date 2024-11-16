# Бот для уведомлений о дежурных

Этот бот предназначен для уведомления о текущем и следующем дежурном в корпоративном чате или приватном чате. Бот проверяет текущую дату и выводит информацию о человеке, который отвечает за дежурство на текущей и следующей неделе.

## Функциональность

- **Дежурный на текущей неделе**: Бот сообщает, кто из сотрудников дежурит на текущей неделе.
- **Дежурный на следующей неделе**: Также предоставляется информация о человеке, который будет дежурить на следующей неделе.
- **Ссылки на корпоративные чаты**: Для каждого дежурного предоставляется ссылка на его профиль в корпоративном мессенджере (например, Telegram).
- **Приватный и групповой чаты**: Бот может работать как в приватных, так и в групповых чатах.

## Установка

1. установить необходимые библиотеки:
    ```bash
    pip install python-telegram-bot
    ```

2. скачать и сохраните файл с кодом.

3. внести свои переменные, вместо прочерка:
    - **chat_id**: Замените на ID чата.
    - **duty_schedule**: ставим фамилии в той последовательности, в которой будет дежурство.
    - **corporate_links**: ссылка на телегу сотрудника.

4. токен бота:
    ```python
    updater = Updater("ХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХ", use_context=True)
    ```

## как  это работает

- Бот отслеживает текстовые сообщения в чатах.
- далее если в сообщении встречается слово "дежурн", или подобное(коренное) ему, то бот отвечает с информацией о текущем и следующем дежурном.
- В приватных чатах бот отправляет сообщения пользователю.  
## Пример работы

1. в приватном чате:

    - Бот ответит с именем текущего дежурного и ссылкой на его профиль.
    - Также будет указано имя и ссылка на дежурного следующей недели.

2. в группах:

    - Бот отправит сообщение в указанный чат, оповещая всех участников о текущем и следующем дежурном.

# примечания

- Бот работает с библиотекой `python-telegram-bot` и использует `polling` для получения сообщений.
- Убедитесь, что у вас есть доступ к API Telegram и токен бота для корректной работы.

---
разработал для автоматизации оповещений о дежурных. не возникает повисшего в тишине вопроса, уведомляет автоматически 24/7, пока решается возможность дежурным самим менять последовательность, в случае ЧП