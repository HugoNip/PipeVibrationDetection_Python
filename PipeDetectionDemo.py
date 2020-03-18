import MR
import matplotlib.pyplot as plt
import cv2
import numpy as np
import os
import glob



# path
video_dir = './Video_Source/'
img_dir = './Frames_Source/'
sal_des = './Frames_Saliency/'
edge_des = './Frames_Edge/'

video_path = os.path.join(video_dir,'C0002_Pipe.MP4')
frame_path = os.path.join(img_dir,'*jpg')

'''
################# Preparation #################
####### Convert Video to Images (Frames)#######
###############################################
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(video_path)
# Resolutions of the frame
# Convert the resolutions from float to integer.
frame_width = int(cap.get(3))
# print(frame_width)
frame_height = int(cap.get(4))
# print(frame_height)

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

i = 0
# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # Display the resulting frame
        cv2.imshow('Frame',frame)
        # Naming frames
        if i < 10: 
            frame_name = 'pipe000'+str(i)+'.jpg' # pipe0001.jpg
        elif i > 9 and i < 100:
            frame_name = 'pipe00'+str(i)+'.jpg' # pipe0011.jpg
        elif i > 99 and i < 1000:
            frame_name = 'pipe0'+str(i)+'.jpg' # pipe0111.jpg
        elif i > 999 and i < 10000:
            frame_name = 'pipe'+str(i)+'.jpg' # pipe1111.jpg
        else:
            break

        # Save frames
        cv2.imwrite(img_dir + frame_name, frame)
        # Press Q on keyboard to  exit
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    # Break the loop
    else: 
        break

    i += 1

# When everything done, release the video capture object
cap.release()
# Closes all the frames
cv2.destroyAllWindows()
'''


################# Preparation ##################
####### Convert Images (Frames) to Video #######
################################################
'''
fps = 30
frame_array = []
files = [f for f in os.listdir(img_dir) if os.path.isfile(os.path.join(img_dir, f))]

#for sorting the file names properly
files.sort(key = lambda x: x[4:])
files.sort()
frame_array = []
files = [f for f in os.listdir(img_dir) if os.path.isfile(os.path.join(img_dir, f))]

#for sorting the file names properly
files.sort(key = lambda x: x[4:])

for i in range(len(files)):
    filename = img_dir + files[i]
    #reading each files
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    
    #inserting the frames into an image array
    frame_array.append(img)

out = cv2.VideoWriter(video_dir + 'ReConvert.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()
'''

############################### Saliency detection and Edge detection ###############################

################### Case 1 ###################
### Read image from a video frame by frame ###
##############################################
'''
cap = cv2.VideoCapture(video_path)

# Resolutions of the frame
# Convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    # Naming frames
    if i < 10: 
        frame_name = 'pipe000'+str(i)+'.jpg' # pipe0001.jpg
    elif i > 9 and i < 100:
        frame_name = 'pipe00'+str(i)+'.jpg' # pipe0011.jpg
    elif i > 99 and i < 1000:
        frame_name = 'pipe0'+str(i)+'.jpg' # pipe0111.jpg
    elif i > 999 and i < 10000:
        frame_name = 'pipe'+str(i)+'.jpg' # pipe1111.jpg
    else:
        break

    # edge detection (not available)
    # edge = cv2.Canny(frame, cap.get(3), cap.get(4))
    # cv2.imwrite(edge_des + frame_name, edge)
    
    # Saliency Detection (7s per image, with resolution of 1920 * 1080)
    mr = MR.MR_saliency() # initialization
    sal = mr.saliency(frame)
    cv2.imwrite(sal_des + frame_name, sal)

    i+=1

# When everything done, release the video capture object
cap.release()
# Closes all the frames
cv2.destroyAllWindows()
'''


################### Case 2 ###################
########### Read image from folder ###########
##############################################
'''
files = glob.glob(frame_path)
# i = 0
for f1 in files:
    img = cv2.imread(f1)

    # Saliency Detection
    mr = MR.MR_saliency() # initialization
    sal = mr.saliency(img)

    save_name = f1[16:]
    print(save_name)
    cv2.imwrite(sal_des + save_name, sal)
'''


################### Case 3 ###################
########### Read image from Webcam ###########
##############################################
'''
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if ret == True:
        # Write the frame into the file 'output.avi'
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('Frame', frame)
        # Press Q on keyboard to  exit
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Break the loop
    else: 
        break

cap.release()
cv2.destroyAllWindows()
'''