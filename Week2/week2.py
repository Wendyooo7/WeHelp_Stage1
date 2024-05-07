# Task 1
def find_and_print(messages, current_station):
    stations = [
        "Songshan",
        "Nanjing Sanmin",
        "Taipei Arena",
        "Nanjing Fuxing",
        "Songjiang Nanjing",
        "Zhongshan",
        "Beimen",
        "Ximen",
        "Xiaonanmen",
        "Chiang Kai-Shek Memorial Hall",
        "Guting",
        "Taipower Building",
        "Gongguan",
        "Wanlong",
        "Jingmei",
        "Dapinglin",
        "Qizhang",
        "Xiaobitan",
        "Xindian City Hall",
        "Xindian",
    ]

    # 取出messages中每人所在捷運站，作為新物件的值
    new_messages = {}
    for key in messages.keys():
        value = messages[key]
        for j in range(0, len(stations)):
            if stations[j] in value:
                value = stations[j]
                new_messages[key] = value

    # 找最短距離的朋友
    min_distance = float('inf')
    closest_friend = None

    for new_key in new_messages:
        new_value = new_messages[new_key]
        friend_location = stations.index(new_value)
        my_location = stations.index(current_station)
        distance = abs(my_location - friend_location)

        # 處理支線小碧潭
        if current_station == "Xiaobitan" and new_value == "Xindian City Hall":
            distance += 1
        elif current_station == "Xiaobitan" and new_value == "Xindian":
            distance += 2

        if new_value == "Xiaobitan" and current_station == "Xindian City Hall":
            distance += 1
        elif new_value == "Xiaobitan" and current_station == "Xindian":
            distance += 2

        if distance < min_distance:
            min_distance = distance
            closest_friend = new_key

    print(closest_friend)
    return closest_friend


messages = {
    "Leslie": "I'm at home near Xiaobitan station.",
    "Bob": "I'm at Ximen MRT station.",
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Vivian": "I'm at Xindian station waiting for you."
}

print("===Task1===")
find_and_print(messages, "Wanlong")  # print Mary
find_and_print(messages, "Songshan")  # print Copper
find_and_print(messages, "Qizhang")  # print Leslie
find_and_print(messages, "Ximen")  # print Bob
find_and_print(messages, "Xindian City Hall")  # print Vivian


# Task 2
# 創建全部顧問時間表
def consultant_schedule(consultants):
    schedule = {}

    for consultant in consultants:
        name = consultant["name"]
        schedule[name] = [0] * 24
    return schedule


def book(consultants, hour, duration, criteria):
    criteria_result = None

    if criteria == "price":
        criteria_result = sorted(consultants, key=lambda x: x["price"])
    elif criteria == "rate":
        criteria_result = sorted(consultants,
                                 key=lambda x: x["rate"],
                                 reverse=True)

    for consultant in criteria_result:
        consultant_name = consultant["name"]
        indie_schedule = schedule[consultant_name]
        count = 0
        for j in range(hour - 1, hour + duration - 1):
            if indie_schedule[j] == 1:
                break
            else:
                indie_schedule[j] = 1
                count += 1

            if count == duration:
                print(consultant_name)
                return consultant_name

    print("No Service")
    return "No Service"


consultants = [{
    "name": "John",
    "rate": 4.5,
    "price": 1000
}, {
    "name": "Bob",
    "rate": 3,
    "price": 1200
}, {
    "name": "Jenny",
    "rate": 3.8,
    "price": 800
}]

schedule = consultant_schedule(consultants)

print("===Task2===")
book(consultants, 15, 1, "price")  # Jenny
book(consultants, 11, 2, "price")  # Jenny
book(consultants, 10, 2, "price")  # John
book(consultants, 20, 2, "rate")  # John
book(consultants, 11, 1, "rate")  # Bob
book(consultants, 11, 2, "rate")  # No Service
book(consultants, 14, 3, "price")  # John


# Task 3
def func(*data):

    middle_name_dict = {}

    for full_name in data:
        index = len(full_name) // 2
        middle_name = full_name[index]
        if middle_name not in middle_name_dict:
            middle_name_dict[middle_name] = [full_name]
        else:
            middle_name_dict[middle_name].append(full_name)

    for value in middle_name_dict.values():
        if len(value) == 1:
            print(value[0])
            return (value[0])

    print("沒有")
    return "沒有"


print("===Task3===")
func("彭大牆", "陳王明雅", "吳明")  # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆")  # print 夏曼藍波安


# Task 4
def get_number(index):

    if index == 0:
        print(0)
        return 0

    sequence = [0]
    while len(sequence) <= index:
        last_element = sequence[len(sequence) - 1]
        if len(sequence) % 3 == 0:
            sequence.append(last_element - 1)
        else:
            sequence.append(last_element + 4)
    print(sequence[len(sequence) - 1])
    return sequence[len(sequence) - 1]


print("===Task4===")
get_number(1)  # print 4
get_number(5)  # print 15
get_number(10)  # print 25
get_number(30)  # print 70
