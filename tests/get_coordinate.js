// Optimal adresse : 1 rue de la paix, 75002, Paris
const get_coordinates = (adresse) => {
  try {
    fetch(`https://api-adresse.data.gouv.fr/search/?q=${adresse}`)
      .then((response) => response.json())
      .then((data) => {
        return data.features[0].geometry.coordinates;
      });
  } catch (error) {
    return error;
  }
};
