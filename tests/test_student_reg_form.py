import os
from selene import browser, be, have


def test_student_reg_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').should(be.blank).type('John')
    browser.element('#lastName').should(be.blank).type('Dou')
    browser.element('#userEmail').should(be.blank).type('JohnDou@test.com')
    browser.element('[name=gender][value=Male]+label').click()
    browser.element('#userNumber').should(be.blank).type('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('[value = "3"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value = "1985"]').click()
    browser.element(f'.react-datepicker__day--0{13}').click()
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    browser.element('#subjectsInput').type('Maths').press_enter()

    browser.all('#hobbiesWrapper .custom-control-label').element_by(
        have.attribute('for', 'hobbies-checkbox-1')).click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('photo.jpg'))  # плохой вариант, не будет работать, если

    browser.element('#currentAddress').type('Some Street, some house')

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Uttar Pradesh')).click()

    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Lucknow')).click()

    browser.element('#submit').click()

    browser.element('.table').all('td').should(have.texts(
        'Student Name', 'John Dou',
        'Student Email', 'JohnDou@test.com',
        'Gender', 'Male',
        'Mobile', '1234567890',
        'Date of Birth', '13 April,1985',
        'Subjects', 'Maths',
        'Hobbies', 'Sports',
        'Picture', 'photo.jpg',
        'Address', 'Some Street, some house',
        'State and City', 'Uttar Pradesh Lucknow'
    )
    )

    browser.element('#closeLargeModal').click()
    browser.element('#example-modal-sizes-title-lg').should(be.not_.visible)
