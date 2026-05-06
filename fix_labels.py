import os

base = r"C:\Users\wangjunyi\Desktop\FallDataset"

for split in ('train', 'val'):
    label_dir = os.path.join(base, split, 'labels')
    for f in os.listdir(label_dir):
        if not f.endswith('.txt'):
            continue
        path = os.path.join(label_dir, f)
        with open(path, 'r') as fh:
            lines = fh.readlines()
        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if parts:
                parts[0] = '0'  # change class 1 to 0
            new_lines.append(' '.join(parts) + '\n')
        with open(path, 'w') as fh:
            fh.writelines(new_lines)

print("Fixed all labels!")
