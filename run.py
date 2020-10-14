import csv, os, re, sys


class Main:
    def __init__(self):
        self.file = csv.reader(open('template.csv', 'r'))
        sel = sys.platform
        if sel == "win32" or sel == "cygwin":
            self.bfile = open('run.bat', 'w+', encoding='utf-8')
        elif sel == "darwin" or sel == "linux":
            self.bfile = open('run.sh', 'w+', encoding='utf-8')

    def run(self):
        for i, row in enumerate(self.file):
            if i == 1:
                strings = f"""#!/bin/bash
        adb shell am start -a android.intent.action.SENDTO -d sms:{row[1]} --es sms_body "测试内容，Name:{row[0]}" --ez exit_on_sent true
        adb shell input keyevent 22
        timeout /T 1 /NOBREAK
        adb shell input keyevent 66
        timeout /T 1 /NOBREAK
        echo 确保测试短信没问题后任意键继续，否则关闭窗口
        pause"""
                self.bfile.write(strings)
                self.bfile.write("\n")
            else:
                name = row[1]
                num = row[0]
                strings = f"""adb shell am start -a android.intent.action.SENDTO -d sms:{num} --es sms_body "{name}请在引号内编辑文字，可以带空格，未测试换号" --ez exit_on_sent true
        adb shell input keyevent 22
        timeout /T 1 /NOBREAK
        adb shell input keyevent 66
        timeout /T 1 /NOBREAK"""
                self.bfile.write(strings)
                self.bfile.write("\n")

        strings = """echo 操作完成
        pause"""
        self.bfile.write(strings)
        self.bfile.write("\n")
        self.bfile.close()

    def do(self):
        if os.path.exists('run.bat'):
            val = os.system('run.bat')
        else:
            val = os.system('run.sh')


if __name__ == '__main__':
    start = Main()
    start.run()
    start.do()
