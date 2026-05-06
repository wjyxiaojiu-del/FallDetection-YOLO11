import os
import shutil
import random

random.seed(42)

base = r"C:\Users\wangjunyi\Desktop\FallDataset"
img_dir = os.path.join(base, "img")
txt_dir = os.path.join(base, "txt")

# Find paired files (have both image and label)
txt_files = {os.path.splitext(f)[0] for f in os.listdir(txt_dir) if f.endswith('.txt')}
img_files = []
for f in os.listdir(img_dir):
    name, ext = os.path.splitext(f)
    if ext.lower() in ('.jpg', '.jpeg', '.png', '.bmp') and name in txt_files:
        img_files.append(f)

print(f"Total paired samples: {len(img_files)}")

# Shuffle and split 80/20
random.shuffle(img_files)
split = int(len(img_files) * 0.8)
train_files = img_files[:split]
val_files = img_files[split:]

# Create output dirs
for split_name in ('train', 'val'):
    os.makedirs(os.path.join(base, split_name, 'images'), exist_ok=True)
    os.makedirs(os.path.join(base, split_name, 'labels'), exist_ok=True)

def copy_files(file_list, split_name):
    for f in file_list:
        name = os.path.splitext(f)[0]
        ext = os.path.splitext(f)[1]
        shutil.copy2(os.path.join(img_dir, f), os.path.join(base, split_name, 'images', f))
        shutil.copy2(os.path.join(txt_dir, name + '.txt'), os.path.join(base, split_name, 'labels', name + '.txt'))

copy_files(train_files, 'train')
copy_files(val_files, 'val')

print(f"Train: {len(train_files)}, Val: {len(val_files)}")
print("Done!")
