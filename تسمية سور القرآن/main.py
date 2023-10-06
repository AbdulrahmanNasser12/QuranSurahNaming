import os
path = "D:\قرآن\حسن صالح\حسن صالح ورش"
path = path.replace('\\', '/')
if len(os.listdir(path)) != 114:
    print("Mismatch between the number of files and the list length")
else:
    print("For renaming with Arabic names enter  (1)")
    language = input("For renaming with English names enter (2) : ")
    if int(language) == 1:
        my_file = open("قائمة اسماء السور.txt", "r", encoding="utf-8")
        data = my_file.read()
        data_into_list = data.split("\n")
        my_file.close()
        i = 0
        for filename in os.listdir(path):
            i += 1
            oldname = path + '/' + filename
            formated_i = "{:03d}".format(i)
            temp = filename
            temp = path + '/' + str(formated_i) + '. ' + temp.replace(temp[3:],"") + '.mp3'
            os.rename(oldname, temp)
            newname = path + '/' + str(formated_i) + '. ' + data_into_list[i - 1] + '.mp3'
            os.rename(temp, newname)
        print("File renaming complete.")
    elif int(language) == 2:
        my_file = open("Surah names list.txt", "r", encoding="utf-8")
        data = my_file.read()
        data_into_list = data.replace('\n', ' ').split(" ")
        my_file.close()
        i = 0
        for filename in os.listdir(path):
            i += 1
            oldname = path + '/' + filename
            formated_i = "{:03d}".format(i)
            temp = filename
            temp = path + '/' + str(formated_i) + '. ' + temp.replace(temp[3:], "") + '.mp3'
            os.rename(oldname, temp)
            newname = path + '/' + str(formated_i) + '. ' + data_into_list[i - 1] + '.mp3'
            os.rename(temp, newname)
        print("File renaming complete.")
