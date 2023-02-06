# 开发人员：陶景航
# 开发时间：2023/2/4 14:18
import os

filename = 'student.txt'


# 主菜单
def nume():
    print('********************学生信息管理系统********************')
    print('********************功能菜单********************')
    print('                 1、录入学生信息')
    print('                 2、查找学生信息')
    print('                 3、修改学生信息')
    print('                 4、删除学生信息')
    print('                 5、对成绩进行排序')
    print('                 6、统计学生总人数')
    print('                 7、显示全部信息')
    print('                 0、退出系统')


# 录入信息
def insert():
    student_list = []  # 用于存储录入的学生
    while True:
        id = int(input('id：'))
        if not id:
            break
        name = input('姓名：')
        if not name:
            break
        try:
            English = int(input('英语成绩：'))
            Python = int(input('python成绩：'))
            Java = int(input('java成绩：'))
        except:
            print('重新输入！')
            continue
        # 将学生信息保存在字典当中
        student = {'id': id, '姓名': name, '英语': English, 'python': Python, 'java': Java}
        # 将信息添加到列表中
        student_list.append(student)
        answer = input('继续添加？T/F')
        if answer == 'T' or answer == 't':
            continue
        else:
            break
    # 调用save（）函数将信息保存在文件中
    save(student_list)
    print('学生信息录入成功！')


## 信息存入文件的函数
def save(list):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')  # 以只读的模式打开
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')  # 以写的模式打开
    for item in list:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


# 查找（显示不出信息）
def search():
    student_query = []
    while True:
        #id = ''
        #name = ''
        if os.path.exists(filename):
            mode = int(input('1‘按学号查找   2、按姓名查找'))
            if mode == 1:
                id = int(input('请输入学号'))
            elif mode == 2:
                name = input('请输入姓名：')
            else:
                print('无此查找方式！')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if d['id']== id:
                            student_query.append(d)
                    elif name != '':
                        if d['姓名'] == name:
                            student_query.append(d)
            print(student_query)
            student_query.clear()
            answer = input('继续查找？T/F')
            if answer == 'T' or answer == 't':
                continue
            else:
                break
        else:
            print('文件不存在！')


# 修改#
def modify():
    show()  # 判斷文件是否存在
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_od = rfile.readlines()
    else:
        return
    student_id = int(input('请输入要修改的学生的学号：'))  # 版本不同注意转换数据类型
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_od:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('可以修改相关信息')
                while True:
                    try:
                        d['姓名'] = input('姓名：')
                        d['英语'] = input('英语：')
                        d['python'] = input('python')
                        d['java'] = input('java：')
                    except:
                        print('输入有误！')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改完成！')
            else:
                print('查无此人')
    answer = input('继续操作？T/F')
    if answer == 'T' or answer == 't':
        modify()


# 删除
def delete():
    while True:
        student_id = int(input('需要删除的学号'))
        if student_id != '':
            if os.path.exists(filename):  # 判断文件是否存在
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if int(d['id']) != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = 1
                    if flag == 1:
                        print(f'学号为{student_id}的相关信息已经删除')
                    else:
                        print('操作失败')
            else:
                print('无效操作')
                break
            show()
            answer = input('继续操作？T/F')
            if answer == 'T' or answer == 't':
                continue
            else:
                break


def sort():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()
        student_new = []
        for item in student_list:
            d = dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc = input('1、升序   2、降序')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('操作有误')
        sort()
    mode = input('选择排序科目1、英语 2、python 3、java 4、总成绩 0、学号')
    if mode == '0':
        student_new.sort(key=lambda x: int(x['id']), reverse=asc_or_desc_bool)
    elif mode == '1':
        student_new.sort(key=lambda x: int(x['英语']), reverse=asc_or_desc_bool)
    elif mode == '2':
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode == '3':
        student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
    elif mode == '4':
        student_new.sort(key=lambda x: int(x['英语']) + int(x['python']) + int(x['java']), reverse=asc_or_desc_bool)
    else:
        print('请输入正确的数！')
        sort()
    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print('一共有{0}名学生'.format(len(students)))
            else:
                print('none')
    else:
        print('找不到数据')


# 显示数据
def show_student(list):
    if len(list) == 0:
        print('未找到信息')
        return
    # 定义标体显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('学号', '姓名', '英语', 'python', 'java', '总成绩'))
    # 定义内容显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^9}'
    for item in list:
        print(format_data.format(
            item.get('id'),
            item.get('姓名'),
            item.get('英语'),
            item.get('python'),
            item.get('java'),
            int(item.get('英语')) + int(item.get('python')) + int(item.get('java'))
        ))


def show():
    student_list = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            for item in students:
                student_list.append(dict(eval(item)))
            if student_list:
                show_student(student_list)


def main():
    while True:  # 一直显示主菜单
        nume()
        choise = int(input('请选择你所需要的功能'))
        if choise in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choise == 0:
                answer = input('确定退出？（T/F）')
                if answer == 'T' or answer == 't':
                    print('谢谢你的使用！')
                    break  # 退出系统
                else:
                    continue
            elif choise == 1:
                insert()
            elif choise == 2:
                search()
            elif choise == 3:
                modify()
            elif choise == 4:
                delete()
            elif choise == 5:
                sort()
            elif choise == 6:
                total()
            elif choise == 7:
                show()


if __name__ == '__main__':  # 以主程序的方式进行运行
    main()
