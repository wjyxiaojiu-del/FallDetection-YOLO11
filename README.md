> **中文** | [English](README_en.md)

# 老人摔倒检测模型 - YOLO11

基于YOLO11训练的老人摔倒检测模型，可实时识别图片或视频中的摔倒行为。

## 模型性能

| 指标 | 值 |
|------|-----|
| Precision | 0.853 |
| Recall | 0.871 |
| mAP50 | 0.908 |
| mAP50-95 | 0.617 |

## 快速使用

```python
from ultralytics import YOLO

# 加载模型
model = YOLO("runs/detect/fall_detect-3/weights/best.pt")

# 检测图片
results = model("test.jpg")

# 检测视频
results = model("video.mp4")

# 实时摄像头检测
results = model(source=0)
```

## 训练数据

- 图片数量：4576张
- 类别：fall（摔倒）
- 训练集：3660张
- 验证集：916张

## 训练参数

- 模型：YOLO11n
- Epochs：100
- 图片尺寸：640
- Batch size：16
- GPU：RTX 3060 Laptop

## 文件结构

```
FallDataset/
├── train.py          # 训练脚本
├── data.yaml         # 数据集配置
├── prepare_data.py   # 数据准备脚本
├── fix_labels.py     # 标签修复脚本
├── txt/              # YOLO格式标注
└── runs/detect/fall_detect-3/
    └── weights/
        ├── best.pt   # 最佳模型
        └── last.pt   # 最终模型
```

## 应用场景

- 老人居家监护
- 养老院智能监控
- 医院病房监测
- 智能摄像头集成

## 环境要求

- Python 3.8+
- PyTorch 2.0+
- Ultralytics 8.0+
- CUDA（可选，GPU加速）
