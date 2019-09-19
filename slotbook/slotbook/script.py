f = open('regf.csv', 'r')
# f = open('test.txt', 'r')
a = 0
for line in f:
    if a != 0:
        line = line.split(';')
        print(line)
        # Register.objects.create(college=line[1],
        #                         date=line[2],
        #                         email1=line[3],
        #                         email2=line[4],
        #                         events=line[5],
        #                         field_id=line[6],
        #                         name1=line[7],
        #                         name2=line[8],
        #                         name3=line[9],
        #                         name4=line[10],
        #                         phone1=line[11],
        #                         phone2=line[12],
        #                         receipt_no=line[13],
        #                         total=line[14],
        #                         year=line[15])
        print("f")
        break
    else:
        a = a+1
        print('ff')


