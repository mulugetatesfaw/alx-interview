#!/usr/bin/node

const request = require('request');

// Function to recursively make requests to the provided URLs in the array
const req = (arr, i) => {
  // Base case: Stop recursion when all URLs have been processed
  if (i === arr.length) return;

  // Make a request to the URL at index 'i'
  request(arr[i], (err, response, body) => {
    if (err) {
      throw err;
    } else {
      // Print the name extracted from the response body
      console.log(JSON.parse(body).name);
      
      // Recursively call 'req' for the next URL in the array
      req(arr, i + 1);
    }
  });
};

// Make a request to the provided SWAPI film URL
request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (err, response, body) => {
    if (err) {
      throw err;
    } else {
      // Extract the character URLs from the response body
      const chars = JSON.parse(body).characters;
      
      // Initiate the recursive requests for character details
      req(chars, 0);
    }
  }
);
