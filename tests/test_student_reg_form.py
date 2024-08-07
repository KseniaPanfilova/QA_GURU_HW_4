from selene import browser, be, have


def test_student_reg_form():
    browser.open('/')
    browser.element('#firstName').should(be.blank).type('John')
    browser.element('#lastName').should(be.blank).type('Dou')
    browser.element('#userEmail').should(be.blank).type('JohnDou@test')
    # browser.all('[name = "gender"]').element_by(have.value("Male")).element('.custom-control-label').click()
    # browser.element('[for = "gender-radio-1"]').click()
    browser.all('#genterWrapper label').should(have.texts('Male', 'Female', 'Other'))
    browser.all('#genterWrapper label').element_by(have.attribute('for', 'gender-radio-1')).click()
    browser.element('#userNumber').should(be.blank).type('1234567890')
    browser.element('.react-datepicker-wrapper').click()
    # browser.element('.react-datepicker__year-select').element()
