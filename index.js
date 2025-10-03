/* var express= require("express");
var app= express();
app.set("view engine", "ejs"); */

import express from "express";
import { ChromaClient } from "chromadb-client";
import { render } from "ejs";
import { pipeline } from '@huggingface/transformers';
const pipe = await pipeline('translation', 'Xenova/opus-mt-ar-en', { dtype: 'fp32' });


const output = await pipe("أحبك يا رسول الله");
console.log(output[0].translation_text);


const app = express();
app.set("view engine", "ejs");
app.use(express.static('public'));
app.listen(8080, function(){
    console.log("Server running on 8080!");
});


const client = new ChromaClient({ path: "http://localhost:8000" });

const collection = await client.getCollection({
      name: "muslim_hadiths"});

app.get("/", function(req, res) {
    
    
       
        res.render("home");
   
    
}); 

app.get("/search", async function(req,res){
   
    const searchQuery = req.query.q;
  
    console.log("User searched for:", searchQuery);
    const translation=  await pipe(searchQuery);
    console.log("Translation:", translation[0].translation_text);
    const english_query = translation[0].translation_text;
    const results = await collection.query({
        queryTexts: [english_query],
        nResults: 100
    });
    /* console.log("Results:", results); */
let scores=results.distances[0]
    console.log(scores.length)
    console.log(scores)
    const data = results.documents[0];
    console.log(data.length)
    let pairedResults = scores.map((score, index) => {
        return {
            score: score,
            hadith: data[index]
        };
    });
    pairedResults= pairedResults.filter(pair => pair.score - 1 <= 0.9)
    console.log(pairedResults.length)
    

    
    
    res.render("results", {
        searchQuery:searchQuery,
        results: pairedResults
    });
   

});


