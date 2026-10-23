from blockchain import *
from steganography import *


# 1. Hide data in image
hide_data_in_image('user_1.jpg', 'Secret Message', 'stegged_image.jpg')

# 2. Open and read the stegged image
with open('stegged_image.jpg', 'rb') as img_file:
    stegged_image_data = img_file.read()

# 3. Add stegged image to the blockchain
blockchain = Blockchain()
blockchain.add_block(stegged_image_data)

# Print the blockchain data (in this case, image data in each block)
for block in blockchain.chain:
    print(f"Block {block.index} | Data: {block.data[:20]}... | Hash: {block.hash}")

hidden_message = retrieve_data_from_image('stegged_image.jpg')
print(f"Hidden message: {hidden_message}")

