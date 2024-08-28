from data.student_info import Student
from model.student_reg_form_page import StudentRegFormPage

student = Student('John', 'Dou', 'JohnDou@test.com', 'Male', '1234567890', '13', 'April', '1985',
                  'Maths', 'Sport', 'photo.jpg', 'Some Street, some house',
                  'Uttar Pradesh', 'Lucknow')


def test_student_reg_form():
    registration_page = StudentRegFormPage()

    registration_page.open()
    registration_page.student_registration(student)
    registration_page.shoud_registered_student_with(student)
