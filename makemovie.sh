# must be called from the experiment's root directory, which should contain all the images in
# a folder called "stills".

# create the video
# This specifies the framerate, rather than the duration. 
ffmpeg -framerate 40 -i stills/img_%03d.png -c:v libx264 -r 30 -pix_fmt yuv420p movie.mp4

# This specifies a 10 second long video. 
#ffmpeg -t 10 -i stills/img_%03d.png -c:v libx264 -pix_fmt yuv420p movie.mp4

# delete the stills directory, and all the images within.
#rm -r stills
