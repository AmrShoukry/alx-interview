#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

const actors = [];

request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;
  const len = characters.length;
  for (let i = 0; i < len; i++) {
    request(characters[i], (error2, response, body2) => {
      if (error2) {
        console.error('Error fetching data:', error2);
        return;
      }

      const data2 = JSON.parse(body2);
      actors.push({ i, name: data2.name });

      if (actors.length === len) {
        actors.sort((a, b) => parseInt(a.i) - parseInt(b.i));

        for (const actor of actors) {
          console.log(actor.name);
        }
      }
    });
  }
});

