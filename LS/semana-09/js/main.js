import flags from './model/flags.js';


for (const countryflags of flags) {
    const deck = document.querySelector('.deck');

    const card = createCountryFlagCard(countryflags);

    deck.insertAdjacentHTML('beforeend', card)

}

function createCountryFlagCard(countryflags) {
    return `<div class="flag col-2 my-2 text-center">
              <img src="${countryflags.image}" alt="${countryflags.name}">
              <p>${countryflags.name}</p>
            </div>`

}