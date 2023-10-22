
async function songVote(element, upvote) {
    let data = await fetch('/api/votes', {
        method: 'POST',
        body: JSON.stringify({
            musicID: element.dataset.id,
            upvote: upvote
        }),
        headers: { "Content-Type": "application/json" }
    })
}

async function updateStatus(element) {
    let status = element.parentElement.querySelector("select").value
    if (status === "-- Select --") return
    if (status === "Planned") status = "planned"
    if (status === "Working On") status = "working_on"
    if (status === "Mastered") status = "mastered"

    let data = await fetch('/api/scores', {
        method: 'POST',
        body: JSON.stringify({
            musicID: element.dataset.id,
            status: status
        }),
        headers: { "Content-Type": "application/json" }
    })
}


function playSong(id) { location.href = `/play?id=${id}` }
