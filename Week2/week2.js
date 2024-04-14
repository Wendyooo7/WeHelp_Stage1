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

console.log("===Task3===");
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
    let last_element = sequence[sequence.length - 1];
    if (sequence.length % 3 === 0) {
      sequence.push(last_element - 1);
    } else {
      sequence.push(last_element + 4);
    }
  }
  console.log(sequence[sequence.length - 1]);
  return sequence[sequence.length - 1];
}

console.log("===Task4===");
getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70
