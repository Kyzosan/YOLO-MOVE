#!/bin/bash

echo "🚀 Memulai instalasi YOLOv8 Object Detection..."

echo "🔄 Update sistem..."
sudo apt update && sudo apt upgrade -y

if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 belum terinstal!"
    echo "Install dulu Python3 sebelum lanjut"
    exit
fi

if ! command -v pip &> /dev/null
then
    echo "🔧 Install pip..."
    sudo apt install -y python3-pip
fi

echo "📦 Install YOLOv8 (ultralytics)..."
pip install --upgrade pip
pip install ultralytics

chmod +x yolo_detect.py

echo "✅ Instalasi selesai!"
echo "Jalankan script dengan: python3 main.py"