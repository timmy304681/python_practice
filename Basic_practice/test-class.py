#coding=UTF-8
#定義類別,與類別屬性（封裝在類別中的變數與函式）
#定義一個類別IO,有兩個屬性supportedSrc和read
class IO:
    supportedSrcs=["console", "file"] #資源的資料來源,讓使用者從終端機(console)或是檔案
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not supported")
        else:
            print("Read from", src)

#使用類別
print(IO.supportedSrcs)

IO.read("file")

IO.read("internet")
