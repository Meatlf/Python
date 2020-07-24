# 参考资料：[1] [浅析Python中的main函数](https://www.cnblogs.com/keguo/p/9760361.html)
# import os
# import time
import datetime

print('Hello World!')
print('Time is ', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %A'))
print('__name__ value: ', __name__)


def main():
    print('this message is from main function')


if __name__ == '__main__':
    main()
    print(__name__)
