import shutil
print("enter 'x' for exit");
filename1 = input("enter first file name to merge:");
if filename1 == 'x':
    exit();
else:
    filename2 = input("enter second file name to merge:");
    filename3 = input("create a newfile to merge content of 2 files inside this file:");
    print();
    print("merging the content of 2 file in ",filename3);
    with open(filename3,"wb") as wfd:
        for f in[filename1,filename2]:
            with open(f,"rb") as fd:
                shutil.copyfileobj(fd,wfd,1024*1024*10);
    print("content merged successfully!");
    print("want to see?(y/n):");
    check = input();
    if check == 'n':
        exit();
    else:
        print();
        c = open(filename3,"r");
        print(c.read());
        c.close();
