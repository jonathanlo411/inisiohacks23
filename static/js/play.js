
window.addEventListener("load", async () => {

    // Get Music ID from params
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    
    // Load Music Sheet
    let rawMusic = await fetch(`/api/music?id=${urlParams.get('id')}`, {
        method: 'GET'
    })
    let musicData = await rawMusic.json()
    console.log(musicData)

    // Preproccess music
    tab = "options width=1000";
    for (let i = 1; i < musicData['music-data'].length; i ++) {
        tab += `
            ${musicData['music-data'][0]}
            ${musicData['music-data'][i]}`
    }
    console.log(tab)
    
    // Create VexFlow Renderer element with id #boo.
    rendererPageOne = new Vex.Flow.Renderer($('#pageOne')[0], Vex.Flow.Renderer.Backends.SVG);
    artistOne = new Artist(10, 30, 800, {scale: 0.7});
    new VexTab(artistOne).parse(tab)
    artistOne.render(rendererPageOne);

    // Remove Vexflow P1 tag
    let item = document.querySelectorAll("svg text")
    item[item.length - 1].remove()

    // Inject name
    document.getElementById('score-title').innerHTML = musicData['score-name']

    // // Create VexFlow Renderer element with id #boo.
    // rendererPageTwo = new Vex.Flow.Renderer($('#pageTwo')[0], Vex.Flow.Renderer.Backends.SVG);
    // artistTwo = new Artist(10, 30, 800, {scale: 0.7});
    // new VexTab(artistTwo).parse(tab)
    // artistTwo.render(rendererPageTwo);

    // // Remove Vexflow P2 tag
    // item = document.querySelectorAll("svg text")
    // item[item.length - 1].remove()


//     const canvas = new fabric.Canvas('canvas');
//   const rect = new fabric.Rect({
//     top: 100,
//     left: 100,
//     width: 60,
//     height: 70,
//     fill: 'red',
//   });
//   canvas.add(rect);
})

