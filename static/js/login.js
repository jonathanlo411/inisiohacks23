
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
        console.log(payload)
        let res = await fetch("/login", {
            method: "POST",
            credentials: "same-origin",
            body: JSON.stringify(payload),
            headers: { "Content-Type": "application/json" }
        })
    }
})

// Loads error onto user's DOM
function raiseError(msg) {
    
}