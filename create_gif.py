import imageio.v3 as iio
from pathlib import Path

# adding the files

#filenames = ['team-pic1.png', 'team-pic2.png']
filenames = sorted(Path(".").glob("*.png"))
images = [iio.imread(f) for f in filenames]

# adding a loop to read the images using imageio
# imread loads image based on file path
# images has the pictures

#for filename in filenames:
  #  images.append(iio.imread(filename))

iio.imwrite('team_auto.gif', images, duration = 500, loop= 0)

