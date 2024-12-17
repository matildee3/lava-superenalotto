import cv2
import hashlib
import time
import random

# Function to hash an image using SHA-1
def hash_image(image):
    #image-to-byte
    image_bytes = image.tobytes()
    hash_object = hashlib.sha1(image_bytes) #SHA-1 of the bytes
    return hash_object.hexdigest()

def hash_to_number(hash_value):
    hash_int = int(hash_value, 16)
    return (hash_int % 90) + 1 #hash-to-int (1-90)


cap = cv2.VideoCapture(0)  #1 for phone

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()


frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS)) if cap.get(cv2.CAP_PROP_FPS) > 0 else 20


fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
out = cv2.VideoWriter('lava.mp4', fourcc, fps, (frame_width, frame_height))
print("\n\n")
print("Capturing video of the lava lamp and generating random numbers to play at Superenalotto! 💸💸💸 \n\n")




start_time = time.time()
hash_intervals = [10, 20, 30, 40, 50, 60] #frame every 60 sec
hash_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame from video stream.")
        break

    out.write(frame)


    elapsed_time = time.time() - start_time
    if hash_count < len(hash_intervals) and elapsed_time >= hash_intervals[hash_count]:
        random_hash = hash_image(frame)  # Generate a random number by hashing the image
        random_number = hash_to_number(random_hash)


        print(f"Random squence {hash_count + 1}: {random_hash}")
        print(f"--> corresponding number for Superenalotto: {random_number}")

        hash_count += 1

    if elapsed_time >= 60:
        break

cap.release()
out.release()
print("\n")
print("Process completed!")
print("Good luck! 🍀")
