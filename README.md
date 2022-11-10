# FeaturesDetection-Matching

A small recap about how to proceed features detection on images
![Screenshot from 2022-11-10 16-10-52](https://user-images.githubusercontent.com/79518374/201132940-410c23da-8024-4bd6-8a94-e5b40b48ace0.png)

Today, thanks to openCV ressources we don't need to manually implement algorithms and mathematical methods to detect the significant features on an image
Let's see some of these, on this image :  
![image](https://user-images.githubusercontent.com/79518374/201133734-d6c6f445-7f6f-496e-bd2f-10277d271e82.png)


FEATURES DETECTION : 

      -Harris' corner detection : (based on Harris and Stephen’s method) 
        --Code explanation : 
            img = cv2.imread('monkey.jpg')
                → we load the wished image
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                → we change the color, now it’s only in tones of grey ( black and white)
            gray_img = np.float32(gray_img)
                → convert the image in an array of pixel
            dst = cv2.cornerHarris(gray_img, blockSize=2, ksize=3, k=0.04)
                → run the Harris detection on the previous image, with neighborhood’s size equal to 2 and k the value alpha in the Harris formula
            dst = cv2.dilate(dst, None)
                → use to keep size of image after the operation of the cornerharris function
            img[dst > 0.01 * dst.max()] = [0, 255, 0]
                → give the coordinates of the image’s corners
            cv2.imshow('haris_corner', img)
            cv2.waitKey()
                → show the corners on the image
![image](https://user-images.githubusercontent.com/79518374/201133802-08455603-c1ee-4074-9935-3052e607d1dc.png)


      -SIFT (Scale-Invariant Feature Transform) :
 ![image](https://user-images.githubusercontent.com/79518374/201134015-29dbbce9-bb43-4829-8ed8-5ca5efa4ee8a.png)
          The resulting image has circles depicting the key points/features, where size of the circle represents the strength of the key point and the line inside the circle denotes the orientation of the key point.


      -FAST algorithm for corner detection :
![image](https://user-images.githubusercontent.com/79518374/201134250-c02edd2a-fcde-42ee-91ed-58c54b8b45f8.png)
          This algorithm was introduced with reduced processing time. 
          However FAST gives only the key points and we may need to compute descriptors with other algorithms like SIFT to obtains further informations.
          As you can see we have too many point on the outputed image!
          
          
     -ORB (Oriented FAST and Rotated Brief) :
![image](https://user-images.githubusercontent.com/79518374/201134722-49d63a33-6875-4902-8a86-a1fb9ff1cba7.png)
          ORB is an efficient open source alternative to SIFT and SURF. It computes less key points when compared to SIFT and SURF but they are effective. 
          It uses FAST and BRIEF techniques to detect the key points and compute the image descriptors respectively.    
          
          
      -Other methods :
          -Shi
          -SURF
          -...
          
          
          
          
KEYPOINT MATCHMING (between several images) :
      -Brute-Force matching :
      It matches the descriptor of a feature from one image with all other features of another image and returns the match based on the distance. 
      Due to this it’s slow, as it checks match with all the features.
      
            --Brute-Force matching after orb detection 
![image](https://user-images.githubusercontent.com/79518374/201135637-5898988b-42a0-4779-a868-3965cde28e04.png)
     
            --Brute-Force matching after SIFT detection 
![image](https://user-images.githubusercontent.com/79518374/201135739-81aa88f1-fd0c-480d-ba22-10a13d23bf62.png)


       -FLANN matching : 
        It means Fast Library for Approximate Nearest Neighbors.
        And it’s optimised to find the matches with search even with large datasets hence its fast when compared to Brute-Force matcher.

             --FLANN combine with orb detection 
![image](https://user-images.githubusercontent.com/79518374/201136120-3482a22d-8a13-4d3c-a9c3-84e09871e1f2.png)
             
             --FLANN combine with SIFT method
![image](https://user-images.githubusercontent.com/79518374/201136186-ae270c66-cb17-4bfe-9d1b-e8b86f03cce2.png)

         We can see that it seems we found more key points than the BF, so a bad point. 
         But we must consider that we have more control on the accuracy of the key points, as we can control the parameter of the neighborhood  seen is the following line « if m.distance < 0.3*n.distance: ». 
         By adjusting the value before n.distance we will find less or more points, and less or more lines.
         
              Some further explanations : 
                for i,(m,n) in enumerate(matches):
                  if m.distance < 0.7*n.distance:
                      matchesMask[i]=[1,0]
              In these lines we must explain the choice of ‘0.7’. 
              Indeed this matching strategy remain on setting a threshold and returning all matches from other images within this threshold.
              So the value of the threshold is important, it must to be small to maintainaccuracy.conserver la precision 
              
                --> To find the best value I took the bikes collection of distorted images. 
                If I run the program with 2.4 it contain a lot of error when yu compare the images two by two : 
![image](https://user-images.githubusercontent.com/79518374/201137515-cca2399d-88da-4450-a43a-f419a29cfb7e.png)
                These image were obtained by comparing the first image with the twoth, and the fiveth with the sixth. 
                As you can see there are a lot of key points but the matching contain lot of errors, we see it through the green lines which are not horizontal.
                To solve this problem we need to put a lower value. I found that the best value was 0.4. 
                It’s the best value to avoid errors and maintain a good number of key points.
                Even if we lost few points, there are no more errors : 
![image](https://user-images.githubusercontent.com/79518374/201137826-28ab4203-b963-41da-b32e-5a3f2b3df28f.png)
Comparison between images 1 and 2

![image](https://user-images.githubusercontent.com/79518374/201137859-5c85a41d-c9bf-490a-9797-338d0692215e.png)
Comparison between images 5 and 6

