# steganography.py

import os
import subprocess
import pickle
from PIL import Image
import cv2
import numpy as np


class Original_Image:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.ext = file_name[-3:]
        self.img_data = Image.open(file_name)

class Steged_Image:
    def __init__(self, img_data) -> None:
        self.img_data = img_data
    
    def save_img(self, file_name):
        self.img_data.save(f"{file_name}")

class Org_Steg_Image:
    pass


def hide_data_in_image(data, input_image, passcode):
    """
    Hide the username and password in the image using steghide.
    The hidden data is stored in the output image file.
    """
    
    # Write the hidden data to a temporary file
    with open("temp/temp.bin", "wb") as temp_file:
        pickle.dump(data, temp_file)

    input_image.img_data.save("temp/temp_input_image.jpg")
    
    # Use steghide to embed the data into the image
    command = ["steghide", "embed", "-cf", "temp/temp_input_image.jpg", "-ef", "temp/temp.bin", "-sf", "temp/temp_output.jpg", "-p", passcode]
    
    try:
        subprocess.run(command, check=True)
        print(f"Data hidden successfull.")
    except subprocess.CalledProcessError as e:
        print(f"Error hiding data: {e}")

    output_image = None
    with Image.open("temp/temp_output.jpg") as img:
        output_image = Steged_Image(img.copy())

    # Clean up the temporary file
    os.remove("temp/temp.bin")
    os.remove("temp/temp_input_image.jpg")
    os.remove("temp/temp_output.jpg")

    return output_image

def extract_data_from_image(steg_image_data, passcode):
    """
    Extract the hidden data from the steganographic image using steghide.
    """

    # img = cv2.imdecode(np.frombuffer(steg_image_data, np.uint8), cv2.IMREAD_COLOR)
    # cv2.imwrite("temp/temp_steg_img.jpg", img)

    with open("temp/temp_steg_img.jpg", "wb") as file:
        file.write(steg_image_data)

    outfile_name = "temp/out_bin.bin"
    
    # Use steghide to extract the hidden data from the image
    command = ["steghide", "extract", "-sf", "temp/temp_steg_img.jpg", "-xf", outfile_name, "-p", passcode]
    
    try:
        subprocess.run(command, check=True)
        # Read and print the extracted data
        with open(outfile_name, "rb") as file:
            hidden_data = pickle.load(file)
            print(f"Extracted Data:\n{hidden_data}")
        # Clean up the temporary extracted file
        os.remove(outfile_name)
        os.remove("temp/temp_steg_img.jpg")
        return hidden_data
    except subprocess.CalledProcessError as e:
        print(f"Error extracting data: {e}")
        return None

if __name__ == "__main__":
    # # Example usage with PIL Image
    # data = {"username":"user1", "password":"password123"}
    # input_image = Original_Image("user_1.jpg")
    
    # # Hide data
    # output_image = hide_data_in_image(data, input_image, "123")
    # output_image.save_img("output_img.jpg")

    # print("\nEmbedded\n")
    

    #
    # Extract data
    # steged_img = Original_Image("output_img.jpg")
    steged_img = "output_img.jpg"
    with open(steged_img, "rb") as file:
        steged_img_data = file.read()

    extracted_data = extract_data_from_image(steged_img_data, "123")
    if extracted_data:
        print(f"Successfully extracted data: {extracted_data}")
