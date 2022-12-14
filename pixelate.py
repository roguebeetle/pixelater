from PIL import Image
import webcolors


def pixelate(input_file_path, pixel_size, scale_depth):
    image = Image.open(input_file_path)
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )

    if image.width > 100 or image.height > 100:
        if image.height > image.width:
            factor = scale_depth / image.height
        else:
            factor = scale_depth/ image.width
        tn_image = image.resize((int(image.width * factor), int(image.height * factor)))

    image.save("pixelated.jpg")
    tn_image.save("scaled.jpg")

def pixelcalc():
    with Image.open("pixelated.jpg") as image:
        color_count = {}
        width, height = image.size
        rgb_image = image.convert('RGB')

        # iterate through each pixel in the image and keep a count per unique color
        for x in range(width):
            for y in range(height):
                rgb = rgb_image.getpixel((x, y))

                if rgb in color_count:
                    color_count[rgb] += 1
                else:
                    color_count[rgb] = 1

        print('Pixel Count per Unique Color:')
        print('-' * 30)
        color_index = 1
        for color, count in color_count.items():

            try:
                print('{}.) {}: {}'.format(color_index, webcolors.rgb_to_name(color), count))
            except ValueError:
                print('{}.) {}: {}'.format(color_index, color, count))
            color_index += 1

