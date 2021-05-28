import os
import cv2
import shutil
import random


class BatchRename():
    """
    批量重命名文件夹中的图片文件
    """

    def __init__(self, path):
        self.path = path

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 1
        for item in filelist:
            Suffix_name = ['.png', '.jpg', '.jpeg', '.tif']
            if item.endswith(tuple(Suffix_name)):
                n = 6 - len(str(i))
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), str(0) * n + str(i) + '.jpg')
                try:
                    os.rename(src, dst)
                    # print('converting %s--to-->%s' % (src, dst))
                    i = i + 1
                except:
                    continue
        print('total %d to rename & converted %d jpgs' % (total_num, i))


def list_dictionary_codes(root_dir):
    paths_list = []
    for parent, dirNames, fileNames in os.walk(root_dir):
        for name in fileNames:
            ext = ['.jpg', '.png', '.jpeg']  # 需要移动文件的后缀名
            if name.endswith(tuple(ext)):
                paths_list.append(os.path.join(parent, name))
    return paths_list


def copy_move_file(root_dir, target_path):
    paths_list = list_dictionary_codes(root_dir)
    for file_path in paths_list:
        shutil.move(file_path, target_path)
        print("正在move文件：", file_path)
    print("done!")


def rename():
    path = r"D:\Codes\chip_defect_detection\roi\all"  # 文件夹目录
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    for dir in files:  # 遍历文件夹
        if os.path.isdir(dir):  # 判断是否是文件夹，不是文件夹才打开
            temp_path = os.path.join(path, dir)  # 图片文件夹路径
            BatchRename(path).rename()


def train_txt_file():
    with open("../dataset/train.txt", "w", encoding="utf-8") as train_file:
        path = "../dataset/"  # 文件夹目录
        dirs = os.listdir(path)  # 得到文件夹下的所有文件名称
        s = []
        for dir in dirs:  # 遍历文件夹
            if os.path.isdir(dir):  # 判断是否是文件夹，不是文件夹才打开
                temp_path = os.path.join(path, dir)  # 图片文件夹路径
                files = os.listdir(temp_path)
                for file in files:
                    train_file.write(dir + "/" + file + "\n")


def shuffle():
    out = open("./train1.txt", 'w')
    lines = []
    with open("../dataset/train.txt", 'r') as infile:
        for line in infile:
            lines.append(line)
    random.shuffle(lines)
    for line in lines:
        out.write(line)


def rgb2gray():
    path = "../dataset/"  # 文件夹目录
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    for dir in files:  # 遍历文件夹
        if os.path.isdir(dir):  # 判断是否是文件夹，不是文件夹才打开
            temp_path = os.path.join(path, dir)  # 图片文件夹路径
            files = os.listdir(temp_path)
            for file in files:
                read_path = os.path.join(temp_path, file)
                img = cv2.imread(read_path, cv2.IMREAD_GRAYSCALE)
                cv2.imwrite(os.path.join(temp_path, "99" + file), img)


if __name__ == '__main__':
    rename()
    # train_txt_file()
    # shuffle()
