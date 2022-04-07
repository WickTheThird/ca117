from classlist_v3_121 import Student, Classlist

def main():

    cl = Classlist()
    s1 = Student('Boris Spassky', 21345654)
    s2 = Student('Bobby Fischer', 21907321)
    s3 = Student('Mikhail Tal', 21884786)

    s1.add_grade('english', 'H1')
    s1.add_grade('irish', 'O4')

    s2.add_grade('english', 'H2')
    s2.add_grade('french', 'O5')
    s2.add_grade('spanish', 'O1')

    s3.add_grade('english', 'O3')
    s3.add_grade('irish', 'O3')

    cl.add(s1)
    cl.add(s2)
    cl.add(s3)

    print(cl.most_popular_subject())

if __name__ == '__main__':
    main()
