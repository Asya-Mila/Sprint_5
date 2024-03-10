from selenium import webdriver
import time

# инициализируем драйвер браузера
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")



# страница логинации
# https://stellarburgers.nomoreparties.site/login

# Регистрация
# Проверь:
# Успешную регистрацию.
# 1 Поле «Имя» должно быть не пустым;
# 2 в поле Email введён email в формате логин@домен: например, 123@ya.ru.
# 3 Минимальный пароль — шесть символов.
# 4 Ошибку для некорректного пароля.


# закроем браузер
driver.quit()