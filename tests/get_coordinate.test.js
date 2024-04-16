const get_coordinates = require("./get_coordinates");

describe("get_coordinates", () => {
  test("returns coordinates for a valid address", async () => {
    const address = "1600 Amphitheatre Parkway, Mountain View, CA";
    const coordinates = await get_coordinates(address);
    expect(coordinates).toEqual([37.422408, -122.085608]);
  });

  test("throws an error for an invalid address", async () => {
    const address = "Invalid Address";
    await expect(get_coordinates(address)).rejects.toThrow();
  });
});
