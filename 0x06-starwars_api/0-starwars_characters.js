#!/usr/bin/node  

const request = require('request');  

// Recursive function to fetch character names from their URLs  
const req = (arr, i) => {  
    if (i >= arr.length) return; // Base case for recursion  
    request(arr[i], (err, response, body) => {  
        if (err) {  
            console.error('Error fetching character data:', err);  
            return; // Exit on error  
        }  
        const characterData = JSON.parse(body);  
        console.log(characterData.name); // Print character name  
        req(arr, i + 1); // Recur for next character  
    });  
};  

// Check for a valid movie ID  
const movieId = process.argv[2];  
if (!movieId || isNaN(movieId)) {  
    console.error('Please provide a valid movie ID as a numeric argument.');  
    process.exit(1); // Exit if invalid ID  
}  

// Fetch film data to get character URLs  
request(  
    `https://swapi-api.hbtn.io/api/films/${movieId}`,  
    (err, response, body) => {  
        if (err) {  
            console.error('Error fetching film data:', err);  
            return; // Exit on error  
        }  
        const filmData = JSON.parse(body);  
        const chars = filmData.characters; // Extract character URLs  
        req(chars, 0); // Start fetching character names  
    }  
);
