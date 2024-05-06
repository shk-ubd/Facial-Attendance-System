# Facial Recognition Attendance System

## Overview
The Facial Attendance System is a comprehensive solution designed to streamline attendance tracking processes through facial recognition technology. Leveraging advanced computer vision and machine learning algorithms, this system automates attendance marking for known individuals, enhancing efficiency and accuracy. Key features include real-time facial detection, Firebase integration for seamless data management, and selective face capture to ensure security and reliability.

## Features
- **Facial Detection and Recognition:** Utilizes the `face_recognition` library with `dlib` for robust facial detection and recognition in real-time.
- **Real-time Attendance Marking:** Automatically marks attendance for recognized individuals, eliminating the need for manual tracking and reducing administrative burden.
- **Firebase Integration:** Leverages Firebase Realtime Database for storing student information and attendance records, enabling real-time updates and accessibility from anywhere.
- **Selective Face Capture:** Only known faces trigger attendance marking, enhancing security and preventing unauthorized access.
- **User Interface:** Provides visual feedback through different display modes, ensuring a seamless and intuitive user experience.

## Technical Details
- **Libraries Used:** `face_recognition`, `dlib`, `cv2` (OpenCV), `pickle`, `cvzone`, `firebase_admin`.
- **Backend Processing:** Facial features are encoded and stored during initialization using `face_recognition.face_encodings()` for efficient recognition during runtime.
- **Database Management:** Firebase Realtime Database stores student information, attendance records, and last attendance time, facilitating real-time updates and analysis.
- **Image Storage:** Firebase Cloud Storage is utilized for storing and retrieving student images, ensuring efficient image management and retrieval.

---
### Guide for Running the Project on Your PC

#### Cloning the Repository
1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command to clone the repository:

    ```
    git clone https://github.com/shk-ubd/Facial-Attendance-System.git
    ```

#### Setting Up the Environment
1. Navigate to the cloned repository directory.
2. Create a virtual environment by running the following command:

    ```
    python -m venv venv
    ```

3. Activate the virtual environment. On Windows, run:

    ```
    .\venv\Scripts\activate
    ```

    On macOS and Linux, run:

    ```
    source venv/bin/activate
    ```

#### Installing Dependencies
1. With the virtual environment activated, install the required dependencies by running the following command:

    ```
    pip install -r requirements.txt
    ```

    This command will install all the required Python packages listed in the `requirements.txt` file.

#### Running the Application
1. Once the dependencies are installed, you can run the application.
2. Navigate to the directory where your main Python script is located.
3. Run the script using Python.

    ```
    python main.py
    ```


That's it! You've successfully cloned the repository, set up the environment, installed dependencies, and run the application on your PC.

---

## Project Completion
Facial Attendance System Completed by Sheikh Ubaid Ullah as part of the final project of Artificial Intelligence in Software Engineering [CSSE-509] taught at University of Karachi.
