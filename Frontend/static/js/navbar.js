var flag = 0;
icon = document.getElementById("drop_down_element");
element = document.getElementById("drop_down_element");
function showElement() {
  if (flag == 0) {
    element.style.visibility = "visible";
    flag = 1;
  } else {
    element.style.visibility = "hidden";
    flag = 0;
  }
}
