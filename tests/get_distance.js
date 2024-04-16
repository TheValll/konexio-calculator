// mode : pedestrian, car
const get_distance = (latitude1, longitude1, latitude2, longitude2, mode) => {
  try {
    fetch(
      `https://wxs.ign.fr/calcul/geoportail/itineraire/rest/1.0.0/route?resource=bdtopo-pgr&profile=${mode}&optimization=fastest&start=${longitude1},${latitude1}&end=${longitude2},${latitude2}`
    )
      .then((response) => response.json())
      .then((data) => {
        return data[distance];
      });
  } catch (error) {
    return error;
  }
};
