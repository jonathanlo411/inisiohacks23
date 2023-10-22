
document.getElementById("pfp").addEventListener("click", () => {
    document.getElementById("profile").style.display = "block";
    document.getElementById("overlay-pfp").style.display = "block";
});

document.getElementById("overlay-pfp").addEventListener("click", function() {
    // Hide the modal and overlay when clicking outside of the modal
    document.querySelector("#profile").style.display = "none";
    document.getElementById("overlay-pfp").style.display = "none";
});