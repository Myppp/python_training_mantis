class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_xpath("//body/div[@id='main-container']/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/form[1]/fieldset[1]/input[2]").click()
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//span[contains(text(),'Доступ к этой сессии будет только с данного IP-адр')]").click
        wd.find_element_by_xpath("//body/div[@id='main-container']/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/form[1]/fieldset[1]/input[3]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//body/div[@id='navbar']/div[@id='navbar-container']/div[2]/ul[1]/li[3]/a[1]").click
        wd.find_element_by_link_text("Выход").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Выход")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logget_user() == username

    def get_logget_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//a[contains(text(),'administrator')]").text

    def ensure_login(self, username, password):
        self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)