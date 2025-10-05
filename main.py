#!/usr/bin/env python3

from ultralytics import YOLO
import os

def deteksi_file():
    print("\n=== DETEKSI FILE ===")
    source = input("Masukkan path file (gambar/video): ").strip()
    
    if not os.path.exists(source):
        print(f"Error: File '{source}' ga ditemukan!")
        return
    
    model_name = input("Model YOLO (default: yolov8n.pt): ").strip()
    if not model_name:
        model_name = "yolov8n.pt"
    
    print(f"\nLoading model: {model_name}...")
    model = YOLO(model_name)
    
    print(f"Running detection on: {source}...")
    results = model.predict(
        source=source,
        save=True,
        show=False
    )
    
    # Print hasil
    print("\n=== Hasil Deteksi ===")
    for i, result in enumerate(results):
        print(f"\nFrame/Image {i+1}:")
        if len(result.boxes) > 0:
            for box in result.boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                label = model.names[cls]
                print(f"  - {label}: {conf:.2f}")
        else:
            print("  Ga ada objek terdeteksi")
    
    print(f"\nHasil disimpan di: runs/detect/predict/")

def deteksi_langsung():
    """Deteksi langsung dari kamera"""
    print("\n=== DETEKSI LANGSUNG (KAMERA) ===")
    
    camera_id = input("Camera ID (default: 0): ").strip()
    if not camera_id:
        camera_id = "0"
    
    model_name = input("Model YOLO (default: yolov8n.pt): ").strip()
    if not model_name:
        model_name = "yolov8n.pt"
    
    print(f"\nLoading model: {model_name}...")
    model = YOLO(model_name)
    
    print(f"Starting live detection from camera {camera_id}...")
    print("Tekan 'q' untuk keluar\n")
    
    # Run live detection
    model.predict(
        source=int(camera_id),
        show=True,
        stream=True
    )

def main():
    print("="*50)
    print("   YOLO OBJECT DETECTION")
    print("="*50)
    
    while True:
        print("\nPilih mode deteksi:")
        print("1. Deteksi File (Gambar/Video)")
        print("2. Deteksi Langsung (Kamera)")
        print("3. Exit")
        
        pilihan = input("\nPilihan (1/2/3): ").strip()
        
        if pilihan == "1":
            deteksi_file()
        elif pilihan == "2":
            deteksi_langsung()
        elif pilihan == "3":
            print("\nTerima kasih! Bye bro!")
            break
        else:
            print("\nPilihan ga valid! Pilih 1, 2, atau 3")
        
        if pilihan in ["1", "2"]:
            input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan. Bye bro!")