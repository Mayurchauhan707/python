def set1():
    sentence=[input("enter the sentence").split()]
    print(sentence)
    s=set()
    for x in sentence:
        s.add(x.upper())
        s={x.upper()for x in sentence}
        print(s)
set1()

