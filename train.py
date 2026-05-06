from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("yolo11n.pt")

    results = model.train(
        data="C:/Users/wangjunyi/Desktop/FallDataset/data.yaml",
        epochs=100,
        imgsz=640,
        batch=16,
        device=0,
        workers=0,
        name="fall_detect",
        patience=20,
    )

    print("Training complete!")
