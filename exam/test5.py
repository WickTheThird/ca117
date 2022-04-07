from classlist_v1_121 import Student, Classlist

def main():

    cl = Classlist()
    s1 = Student('Boris Spassky', 21345654)
    s2 = Student('Bobby Fischer', 21907321)

    cl.add(s1)
    cl.add(s2)

    s = cl.lookup(21345654)
    assert(isinstance(s, Student))
    assert(s.name == 'Boris Spassky')
    assert(s.cao == 21345654)

    cl.remove(21345654)
    s = cl.lookup(21345654)
    assert(s is None)

if __name__ == '__main__':
    main()
