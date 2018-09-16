
infile = open('acc_histrjn_yjs.txt','rb') #二进制读取
outfile = open("test.txt","w")
s = infile.readline()
print(s)
# print(s.decode('unicode-escape').encode('utf-8'))
# outfile.write(s)

infile.close()
outfile.close()

# if __name__ == '__main__':
#     run_coding()
#     print("It's done")