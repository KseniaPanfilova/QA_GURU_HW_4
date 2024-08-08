from selene import browser, be, have
import os


def test_student_reg_form():
    browser.open('/')
    browser.element('#firstName').should(be.blank).type('John')
    browser.element('#lastName').should(be.blank).type('Dou')
    browser.element('#userEmail').should(be.blank).type('JohnDou@test')
    browser.all('#genterWrapper label').should(have.texts('Male', 'Female', 'Other'))
    browser.all('#genterWrapper label').element_by(have.attribute('for', 'gender-radio-1')).click()
    browser.element('#userNumber').should(be.blank).type('1234567890')
    browser.element('.react-datepicker-wrapper').click().element('#dateOfBirthInput').should(be.not_.blank)
    browser.element('.react-datepicker__tab-loop').element('.react-datepicker__month-select').click().element(
        '[value = "3"]').click()
    browser.element('.react-datepicker__tab-loop').element('.react-datepicker__year-select').click().element(
        '[value = "1985"]').click()
    browser.all('.react-datepicker__month .react-datepicker__day').element_by(have.exact_text('13')).click()
    browser.element('#subjectsInput').type('M')
    browser.element('#react-select-2-option-0').click()
    browser.all('#hobbiesWrapper .custom-control-label').should(have.texts('Sports', 'Reading', 'Music'))
    browser.all('#hobbiesWrapper .custom-control-label').element_by(have.attribute('for', 'hobbies-checkbox-1')).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('photo.jpg'))
    browser.element('#currentAddress').type('Some Street, some house')
    browser.element('#state').click().element('#react-select-3-option-1').click()
    browser.element('#city').click().element('#react-select-4-option-1').click()
    browser.element('#submit').click()
