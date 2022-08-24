from Automation_testing_final_task_stepik import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                             # открываем страницу
    page.go_to_login_page()                 # выполняем метод страницы — переходим на страницу логина