# NAME = 0
# AGE = 1
# ADDRESS = 2
NAME, AGE, ADDRESS = range(3)

student = ('五哈', 15, '邓超')

print(student[NAME],student[AGE],student[ADDRESS])


from collections import namedtuple

student_obj = namedtuple('student', ['name', 'age', 'address'])
# student = student_obj('五哈', 10, '鹿晗')
student = student_obj(name='五哈', age=100, address='陈赫')
print(student.name, student.age, student.address)
print(isinstance(student, tuple))