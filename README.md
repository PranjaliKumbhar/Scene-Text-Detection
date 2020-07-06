# Scene-Text-Detection
Scene Text Detection using stroke width property 

Our proposed work of text detection consists of three phases:
1) Edge detection include two steps: 
   (1.1) Convert RGB (3 channel) image into grey (1 channel) image. 
   (1.2) Apply canny edge detection method 
   (1.3) Edge extraction using vertical and horizontal projection by Sobel projection. 
2) MSER region detection.
3) Apply geometric properties like aspect ratio, occupation, stroke width variance.
4) Character region detection and bounding box generation.
  4.1) find stroke width ratio.
  4.2) Binarize the image.
  4.3) Dilate image and find contours.  
  
A. Edge detection 
In this work, first original RGB image is converted into grey image for easy processing. Apply canny edge detection to get edge strokes. 
The edge is extracted by vertical and horizontal projection by sobel operation.

1) Canny edge detection method: 
Canny edge operator identifies edges in an image. Also, to extract useful structural information canny operator is required. 
It finds the intensity gradient of the image. Edges computed as follow: 
Edge_Gradient (G) = |𝐺𝑥| + |𝐺𝑦| 
Where Gx value for the 1st derivation in the horizontal direction and vertical direction (Gy). 

2) Edge extraction using sobel operator: 
There are many techniques are there too extract edges but, in this work, we have used sobel technique. 
Sobel operator produce more perfect edges in different orientation. Also, we have calculated X and Y gradient using sobel operator. 

B. MSER region detection 
By using MSER technique we have detected maximum stable regions. It retrieves a number of co-variant regions. In this technique, image I is a set of {0….255} number. 
I indicate as: I : D ⊂ Z2 → {0…255} 
Region Q denotes continuous subset of D. Extremal region is denoted as  Q subset of D as follow:  
(Above statement is indicating for maximum intensity region) 

C. Character region detection  
In this last phase, stroke widths are calculated, and resultant image is binarized. 
Binarization is the process of finding threshold value and assign them as 1 or 0 (background or text object).
After binarization, image is dilated. Dilation is used to join the broke part of text. 
It connects the edges into cluster. Also, it reduces the noise and increases the white region in the image. 
Dilated image is given as input to contour method to find the points that have same intensity. Also, it joins all the points along with boundary of an image. 
This contour method is useful to produce bounding box around the interest of area (i.e. text region)

D. Algorithm 
Algorithm: Text detection using MSER and stroke width 
Step 1: Convert the input RGB image in gray image. 
Step 2: Apply the Sobel projection on grey image. 
Step 3: Compute maximally stable extremal regions (MSER) of RGB image. 
Step 4: Apply geometric features like aspect ratio, compactness on MSER regions. 
Step5:  Find stroke width variance ratio of grey image on which Sobel projection is applied. 
Step 6: Binarized the grey image. 
Step 7: Dilate the binarized image and find contours in dilated image. 
Step 8: Draw the bounding boxes around contoured area where text is present. 
Step 9: Finally, bounding box generated around text. 
















