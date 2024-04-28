// 搭配HTML form標籤放onsubmit="return checkAgreement();
function checkAgreement() {
  const agreementCheckbox = document.querySelector("#agreement");

  // 檢查核取方塊是否被勾選
  if (!agreementCheckbox.checked) {
    alert("請先確認同意條款");
    return false;
  }

  return true;
}
