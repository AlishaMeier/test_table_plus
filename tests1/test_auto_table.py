from selene.support.conditions import have, be
from selene.support.shared import browser


first_name = 'Alisha'
last_name = 'Meier'
email = 'aa@mail.ru'
age = 26
salary = 60000
department = 'QA'

first_name_e = 'Elma'
last_name_e = 'Jambo'
email_e = 'bb@mail.ru'
age_e = 30
salary_e = 200000
department_e = 'PM'


def test_create_new(window_expect_size):
    browser.element('#addNewRecordButton').click()
    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)
    browser.element('#userEmail').type(email)
    browser.element('#age').type(age)
    browser.element('#salary').type(salary)
    browser.element('#department').type(department)
    browser.element('#submit').double_click()
# now check 1
    browser.element('.rt-table').should(have.text(first_name))
    browser.element('.rt-table').should(have.text(last_name))
    browser.element('.rt-table').should(have.text(email))
    browser.element('.rt-table').should(have.text('26'))
    browser.element('.rt-table').should(have.text('60000'))
    browser.element('.rt-table').should(have.text(department))

def test_edit(window_expect_size):
    browser.element('#edit-record-2').click()
    browser.element('#firstName').clear().type(first_name_e)
    browser.element('#lastName').clear().type(last_name_e)
    browser.element('#userEmail').clear().type(email_e)
    browser.element('#age').clear().type(age_e)
    browser.element('#salary').clear().type(salary_e)
    browser.element('#department').clear().type(department_e)
    browser.element('#submit').double_click()

# now check 2
    browser.element('.rt-table').should(have.text(first_name_e))
    browser.element('.rt-table').should(have.text(last_name_e))
    browser.element('.rt-table').should(have.text(email_e))
    browser.element('.rt-table').should(have.text('30'))
    browser.element('.rt-table').should(have.text('20000'))
    browser.element('.rt-table').should(have.text(department_e))


def test_delete(window_expect_size):
    browser.element('#delete-record-3').click()
#now check 3
    browser.element('.rt-table').should(have.no.text('Kierra'))
    browser.element('.rt-table').should(have.no.text("Gentry"))
    browser.element('.rt-table').should(have.no.text('kierra@example.com'))
    browser.element('.rt-table').should(have.no.value('20'))
    browser.element('.rt-table').should(have.no.value('2000'))
    browser.element('.rt-table').should(have.no.text('Legal'))