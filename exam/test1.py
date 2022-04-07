from student_v1_121 import Student

def main():
    s1 = Student('Boris Spassky', 21345654)
    s2 = Student('Bobby Fischer', 21907321)

    assert(s1.name == 'Boris Spassky')
    assert(s1.cao == 21345654)

    print(s1)
    print(s2)

if __name__ == '__main__':
    main()
