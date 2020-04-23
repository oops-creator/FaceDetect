# Facial-Recognition
Uses transfer learning on MobileNet model to recognize faces.
Employs cosine distance as a metric to find similarity between two images (image in 'database' and image currently being recognized).

To begin , create two folders named 'database' and 'imagesForDatabase' in the main folder.
To add 'check against' images to 'database' folder , first copy them to 'imagesForDatabase'. After copying, 
run 'createDatabase.py'. This will create facial crops of the people in original image using haar cascade.

To start 'recognizing' people, run app.py. This will open up file picker. Choose the image of person you want to recognize. It will show the person if found in the 'database'.
