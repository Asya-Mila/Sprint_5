# Проект автоматизации тестирования сайт заказов "stellar burgers"
# Ссылка на проект https://stellarburgers.nomoreparties.site

1. Основа для написания автотестов — фреймворк pytest.
2. Установить зависимости — pip install -r requirements.txt.
3. Команда для запуска — pytest -v.

Тесты:
1. Регистрация
1.1. Успешная регистрацию. Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен: например, 123@ya.ru. Минимальный пароль — шесть символов.
1.2. Ошибку для некорректного пароля
пш
2. Вход
2.1. вход по кнопке «Войти в аккаунт» на главной
2.2. вход через кнопку «Личный кабинет»
2.3. вход через кнопку в форме регистрации
2.4. вход через кнопку в форме восстановления пароля

3. Переходы по страницам
3.1. Переход по клику на «Личный кабинет».
3.2. Переход по клику на «Конструктор» и на логотип Stellar Burgers.
3.3. Выход по кнопке «Выйти» в личном кабинете.

4. Проверка переходов в разделе «Конструктор»
4.1. «Булки»
4.2. «Соусы»
4.3. «Начинки»