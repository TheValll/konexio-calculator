const get_distance = require("./get_distance");

describe("get_coordinates", () => {
  test("returns coordinates for a valid address", async () => {
    const latitude1 = 37.7749;
    const longitude1 = -122.4194;
    const latitude2 = 37.7749;
    const longitude2 = -122.4194;
    const mode = "pedestrian";
    const distance = await get_distance(
      latitude1,
      longitude1,
      latitude2,
      longitude2,
      mode
    );
    expect(distance).toEqual(0);
  });

  test("throws an error for an invalid address", async () => {
    const latitude1 = 37.7749;
    const longitude1 = -122.4194;
    const latitude2 = 37.7749;
    const longitude2 = -122.4194;
    const mode = "invalid";
    await expect(
      get_distance(latitude1, longitude1, latitude2, longitude2, mode)
    ).rejects.toThrow();
  });
});
