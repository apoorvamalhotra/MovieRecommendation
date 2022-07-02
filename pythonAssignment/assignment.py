import warnings

from pythonAssignment import tasks

warnings.filterwarnings("ignore")


def input_id():
    inp = check_input("task number", 6)
    initiate_task(inp)


def initiate_task(tid):
    if tid == 1:
        tasks.task1()
        print("Task Completed.\nOutput File: task1Output.csv")
    if tid == 2:
        tasks.task2()
        print("Task Completed.\nOutput File: task2Output.csv")
    if tid == 3:
        cust_dict, l0, minmax = tasks.task3()
        print(f"Custom Dictonary is : {cust_dict}")
        print("Task Completed.")
    if tid == 4:
        age = check_input("user age", 101)
        recommendations = check_input("number of recommendations", 26)
        recom = tasks.task4(inp_age=age, recs=recommendations)
        print(f"List of recommendations is : {recom}")
        print("Task Completed.")
    if tid == 5:
        tasks.task5()
        print("Task Completed.\nOutput File: task5Output.csv")


def check_input(inp_name, max_val):
    try:
        inp = int(input(f"Enter {inp_name} : "))
        if inp > 0 and inp < max_val:
            return inp
        else:
            print(f"{inp_name} should be a numeric value in range 1 to {max_val-1}")
            return check_input(inp_name, max_val)
    except Exception as e:
        print(f"An exception has occured : {str(e)}")
        print(f"{inp_name} should be a numeric value in range 1 to {max_val-1}")
        return check_input(inp_name, max_val)


input_id()
