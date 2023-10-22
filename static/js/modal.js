
async function songVote(element, upvote) {
    let data = await fetch('/api/votes', {
        method: 'POST',
        body: JSON.stringify({
            musicID: element.dataset.id,
            upvote: upvote
        }),
        headers: { "Content-Type": "application/json" }
    })
    console.log(data)
}

async function updateStatus(element, status) {
    let data = await fetch('/api/scores', {
        method: 'POST',
        body: JSON.stringify({
            musicID: element.dataset.id,
            status: status
        }),
        headers: { "Content-Type": "application/json" }
    })
    console.log(data)
}


function playSong(id) { location.href = `/play?id=${id}` }
