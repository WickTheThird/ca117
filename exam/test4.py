from student_v4_121 import Student

def main():

    s1 = Student('Boris Spassky', 21345654)
    s2 = Student('Bobby Fischer', 21907321)
    s3 = Student('Mikhail Tal', 21884786)

    s1.add_grade('english', 'H2')
    s1.add_grade('irish', 'H3')
    s1.add_grade('chemistry', 'H5')
    print(s1)

    s2.add_grade('irish', 'H3')
    s2.add_grade('physics', 'H2')
    s2.add_grade('french', 'O1')
    print(s2)

    s3.add_grade('art', 'H1')
    s3.add_grade('music', 'H2')
    s3.add_grade('woodwork', 'H2')
    print(s3)

    assert(s1 == s2)
    assert(s1 < s3)
    assert(s3 > s2)

if __name__ == '__main__':
    main()
