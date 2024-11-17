#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

function fetchUrl (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

fetchUrl(url).then(async (filmData) => {
  const charList = filmData.characters;

  const charNames = await Promise.all(
    charList.map((charUrl) =>
      fetchUrl(charUrl).then((charData) => charData.name)
    )
  );

  charNames.forEach((name) => console.log(name));
}).catch(
  (err) => console.error(err));
