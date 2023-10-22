
let currentTime = new Date().getHours()
if (currentTime < 11) {
    msg = "Good morning, "
} else if (currentTime < 16) {
    msg = "Good afternoon, "
} else {
    msg = "Good evening, "
}
let welcome = document.getElementById("welcome-msg")
welcome.innerHTML = msg + welcome.innerHTML

// Add Card Openners
musicCards = document.querySelectorAll(".music-card")
musicCards.forEach(element => {
    element.addEventListener("click", () => {
        let id = element.id.replace("music-card-", "")
        const modal = document.getElementById(`modal-${id}`)
        const overlay = document.getElementById(`modal-overlay-${id}`)
        modal.style.display = "flex";
        overlay.style.display = "block";
        document.querySelector("body").style.overflow = 'hidden';
    })
});

// Add Overlay Closers
const modalOverlays = document.querySelectorAll(".modal-overlay")
const modals = document.querySelectorAll(".modal")
modalOverlays.forEach(element => {
    element.addEventListener("click", () => {
        modals.forEach(modal => {
            modal.style.display = "none";
        })
        element.style.display = "none";
        document.querySelector("body").style.overflow = 'visible';
    })
});