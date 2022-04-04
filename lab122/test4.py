from mp3track_v3_131 import MP3Track

def main():
    t1 = MP3Track('Fools Gold', 604, ['The Stone Roses'])
    t2 = MP3Track('Shallow', 197)

    print(t1)
    print(t2)

    t2.add_artist('Lady Gaga')
    print(t2)

    t2.add_artist('Bradley Cooper')
    print(t2)

if __name__ == '__main__':
    main()