# Use ffmpeg:
ffmpeg -framerate 5 -pattern_type glob -i 'GOES16_b_14_2023*.png' -c:v libx264 -r 5 -pix_fmt yuv420p Franklin_2023.mp4
