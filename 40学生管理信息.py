"""
学生管理系统:
1 添加学生信息
多个学生保存为列表,列表中每个元素(学生)为单独一个字典
2 显示学生信息
遍历学生信息列表,取出所有数据
3 删除学生信息
名字可能不唯一,更据学号删除
4 修改学生信息
可变函数
5 根据学生信息排序
匿名函数
6 退出
break
"""
student_id=10000
students=[]
#主函数/入口函数
def main():
    print("欢迎来到学生管理系统")
    while True:
       print("请选择功能编码:")
       print("1 添加学生信息")
       print("2 显示学生信息")
       print("3 删除学生信息")
       print("4 修改学生信息")
       print("5 根据学生信息排序")
       print("6 退出")
       if select_menu():
           break
#选择功能
def select_menu():
    try:
        choice = int(input("请选择功能编码:"))
        if choice == 1:
            add_student()
        elif choice == 2:
            show_student()
        elif choice == 3:
            delete_student()
        elif choice == 4:
            update_student()
        elif choice == 5:
            sort_student()
        elif choice == 6:
            print("退出系统")
            return True
        else:
            print("输入错误,请重新输入")
    except KeyboardInterrupt:
        print("\n程序已被用户中断退出")
        return True
    except ValueError:
        print("输入无效，请输入数字")
#1 实现添加学生信息功能
def add_student():
    name = input("请输入学生姓名:")
    age = int(input("请输入学生年龄:"))
    score = float(input("请输入学生成绩:"))
    global student_id
    student_id += 1
    students.append({"name":name,"age":age,"score":score,"id":student_id})
    print("添加成功")
#2 显示所有学生信息
def show_student():
    for i in students:
        print(f"id:{i['id']} 姓名:{i['name']} 年龄:{i['age']} 成绩:{i['score']}")
#3 实现删除学生信息功能
def delete_student():
    a_id = int(input("请输入学生id:"))
    for k,v in enumerate(students):#给每个v添加下标
        if v["id"] == a_id:
            del students[k]
            print("删除成功")
            return
    print("没有此id")
    #4 实现修改学生信息功能
def update_student():
    b_id = int(input("请输入学生id:"))
    for d in students:
        if d["id"] == b_id:
            d["name"] = input("请输入学生姓名:")
            d["age"] = int(input("请输入学生年龄:"))
            d["score"] = float(input("请输入学生成绩:"))
            print("修改成功")
            return
    print("没有此id")
#5 实现根据学生信息排序功能
def sort_student():
    students.sort(key=lambda x:x["score"],reverse=True)#匿名函数 lambda: 关键字，表示定义匿名函数 x: 参数名（可以是任意名称） x["score"]: 函数体，返回字典中"score"键的值
    show_student()
"""
key参数: 指定排序依据，告诉sort()函数按照什么标准进行排序
lambda x:x["score"]:
对于students列表中的每个元素（学生字典），用x表示
提取该字典中的"score"字段值作为排序依据
相当于定义了一个函数：def get_score(x): return x["score"]
"""
main()






