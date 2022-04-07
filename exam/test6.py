from classlist_v2_121 import Student, Classlist

def main():

    cl = Classlist()
    s1 = Student('Boris Spassky', 21345654)
    s2 = Student('Bobby Fischer', 21907321)
    s3 = Student('Mikhail Tal', 21884786)

    cl.add(s1)
    cl.add(s2)
    cl.add(s3)

    print(cl)

if __name__ == '__main__':
    main()
