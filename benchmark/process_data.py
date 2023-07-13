##从日志中获取各种所需要的数据，以及数据结构
##维护人：张克凡
import re


def get_time_data(log_file_path):
    with open(log_file_path, 'r') as log_file:
        pattern = r'(\d+:\d+\.\d+)elapsed'
        for line in log_file:
            # 使用正则表达式进行匹和提取
            match = re.search(pattern, line)
            if match:
                time_data = match.group(1)
                return time_data #mins
                # 提取到的时间数据
            else :
                return 0

def get_data(log_file_path,string,n):
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            if string in line:
                Rating_scores = float(line.split()[n].replace(",",""))
                break
            if 'No such file or directory' in line:
                Rating_scores = 0
                print("No such file or directory,测试未进行")
        if Rating_scores  :
            return Rating_scores  #MIPS
        else:
            return 0



