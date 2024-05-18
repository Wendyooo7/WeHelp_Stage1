// Week7程式碼
document.querySelector("#query-button").addEventListener("click", async () => {
  const username = document.querySelector("#query-string").value;

  try {
    const response = await fetch(
      `http://127.0.0.1:8000/api/member?username=${encodeURIComponent(
        username
      )}`
    );
    const data = await response.json();

    const queryUsername = document.querySelector("#show-query-username");

    if (data && data.data) {
      queryUsername.textContent = `${data.data.name}(${data.data.username})`;
    } else {
      queryUsername.textContent = "查無此人";
    }
  } catch (err) {
    console.log(err);
  }
});

document.querySelector("#update-button").addEventListener("click", async () => {
  const updateValue = document.querySelector("#update-name").value;
  const updateName = document.querySelector("#show-update-name");

  try {
    const response = await fetch("http://127.0.0.1:8000/api/member", {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: updateValue }),
    });

    const data = await response.json();
    if (data.ok) {
      updateName.textContent = "更新成功";
    } else if (data.error) {
      updateName.textContent = "更新失敗";
    } else {
      updateName.textContent = "發生未知錯誤，請稍後再試";
    }
  } catch (err) {
    console.log("fetch err: ", err);
  }
});

// Week6程式碼
// 搭配HTML form標籤放onsubmit="return checkSignInInput();
function checkSignUpInput() {
  // 選擇姓名、帳號和密碼的輸入框的值
  const nameInput = document.querySelector("#name").value;
  const usernameInput = document.querySelector("#username").value;
  const passwordInput = document.querySelector("#password").value;

  // 檢查姓名、帳號和密碼是否都已填寫，填寫的話值就不是""（因為""empty str的值為假），故填寫後的值就為真
  if (nameInput && usernameInput && passwordInput) {
    // 如果三者均填寫，則允許表單提交
    return true;
  }

  // 如果三者任一未填寫，阻止表單的提交並顯示警告訊息
  alert("請確認全部註冊資料都已填寫");
  return false; // 阻止表單提交
}

function checkSignInInput() {
  const usernameInput = document.querySelector("#username2").value;
  const passwordInput = document.querySelector("#password2").value;

  // 檢查帳號和密碼是否都已填寫，填寫的話值就不是""（因為""empty str的值為假），故填寫後的值就為真
  if (usernameInput && passwordInput) {
    // 如果兩者均填寫，則允許表單提交
    return true;
  }

  // 如果兩者任一未填寫，阻止表單的提交並顯示警告訊息
  alert("請確認全部登入資料都已填寫");
  return false; // 阻止表單提交
}

function checkContentInput() {
  const contentInput = document.querySelector("#new-msg").value;

  if (contentInput) {
    return true;
  } else {
    alert("請輸入留言");
    return false;
  }
}
