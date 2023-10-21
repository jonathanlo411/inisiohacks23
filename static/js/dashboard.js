
let msg;
let currentTime = new Date().getHours()
if (currentTime < 11) {
    msg = "Good morning,"
} else if (currentTime < 16) {
    msg = "Good afternoon,"
} else {
    msg = "Good evening,"
}
let welcome = document.getElementById("welcome-msg")
welcome.innerHTML = msg + welcome.innerHTML