from spider import InfoStorage
from spider import CourseTableParser
import requests

def menu():
    print(' -'*20)
    print('      方正教务系统爬虫 for AHUT')
    print(' -'*20)
    menu_item = {'1': InfoStorage.login,
                '2': CourseTableParser.start,
                '3': 2,
                '4': 3,
                'q': exit}
    print('     请输入功能的数字序号以进行后续操作')
    print('     + 1.登陆用户')
    print('     + 2.显示课表')
    print('     + 3.显示考试时间')
    print('     + 4.抢课')
    print('     + q.退出程序')
    print(' -'*20)
    input_selection = input()
    menu_item.get(input_selection)()


if __name__ == '__main__':
    # main()
    InfoStorage.SESSION = requests.session()
    while True:
        menu()
    InfoStorage.SESSION.close()