import os

ls = os.listdir('.')
# ls와 같은 동작을 한다. listdir : ls
# 현재 디렉토리에 있는 파일 및 폴더들
print(ls)

pwd = os.getcwd()
# getcwd (get current working directory) : pwd
# 현재 파일이 실행된 디렉토리 (작업하고 있는 디렉토리)
print(pwd)

os.chdir(r'./dummy')
print(pwd)