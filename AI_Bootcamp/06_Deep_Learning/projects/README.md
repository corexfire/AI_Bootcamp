# Fashion MNIST Image Classification

Project ini membangun **Convolutional Neural Network (CNN)** untuk mengklasifikasikan gambar pakaian dari dataset **Fashion MNIST**.

## Dataset
**Fashion MNIST** terdiri dari 70.000 gambar grayscale (28x28 pixel) dalam 10 kategori:
- T-shirt/top, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, Ankle boot.

## Arsitektur Model
- **Conv2D + MaxPooling**: Ekstraksi fitur visual.
- **Flatten**: Meratakan output menjadi vektor.
- **Dense (ReLU)**: Hidden layer.
- **Dropout**: Regularisasi untuk mencegah overfitting.
- **Dense (Softmax)**: Output layer dengan 10 neuron (probabilitas per kelas).

## Requirements
- tensorflow
- numpy
- matplotlib

## Cara Menjalankan
```bash
python main.py
```
Program akan otomatis mendownload dataset, melatih model, dan menampilkan hasil prediksi sampel.
