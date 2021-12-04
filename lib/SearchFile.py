import os

def search_files(path):
    file_names = os.listdir(path)
    file_list = [os.path.join(path, file) for file in file_names]
    return file_list




def from_list_get_filename(file_list):
    name_list = []
    for name in file_list:
        name = name.split("\\")[-1] #得到最后的文件名
        name = name.split(".")[0]  #去掉后缀
        name_list.append(name)
    return name_list

#file_list = search_files("G:\Data\MyBlog\source_blog\scaffolds")
#print(from_list_get_filename(file_list))
#for item in from_list_get_filename(file_list):
#    print(item)

#print(search_files("G:\Data\MyBlog\source_blog\scaffolds"))