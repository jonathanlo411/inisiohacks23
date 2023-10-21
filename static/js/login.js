
// Login Logic
document.getElementById("submit"),addEventListener("submit", async (e) => {
    // Prevent page from reloading
    e.preventDefault();

    // Obtain user's username and password
    let username = document.getElementById("username");
    let password = document.getElementById("password");

    if (username.value == "" || password.value == "") {
        raiseError("Username or Password Empty")
    } else {
        // Submit user's information
        const payload = {
            "username": username.value,
            "password": password.value
        }
        let res = await fetch("/login", {
            method: "POST",
            credentials: "same-origin",
            body: JSON.stringify(payload),
            headers: { "Content-Type": "application/json" }
        })

        // Handle User Submissions
        if (res.success) {
            // Redirect to dashboard
        } else {
            raiseError((res.message) ? res.message : "Something went wrong!")
        }
    }
})

// Loads error onto user's DOM
function raiseError(msg) {
    console.log("here")
    let errorTarget = document.getElementById("error-box")
    errorTarget.innerHTML = msg;
    errorTarget.style.display = "block";
}