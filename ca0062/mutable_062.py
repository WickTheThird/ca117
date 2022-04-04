#!/usr/bin/env python3

# Append l1 to l2. If l2 not supplied default to empty list.
def append2list(l1, listing=[]):
    if len(listing) != 0:
        for i in l1:
            listing.append(i)
        return listing
    return l1

def main():
    list1 = ['fly', 'spider']
    list1 = append2list(list1)
    print(list1)

    list2 = ['lion']
    list2 = append2list(list2, ['lion'])
    print(list2)

    list3 = ['fox', 'chicken']
    nlist3 = append2list(list3)
    print(nlist3)


if __name__ == '__main__':
    main()
