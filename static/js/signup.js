
// Login Logic
document.getElementById("submit"),addEventListener("submit", async (e) => {
    // Prevent page from reloading
    e.preventDefault();

    // Obtain user's information
    let username = document.getElementById("username");
    let displayName = document.getElementById("displayname");
    let password = document.getElementById("password");
    let passwordAuth = document.getElementById("password-auth");

    if (username.value == "" || password.value == "" || displayName == "" || passwordAuth == "") {
        raiseError("One or More Fields Empty")
    } else if (password.value != passwordAuth.value) {
        raiseError("Passwords Do Not Match")
    } else {
        // Submit user's information
        const payload = {
            "username": username.value,
            "password": password.value,
            "displayName": displayName.value
        }
        let res = await fetch("/signup", {
            method: "POST",
            credentials: "same-origin",
            body: JSON.stringify(payload),
            headers: { "Content-Type": "application/json" }
        })
        let data = await res.json()

        // Handle User Submissions
        if (data.success) {
            location.href = '/login'
        } else {
            raiseError((data.message) ? data.message : "Something went wrong!")
            console.log(res)
        }
    }
})

// Loads error onto user's DOM
function raiseError(msg) {
    let errorTarget = document.getElementById("error-box")
    errorTarget.innerHTML = msg;
    errorTarget.style.display = "block";
}