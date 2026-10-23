from stealthledger import *
import os
import time

txt_filenames = os.listdir("test_dataset_1/data_to_hide")
txt_files = [f for f in txt_filenames if f.endswith(".txt")]
# print(txt_files)

img_filenames = os.listdir("test_dataset_1/images")
img_files = [f for f in img_filenames if f.endswith(".jpg")]
# print(img_files)

pswd_filenames = os.listdir("test_dataset_1/passwords")
pswd_files = [f for f in pswd_filenames if f.endswith(".txt")]
# print(pswd_files)

test_ledger = StealthLedger("test_ledger", 'jpg')

hiding_times = []
for i in range(383,420):
    with open(f"test_dataset_1/data_to_hide/{txt_files[i]}", 'r') as data_to_hide_file, open(f"test_dataset_1/passwords/{pswd_files[i]}", 'r') as pswd_file:
        data_to_hide = data_to_hide_file.read()
        pswd = pswd_file.read()

        st = time.time()
        x = test_ledger.add_node(data_to_hide, f"test_dataset_1/images/{img_files[i]}", f"id_{str(img_files[i])[:-4]}", pswd)
        et = time.time()
        hiding_times.append(et-st)

        x.save(f"test_dataset_1/steged_images/steged_{img_files[i]}")

print(hiding_times)
print("avg = ", sum(hiding_times)/len(hiding_times))

print(test_ledger.blockchain.is_chain_valid())

print("done")