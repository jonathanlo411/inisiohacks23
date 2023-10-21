
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
        let data = await res.json()

        // Handle User Submissions
        if (data.success) {
            // Redirect to dashboard
        } else {
            raiseError((data.message) ? data.message : "Something went wrong!")
            console.log(res)
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