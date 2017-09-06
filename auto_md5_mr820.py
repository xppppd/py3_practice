# 用于计算目标文件夹里的bin文件并生成md5.txt
import os
import re


def get_md5():
    target_dir = input('输入文件所在目录:\n')
    filename = 'md5.txt'
    target_file = os.path.join(target_dir, filename)
    if os.path.isdir(target_dir):
        cmd = 'md5 ' + target_dir + '/*.bin'
        pat = re.compile('.*/(\S*bin)\)\s=\s(\S{32})')
        # 该pat用来过滤文件名跟md5值
        file = open(target_file, 'w')
        for line in os.popen(cmd).readlines():
            result = re.match(pat, line).groups()
            for s in result:
                file.write(s + ' ')
            file.write('\n')
        file.close()
        print('*****文件已生成！*****\n')
        print('文件目录：' + target_file)
    else:
        print('路径有误！！！请重新输入!\n')
        get_md5()


get_md5()
