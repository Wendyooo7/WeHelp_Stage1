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
