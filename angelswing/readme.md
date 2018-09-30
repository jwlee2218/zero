# Find contours of given image(tif file) and convert it into svg file!
Though the codes are rather simple, I took these steps to finally make the first success file.

It felt a bit unfair to only present result file so that I upload it online


## edge detection 1
Found edges of given image easily with 'canny edge detector'. 

Also found the way to create svg file with python.

Thought it was the end of the project

But the results were 'path.svg' and 'path2.svg'

Found document about making svg file was converting only the largest contour but canny edges were too thin to vectorize


## edge detection 2
Converted given image into black and white only image.

Got the star shaped figure correct while the others were not making the contours but only silhouettes.

Moreover, the image itself is considered as a figure and a large rectangular box is drawn but I couldn't notice it.

Anyway, it was the most successful work until I got the first success file


## edge detection 3
Made canny edge, drew contours on it and thickened the edges.

Drew another contours to make edges visible but those were too thin again.

Repeated similar attempts until 'edge detection 6'

## edge detection 7
First success file.

## second success
Managed to make the code even simple and neat by vectorizing the contours of canny edge.

Detail(maybe not that much) description in written with the code. 
