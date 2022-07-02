import csv
import warnings

import pandas as pd

warnings.filterwarnings("ignore")


def task1():
    """
    Separate Movie IDs and Movie names.
    output in new created file - task1Output.csv
    """
    df = pd.read_csv("RatingsInput.csv")
    df["MovieID"] = df["MovieName"].map(lambda id: id.split(",")[0])
    df["MovieName"] = df["MovieName"].map(lambda name: name.split(",")[1])
    df.to_csv("task1Output.csv")


def task2():
    """
    String Capitalization - Capitalizing the first letter of every word in the movie names.
    output in new created file - task2Output.csv
    """
    task1()
    df = pd.read_csv("task1Output.csv")
    df["MovieName"] = df["MovieName"].map(lambda name: name.title())
    df.to_csv("task2Output.csv")


def task3():
    """
    Read in from your new CSV file from Task 2 and parse data into lists and dictionaries.
    A dictionary with the key as the age and the value as another dictionary.
    The inner dictionary will use the rating as the key and the list of movies as the value.
    """
    task2()
    df = pd.read_csv("task2Output.csv")
    labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    df["binInterval"] = pd.qcut(df["UserAge"], q=10, precision=0, duplicates="drop")
    df["UserAge"] = pd.qcut(
        df["UserAge"], q=10, precision=0, duplicates="drop", labels=labels
    )
    l0 = (df[["UserAge", "binInterval"]]).to_dict("record")
    max_val, min_val = df["binInterval"].max().right, df["binInterval"].min().left

    df1 = df.groupby("UserAge")
    cust_dic = {}
    for age, group in df1:
        df2 = group.groupby("Rating")
        temp_dic = {}
        for rating, grp in df2:
            temp_dic[rating] = list(grp["MovieName"])
        cust_dic[age] = temp_dic
    return cust_dic, l0, {"max_val": max_val, "min_val": min_val}


def task4(inp_age, recs=2, age_list=[]):
    """
    Find the recommended movies for a given age from best to worst ratings.
    parameters : age <int>, recs <int> default value = 2, age_list <list. default value = []
    recommendations are made on the basis of age group (recommendor is selected by finding the closest age group the user lies in) only if the ratings are above 2 and recommended movie list is created.
    if the number of recommendations asked (parameter : recs) is more than the recommended movie list, a new closest age group is chosen by the same process as mentioned above.
    """
    cust_dic, l0, minmax = task3()
    if not age_list:
        age_list = list(cust_dic.keys())
    if inp_age < minmax["min_val"]:
        age = 1
    elif inp_age > minmax["max_val"]:
        age = 10
    else:
        for i in l0:
            if inp_age in i["binInterval"]:
                age = i["UserAge"]
    difference = lambda age_list: abs(age_list - age)
    res = min(age_list, key=difference)
    count = 0
    a = 0
    l1 = []
    if 1 in cust_dic[res]:
        del cust_dic[res][1]
    if 2 in cust_dic[res]:
        del cust_dic[res][2]
    for i in sorted(cust_dic[res].keys()):
        a = len(cust_dic[res][i])
        for k in range(a):
            l1.append(cust_dic[res][i][k])
        count = a + count
    if count > recs:
        x = count - recs
        return l1[count - 1 : x - 1 : -1]
    elif recs > count:
        x = recs - count
        age_list.remove(res)
        l2 = task4(inp_age, x, age_list)
        l1.reverse()
        l2.reverse()
        return l1 + l2
    else:
        l1.reverse()
        return l1


def task5():
    """
    Recommend movies to users in the second input file
    output in new created file - task5Output.csv
    """
    output = pd.DataFrame()
    with open("NewUsers.csv", "r") as data:
        for line in csv.DictReader(data):
            line["Movies"] = ", ".join(
                task4(int(line["UserAge"]), int(line["NoOfMoviesToRecommend"]))
            )
            output = output.append(line, ignore_index=True)
    output.to_csv("task5Output.csv")
