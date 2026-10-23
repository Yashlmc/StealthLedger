import os
from lorem import sentence

# Define the target size for each file (in bytes)
TARGET_SIZE = 1 * 1024

# Create a directory for the files
output_dir = "test_dataset_3/data_to_hide"
os.makedirs(output_dir, exist_ok=True)

# Function to generate approximately 5 KB of text
def generate_random_text(size):
    content = []
    while len(" ".join(content).encode("utf-8")) < size:
        content.append(sentence())  # Add a random sentence until target size is reached
    return " ".join(content)

# Generate 420 files with 3-digit numbering
for i in range(1, 211):
    file_name = f"text_{str(i).zfill(3)}.txt"  # Pad the number with zeros
    file_path = os.path.join(output_dir, file_name)
    
    # Generate text of approximately TARGET_SIZE bytes
    random_text = generate_random_text(TARGET_SIZE)
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(random_text)

print(f"420 text files, each ~3.5 KB, created in '{output_dir}' directory.")


# import os
# import random
# import string

# # Define password length
# PASSWORD_LENGTH = 12

# # Create a directory for password files
# password_dir = "test_datasets/passwords"
# os.makedirs(password_dir, exist_ok=True)

# # Function to generate a random password
# def generate_password(length):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     return ''.join(random.choices(characters, k=length))

# # Generate 420 password files with 3-digit numbering
# for i in range(1, 421):
#     file_name = f"pswd_{str(i).zfill(3)}.txt"  # Pad the number with zeros
#     file_path = os.path.join(password_dir, file_name)
    
#     # Generate a random password
#     password = generate_password(PASSWORD_LENGTH)
    
#     with open(file_path, "w", encoding="utf-8") as file:
#         file.write(password)

# print(f"420 password files created in '{password_dir}' directory.")

