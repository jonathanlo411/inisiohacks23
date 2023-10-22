
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

function playSong(id) { location.href = `/play?id=${id}` }
