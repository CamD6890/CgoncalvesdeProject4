import arcade
myWindow = arcade.open_window(1800, 800, "Population of the largest pop Nations on Earth")

arcade.set_background_color(arcade.color. LILAC)

arcade.start_render()
arcade.draw_line(160, 130, 160, 800, arcade.color.BLACK)    # y-axis
arcade.draw_line(160, 130, 1200, 130, arcade.color.BLACK)    # x-axis

my_file = open("nationsPop.txt", "r")
CountryData = my_file.readlines()
print(CountryData)


scaleY = (800 - 160) / len(range(100, 1500, 100))
scaleX = (800 - 160) / (len(CountryData) + 1)

for idx, elt in enumerate(range(100, 1500, 100)):
    currentLabel = arcade.Text(f"{elt}M", 100, idx * scaleY + 160, arcade.color.BLACK)
    currentLabel.draw()


for idx, Country in enumerate(CountryData):
    Nation_split = Country.strip().split(",")
    country_split = Country.split(",")
    Name = country_split[0]
    pop = int(country_split[1])
    growth = float(country_split[2])
    countryLabel = arcade.Text(Name, idx * scaleX + 160, 115, arcade.color.BLACK)
    countryLabel.rotation = -45
    countryLabel.draw()
    color = arcade.color.RED
    bar_height = (int(pop)-100_000_000)/1_000_000
    neg_color = arcade.color.ROYAL_BLUE
    pos_color = arcade.color.RED
    if growth < 0:
        arcade.draw_xywh_rectangle_filled(idx * scaleX + 160, 130, 20, bar_height, neg_color)
    else:
        arcade.draw_xywh_rectangle_filled(idx * scaleX + 160, 130, 20, bar_height, pos_color)


arcade.finish_render()
arcade.run()
