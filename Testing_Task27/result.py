(.venv) PS C:\Users\jagap\PycharmProjects\Testing_Task27> pytest
=============================================================== test session starts ================================================================
platform win32 -- Python 3.12.3, pytest-8.2.0, pluggy-1.5.0
rootdir: C:\Users\jagap\PycharmProjects\Testing_Task27
collected 1 item

Test_cases\test_Loginpage.py F                                                                                                                [100%]

===================================================================== FAILURES =====================================================================
____________________________________________________________ Test_loginPage.test_login _____________________________________________________________

self = <Test_cases.test_Loginpage.Test_loginPage object at 0x000001C13C5F11C0>

    def test_login(self):
        try:
            # Username = 2
            # Password = 3
            # Test Results = 7
            # Row = 2 to End

            for row in range(2, data.Webdata().rowCount()+1):
                username = data.Webdata().readData(row, 2)
                password = data.Webdata().readData(row, 3)
>               self.enterText(locator.Weblocator().usernameLocator, username)

Test_cases\test_Loginpage.py:45:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <Test_cases.test_Loginpage.Test_loginPage object at 0x000001C13C5F11C0>
locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input', textvalue = 'Admin'

    def enterText(self, locator, textvalue):
>       self.wait.until(ec.presence_of_element_located((By.XPATH, locator))).send_keys(textvalue)
E       AttributeError: 'Test_loginPage' object has no attribute 'wait'

Test_cases\test_Loginpage.py:28: AttributeError
================================================================= warnings summary =================================================================
Test_cases/test_Loginpage.py::Test_loginPage::test_login
Test_cases/test_Loginpage.py::Test_loginPage::test_login
Test_cases/test_Loginpage.py::Test_loginPage::test_login
Test_cases/test_Loginpage.py::Test_loginPage::test_login
Test_cases/test_Loginpage.py::Test_loginPage::test_login
Test_cases/test_Loginpage.py::Test_loginPage::test_login
  C:\Users\jagap\PycharmProjects\Testing_Task27\.venv\Lib\site-packages\openpyxl\packaging\core.py:99: DeprecationWarning: datetime.datetime.utcnow()
 is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    now = datetime.datetime.utcnow()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
============================================================= short test summary info ==============================================================
FAILED Test_cases/test_Loginpage.py::Test_loginPage::test_login - AttributeError: 'Test_loginPage' object has no attribute 'wait'