from mp3collection_v2_131 import MP3Track, MP3Collection

def main():
    t1 = MP3Track('Fools Gold', 604, ['The Stone Roses'])
    t2 = MP3Track('Shallow', 197, ['Lady Gaga', 'Bradley Cooper'])
    t3 = MP3Track('Telephone', 220, ['Beyonce', 'Lady Gaga'])

    c = MP3Collection()

    c.add(t1)
    c.add(t2)
    c.add(t3)

    # Retrieve all MP3Tracks from the collection by Lady Gaga
    tracklist = c.get_mp3s_by_artist('Lady Gaga')
    assert(len(tracklist) == 2)
    assert(t2 in tracklist)
    assert(t3 in tracklist)

if __name__ == '__main__':
    main()
