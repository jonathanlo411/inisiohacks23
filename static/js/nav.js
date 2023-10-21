
document.getElementById("pfp").addEventListener("click", () => {
    document.getElementById("profile").style.display = "block";
    document.getElementById("overlay").style.display = "block";
});

document.getElementById("overlay").addEventListener("click", function() {
    // Hide the modal and overlay when clicking outside of the modal
    document.querySelector(".modal").style.display = "none";
    document.getElementById("overlay").style.display = "none";
});