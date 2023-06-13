# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 21:48:41 2023

@author: Harmann
"""
import cv2
import argparse


def motion_detection(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Create a background subtractor object
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()

    while True:
        # Read the current frame
        ret, frame = cap.read()
        
        
    
        # If the frame could not be read, exit the loop
        if not ret:
            break
        
        # Apply background subtraction
        fg_mask = bg_subtractor.apply(frame)

        # Threshold the foreground mask
        _, thresh = cv2.threshold(fg_mask, 128, 255, cv2.THRESH_BINARY)

        # Find contours of the thresholded image
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Iterate over the contours and draw bounding rectangles around the moving objects
        for contour in contours:
            if cv2.contourArea(contour) < 1000:  # Adjust the minimum contour area as needed
                continue
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the resulting frame and foreground mask
        cv2.imshow("Frame", frame)
        cv2.imshow("Foreground Mask", fg_mask)

        # Check for the 'q' key to exit the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close the windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Motion Detection on Video')

    # Add an argument for the video path
    parser.add_argument('video_path', type=str, help='Path to the video file')

    # Parse the arguments
    args = parser.parse_args()

    # Call the motion detection function with the provided video path
    motion_detection(args.video_path)

