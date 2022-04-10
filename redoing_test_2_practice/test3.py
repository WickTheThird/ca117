from student_v3_121 import Student

def main():

    s1 = Student('Boris Spassky', 21345654)
    s2 = Student('Bobby Fischer', 21907321)

    s1.add_grade('english', 'H2')
    s1.add_grade('irish', 'O4')
    s1.add_grade('french', 'H3')
    s1.add_grade('physics', 'H3')
    print(s1)

    print(s2)

if __name__ == '__main__':
    main()