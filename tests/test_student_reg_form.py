from model.test_student_reg_form_page import TestStudentRegFormPage


def test_student_reg_form():
    reg_form = TestStudentRegFormPage()

    reg_form.open()

    reg_form.fill_first_name('John')
    reg_form.fill_last_name('Dou')
    reg_form.fill_email('JohnDou@test.com')
    reg_form.select_gender('Male')
    reg_form.fill_number('1234567890')
    reg_form.fill_date_of_birth(13, 3, 1985)
    reg_form.scroll_page_to_the_end()
    reg_form.fill_subject('Maths')
    reg_form.select_hobby()  # рефакторить селектор
    reg_form.upload_photo()  # рефакторить способ построения пути к фото
    reg_form.fill_current_address('Some Street, some house')
    reg_form.fill_state('Uttar Pradesh')
    reg_form.fill_city('Lucknow')
    reg_form.click_submit_button()

    reg_form.assert_user_values()

    reg_form.close_table()
