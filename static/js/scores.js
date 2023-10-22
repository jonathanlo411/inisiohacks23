document.getElementById("all").addEventListener("click", () => { sortModules("all")});
document.getElementById("working-on").addEventListener("click", () => { sortModules("working-on")});
document.getElementById("planned").addEventListener("click", () => { sortModules("planned")});
document.getElementById("mastered").addEventListener("click", () => { sortModules("mastered")});


function sortModules(sortType) {
    const sortMap = {
        "all": "asd",
        "working-on": "cl-wo",
        "planned": "cl-pln",
        "mastered": "cl-ma"
    }
    let filteredDown = document.querySelectorAll(`.${sortMap[sortType]}`);
    musicCards = document.querySelectorAll(".music-card")
    musicCards.forEach(elem => {
        elem.style.display = 'flex'
    })
    filteredDown.forEach(elem => {
        elem.style.display = 'none'
    })
}

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