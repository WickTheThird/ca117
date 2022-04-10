from student_v2_121 import Student

def main():

    s1 = Student('Boris Spassky', 17345654)
    s2 = Student('Bobby Fischer', 17907321)

    s1.add_grade('english', 'H3')
    s1.add_grade('irish', 'O2')
    print(s1.get_grade('english'))

    s2.add_grade('english', 'H4')
    s2.add_grade('irish', 'H6')
    s2.add_grade('chemistry', 'O5')
    print(s2.get_grade('physics'))

if __name__ == '__main__':
    main()