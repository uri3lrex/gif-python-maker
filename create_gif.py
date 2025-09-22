import imageio.v3 as iio
# adding the files

filenames = ['team-pic1.png', 'team-pic2.png']
images = []

# adding a loop to read the images using imageio
# imread loads image based on file path
# images has the pictures

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop= 0)

