
window.addEventListener("load", async () => {

    // Get Music ID from params
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);

    
    // Load Music Sheet
    let rawMusic = await fetch('/api/music', {
        method: 'GET',
        body: JSON.stringify({
            musicID: urlParams['id']
        })}
    )
    console.log(rawMusic)

    tab = `
        tabstave notation=true clef=treble key=C tablature=false
        notes Cn-C-G/4 G/4 | An-A-G/4 F/4 |
        tabstave notation=true clef=treble key=C tablature=false
        notes E-E-D/4 D/4 | G-G-F/4 F/4 | 
        tabstave notation=true clef=treble key=C tablature=false
        notes E-E-D/4 D/4 | Cn-C-G/4 G/4 | 
        tabstave notation=true clef=treble key=C tablature=false
        notes Cn-C-G/4 G/4 | An-A-G/4 F/4 |
        tabstave notation=true clef=treble key=C tablature=false
        notes E-E-D/4 D/4 | G-G-F/4 F/4 | 
        tabstave notation=true clef=treble key=C tablature=false
        notes E-E-D/4 D/4 | Cn-C-G/4 G/4 |     
    `
    // Create VexFlow Renderer element with id #boo.
    rendererPageOne = new Vex.Flow.Renderer($('#pageOne')[0], Vex.Flow.Renderer.Backends.SVG);
    artistOne = new Artist(10, 30, 800, {scale: 0.7});
    new VexTab(artistOne).parse(tab)
    artistOne.render(rendererPageOne);

    // Remove Vexflow P1 tag
    let item = document.querySelectorAll("svg text")
    item[item.length - 1].remove()

    // Create VexFlow Renderer element with id #boo.
    rendererPageTwo = new Vex.Flow.Renderer($('#pageTwo')[0], Vex.Flow.Renderer.Backends.SVG);
    artistTwo = new Artist(10, 30, 800, {scale: 0.7});
    new VexTab(artistTwo).parse(tab)
    artistTwo.render(rendererPageTwo);

    // Remove Vexflow P2 tag
    item = document.querySelectorAll("svg text")
    item[item.length - 1].remove()

})

