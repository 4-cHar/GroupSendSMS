adb shell am start -a android.intent.action.SENDTO -d sms:testnum --es sms_body "testname请在引号内编辑文字，可以带空格，未测试换号" --ez exit_on_sent true
        adb shell input keyevent 22
        timeout /T 1 /NOBREAK
        adb shell input keyevent 66
        timeout /T 1 /NOBREAK
#!/bin/bash
        adb shell am start -a android.intent.action.SENDTO -d sms:name --es sms_body "测试内容，Name:num" --ez exit_on_sent true
        adb shell input keyevent 22
        timeout /T 1 /NOBREAK
        adb shell input keyevent 66
        timeout /T 1 /NOBREAK
        echo 确保测试短信没问题后任意键继续，否则关闭窗口
        pause
echo 操作完成
        pause
