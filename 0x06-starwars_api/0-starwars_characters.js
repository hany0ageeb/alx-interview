#!/usr/bin/node
const process = require('node:process');
const https = require('node:https');
function getCharacter (idx, CHAR_URLS, len) {
  if (idx < len) {
    const CHAR_URL = CHAR_URLS[idx];
    https.get(CHAR_URL, res => {
      let data = '';
      res.on('data', chunk => {
        data += chunk;
      });
      res.on('end', () => {
        if (res.statusCode === 200) {
          const CHARACHTER = JSON.parse(data);
          console.log(CHARACHTER.name);
          getCharacter(idx + 1, CHAR_URLS, len);
        }
      });
    });
  }
}
if (process.argv.length === 3) {
  const FILM_ID = process.argv[2];
  https.get(`https://swapi-api.alx-tools.com/api/films/${FILM_ID}/`, res => {
    let data = '';
    res.on('data', chunk => {
      data += chunk;
    });
    res.on('end', () => {
      if (res.statusCode === 200) {
        try {
          const film = JSON.parse(data);
          const j = 0;
          getCharacter(j, film.characters, film.characters.length);
        } catch (err) {
          console.log(err);
        }
      }
    });
  });
}
