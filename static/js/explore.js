document.getElementById("recent").addEventListener("click", () => { sortModules("recent")});
document.getElementById("popular").addEventListener("click", () => { sortModules("popular")});
document.getElementById("top").addEventListener("click", () => { sortModules("top")});
document.getElementById("random").addEventListener("click", () => { sortModules("random")});

function compareUpvotes(a, b) {
    if (a > b) {
        return -1;
    } else if (a < b) {
        return 1;
    }
    // a must be equal to b
    return 0;
}

function compareDates(a, b) {
    if (parseInt(a) > parseInt(b)) {
        return -1;
    } else if (parseInt(a) < parseInt(b)) {
        return 1;
    }
    // a must be equal to b
    return 0;
}

function comparePercents(a, b) {
    if (a > b) {
        return -1;
    } else if (a < b) {
        return 1;
    }
    // a must be equal to b
    return 0;
}

function rearrangeGrid(sortedMusic) {
    const grid = document.querySelector("#music-scores-grid");
  
    // Clear the existing grid
    while (grid.firstChild) {
      grid.removeChild(grid.firstChild);
    }
  
    // Append the sorted music cards back to the grid
    sortedMusic.forEach((musicCard) => {
      grid.appendChild(musicCard);
    });
}
  

function sortModules(sortType) {
    const music_list = document.querySelectorAll(".music-card");
    const sorted_music = Array.from(music_list);

    // Map and sort the cards based on the selected sortType
    const sortedMusicCards = sorted_music.map((card) => ({
        card,
        key: card.dataset[sortType],
    }));

    if (sortType === "recent") {
        sortedMusicCards.sort((a, b) => compareDates(a.key, b.key));
    } else if (sortType === "popular") {
        sortedMusicCards.sort((a, b) => compareUpvotes(a.key, b.key));
    } else if (sortType === "top") {
        sortedMusicCards.sort((a, b) => comparePercents(a.key, b.key));
    } else {
        // Shuffle the sortedMusicCards array to sort randomly
        shuffleArray(sortedMusicCards);
    }

    // Extract the sorted cards from the objects
    const finalSortedMusic = sortedMusicCards.map((entry) => entry.card);

    // Rearrange the grid with the sorted cards
    rearrangeGrid(finalSortedMusic);
}

// Function to shuffle an array randomly
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
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