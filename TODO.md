Backlog
=======

+ 01: Take sequence, show the first image to the user, let them choose a coordinate
  and mark it with a yellow rectangle. size 16x16
  + 01.01: open sequence, show first image to user
  + 01.02: catch coordinates from mouse and print them
  + 01.03: Mark the area with a yellow rectangle.
  + 01.04: iterate through images in the sequence

+ 02: Using chosen region, iterate through sequence, and show results to user
  + 02.01: iterate over sequence and collect regions
  + 02.02: Create an image composed of all regions and show user
  + 02.03: update results based on new coordinates

+ 03: Save sequence to disk
  + 03.01: click 's' to save the sequence
  + 03.02: Save the results using the filename from the user, and exit.

- 04: Change utility to find blocks using matching algorithm
  - 04.01: use OpenCV to find a match in the next image
