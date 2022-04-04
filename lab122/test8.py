from mp3collection_v3_131 import MP3Track, MP3Collection

def main():
    t1 = MP3Track('Fools Gold', 604, ['The Stone Roses'])
    t2 = MP3Track('Shallow', 197, ['Lady Gaga', 'Bradley Cooper'])
    t3 = MP3Track('Telephone', 220, ['Beyonce', 'Lady Gaga'])

    c1 = MP3Collection()
    c1.add(t1)
    c1.add(t2)

    c2 = MP3Collection()
    c2.add(t3)

    # Make a new collection from two existing ones
    c3 = c1 + c2
    assert(isinstance(c3, MP3Collection))
    assert(c3 is not c1)
    assert(c3 is not c2)

if __name__ == '__main__':
    main()