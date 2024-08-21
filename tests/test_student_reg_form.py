from selene import browser, be, have
import os


def test_student_reg_form():
    browser.open('/')

    browser.element('#firstName').should(be.blank).type('John')
    browser.element('#lastName').should(be.blank).type('Dou')
    browser.element('#userEmail').should(be.blank).type('JohnDou@test.com')

    browser.all('#genterWrapper label').should(have.texts('Male', 'Female', 'Other'))
    browser.all('#genterWrapper label').element_by(have.attribute('for', 'gender-radio-1')).click()
    '''
    browser.all('[name=gender]).element_by(have.value('Male')).element('./following-sibling::label').click() - кликаем по лэйблу
    browser.element('[name=gender][value=Male]+label').click() - кликаем по лэйблу ('+' - ищет элемент на том же уровне, ' ' - ищет элемент на любой вложенности в родительском, '>' - ищет первый вложенный элемент в родительский (непосредственно вложенный))
    browser.all('[name=gender]).element_by(have.value('Male')).element('..').click() - кликаем по диву, который оборачивает радио-баттон и лэйбл ('..' - перейти к родительскому элементу xpath-селектор )
    '''

    browser.element('#userNumber').should(be.blank).type('1234567890')
    browser.element('.react-datepicker-wrapper').click().element('#dateOfBirthInput').should(be.not_.blank)
    browser.element('.react-datepicker__tab-loop').element('.react-datepicker__month-select').click().element(
        '[value = "3"]').click()
    browser.element('.react-datepicker__tab-loop').element('.react-datepicker__year-select').click().element(
        '[value = "1985"]').click()
    browser.all('.react-datepicker__month .react-datepicker__day').element_by(have.exact_text('13')).click()
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    '''
    browser.element('[for=hobbies-checkbox-2]').perform(command.js.scroll_into_view) - проскроллить страницу до определнного элемента
    '''
    browser.element('#subjectsInput').type('M')
    browser.element('#react-select-2-option-0').click()
    browser.all('#hobbiesWrapper .custom-control-label').should(have.texts('Sports', 'Reading', 'Music'))
    browser.all('#hobbiesWrapper .custom-control-label').element_by(have.attribute('for', 'hobbies-checkbox-1')).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('photo.jpg'))
    browser.element('#currentAddress').type('Some Street, some house')
    browser.element('#state').click().element('#react-select-3-option-1').click()
    browser.element('#city').click().element('#react-select-4-option-1').click()
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.element('//table/tbody/tr[1]/td[1]').should(have.exact_text('Student Name')).element(
        '//table/tbody/tr[1]/td[2]').should(have.exact_text('John Dou'))
    browser.element('//table/tbody/tr[2]/td[1]').should(have.exact_text('Student Email')).element(
        '//table/tbody/tr[2]/td[2]').should(have.exact_text('JohnDou@test.com'))
    browser.element('//table/tbody/tr[3]/td[1]').should(have.exact_text('Gender')).element(
        '//table/tbody/tr[3]/td[2]').should(have.exact_text('Male'))
    browser.element('//table/tbody/tr[4]/td[1]').should(have.exact_text('Mobile')).element(
        '//table/tbody/tr[4]/td[2]').should(have.exact_text('1234567890'))
    browser.element('//table/tbody/tr[5]/td[1]').should(have.exact_text('Date of Birth')).element(
        '//table/tbody/tr[5]/td[2]').should(have.exact_text('13 April,1985'))
    browser.element('//table/tbody/tr[6]/td[1]').should(have.exact_text('Subjects')).element(
        '//table/tbody/tr[6]/td[2]').should(have.exact_text('Maths'))
    browser.element('//table/tbody/tr[7]/td[1]').should(have.exact_text('Hobbies')).element(
        '//table/tbody/tr[7]/td[2]').should(have.exact_text('Sports'))
    browser.element('//table/tbody/tr[8]/td[1]').should(have.exact_text('Picture')).element(
        '//table/tbody/tr[8]/td[2]').should(have.exact_text('photo.jpg'))
    browser.element('//table/tbody/tr[9]/td[1]').should(have.exact_text('Address')).element(
        '//table/tbody/tr[9]/td[2]').should(have.exact_text('Some Street, some house'))
    browser.element('//table/tbody/tr[10]/td[1]').should(have.exact_text('State and City')).element(
        '//table/tbody/tr[10]/td[2]').should(have.exact_text('Uttar Pradesh Lucknow'))
    browser.element('#closeLargeModal').click()
    browser.element('#example-modal-sizes-title-lg').should(be.not_.visible)
