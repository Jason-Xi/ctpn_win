import datetime

if __name__ =='__main__':
    a = 0
    start = datetime.datetime.now()
    for i in range(100000):
        for j in range(10000):
            a = a + 1

    print(datetime.datetime.now()-start)
