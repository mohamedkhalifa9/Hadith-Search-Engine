window.addEventListener("scroll", () => {
    
    if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight) {
        getHadith(); 
        console.log(5)
    }
});

function getHadith() {
    clientResults.splice(0,25)
    console.log(clientResults.length)
    for (let index = 0; index < 25; index++) {
        let li= document.createElement('li')
        let p= document.createElement("p")
        li.appendChild(p)

        p.innerText = clientResults[index].hadith
        p.classList.add("text-gray-700", "font-medium")
        li.classList.add("bg-white" ,"shadow-md", "rounded-lg", "p-4")

        document.getElementById("results-container").appendChild(li)
        
    }

}