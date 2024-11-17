#!/usr/bin/env node  

const axios = require('axios');  

// Recursive function to fetch character names from their URLs  
const fetchCharacterNames = async (urls, index) => {  
    if (index >= urls.length) return; // Base case for recursion  

    try {  
        const response = await axios.get(urls[index]);  
        console.log(response.data.name); // Print character name  
        await fetchCharacterNames(urls, index + 1); // Recur for the next character  
    } catch (error) {  
        console.error('Error fetching character data:', error.message);  
    }  
};  

// Check for a valid movie ID  
const movieId = process.argv[2];  
if (!movieId || isNaN(movieId)) {  
    console.error('Please provide a valid movie ID as a numeric argument.');  
    process.exit(1); // Exit if invalid ID  
}  

// Fetch film data to get character URLs  
axios.get(`https://swapi-api.hbtn.io/api/films/${movieId}`)  
    .then(response => {  
        const characters = response.data.characters; // Extract character URLs  
        return fetchCharacterNames(characters, 0); // Start fetching character names  
    })  
    .catch(error => {  
        console.error('Error fetching film data:', error.message);  
        process.exit(1); // Exit on error  
    });
