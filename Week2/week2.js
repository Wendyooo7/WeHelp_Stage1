// Task 1
function findAndPrint(messages, currentStation) {
  let stations = [
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
  ];

  // 取出messages中每人所在捷運站，作為新物件的值
  let newMessages = {};
  let keys = Object.keys(messages);

  for (let i = 0; i < keys.length; i++) {
    let key = keys[i];
    let value = messages[key];
    for (let j = 0; j < stations.length; j++) {
      if (value.includes(stations[j])) {
        value = stations[j];
        newMessages[key] = value;
      }
    }
  }

  // 找最短距離的朋友
  let minDistance = Infinity;
  let closestFriend = null;
  let newKeys = Object.keys(newMessages);

  for (let i = 0; i < newKeys.length; i++) {
    // 切陣列
    let newKey = newKeys[i];
    let newValue = newMessages[newKey];
    let friendLocation = stations.indexOf(newValue);
    let myLocation = stations.indexOf(currentStation);
    let distance = Math.abs(myLocation - friendLocation);

    // 處理支線小碧潭
    if (currentStation == "Xiaobitan" && newValue == "Xindian City Hall") {
      distance++;
    } else if (currentStation == "Xiaobitan" && newValue == "Xindian") {
      distance = distance + 2;
    }

    if (newValue == "Xiaobitan" && currentStation == "Xindian City Hall") {
      distance++;
    } else if (newValue == "Xiaobitan" && currentStation == "Xindian") {
      distance = distance + 2;
    }

    if (distance < minDistance) {
      minDistance = distance;
      closestFriend = newKey;
    }
  }

  console.log(closestFriend);
  return closestFriend;
}

const messages = {
  "Bob": "I'm at Ximen MRT station.",
  "Mary": "I have a drink near Jingmei MRT station.",
  "Copper": "I just saw a concert at Taipei Arena.",
  "Leslie": "I'm at home near Xiaobitan station.",
  "Vivian": "I'm at Xindian station waiting for you.",
};

console.log("--- Task 1 ---");
findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian

// Task 2
// 創建全部顧問時間表
function consultantSchedule(consultants) {
  let schedule = {};

  for (let i = 0; i < consultants.length; i++) {
    let name = consultants[i].name;
    schedule[name] = Array(24).fill(0);
  }
  return schedule;
}

function book(consultants, hour, duration, criteria) {
  // 依顧客標準決定顧問排序
  let criteriaResult;

  if (criteria === "price") {
    // 陣列以價錢為標準採升冪排序
    criteriaResult = consultants.sort((a, b) => a.price - b.price);
  } else if (criteria === "rate") {
    // 陣列以評價為標準採降冪排序
    criteriaResult = consultants.sort((a, b) => b.rate - a.rate);
  }

  for (let i = 0; i < consultants.length; i++) {
    let consultantName = criteriaResult[i].name;
    let indieSchedule = schedule[consultantName];
    let count = 0;
    for (let j = hour - 1; j < hour + duration - 1; j++) {
      if (indieSchedule[j] == 1) {
        break;
      } else {
        indieSchedule[j] = 1;
        count++;
      }

      if (count == duration) {
        console.log(consultantName);
        return consultantName;
      }
    }
  }
  console.log("No Service");
  return "No Service";
}

const consultants = [
  { "name": "John", "rate": 4.5, "price": 1000 },
  { "name": "Bob", "rate": 3, "price": 1200 },
  { "name": "Jenny", "rate": 3.8, "price": 800 },
];

let schedule = consultantSchedule(consultants);

console.log("--- Task 2 ---");
book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John

// Task 3
function func(...data) {
  let middleNameObj = {};

  for (let fullName of data) {
    let index = Math.floor(fullName.length / 2);
    let middleName = fullName[index];
    if (!middleNameObj.hasOwnProperty(middleName)) {
      // 上行用Object.hasOwn(middleNameObj,middleName)此靜態方法是更安全的作法，但因為考量到瀏覽器支援度且在此題非必要故先不用
      middleNameObj[middleName] = [fullName];
    } else {
      middleNameObj[middleName].push(fullName);
    }
  }

  for (let value of Object.values(middleNameObj)) {
    if (value.length === 1) {
      console.log(value.join());
      return value.join();
    }
  }

  console.log("沒有");
  return "沒有";
}

console.log("--- Task 3 ---");
func("彭大牆", "陳王明雅", "吳明"); // print彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print夏曼藍波安

// Task 4
function getNumber(index) {
  if (index === 0) {
    console.log(0);
    return 0;
  }

  let sequence = [0];
  while (sequence.length <= index) {
    let lastElement = sequence[sequence.length - 1];
    if (sequence.length % 3 === 0) {
      sequence.push(lastElement - 1);
    } else {
      sequence.push(lastElement + 4);
    }
  }
  console.log(sequence[sequence.length - 1]);
  return sequence[sequence.length - 1];
}

console.log("--- Task 4 ---");
getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70
