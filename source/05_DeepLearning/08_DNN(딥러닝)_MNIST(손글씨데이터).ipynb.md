# 딥러닝의 "Hello, World!": MNIST 손글씨 숫자 인식

이제 우리는 딥러닝 세계의 "Hello, World!"라고 불리는, 가장 상징적이고 유명한 데이터셋인 **MNIST 손글씨 숫자 데이터셋**을 다뤄보겠습니다. `08_DNN(딥러닝)_MNIST(손글씨데이터).ipynb` 노트북은 0부터 9까지의 손으로 쓴 숫자 이미지를 보고, 이 이미지가 어떤 숫자인지 예측하는 **다중 클래스 분류(Multi-class Classification)** 모델을 구축합니다.

이 예제는 이미지 데이터를 딥러닝 모델에 어떻게 입력하고 처리하는지에 대한 기본적인 방법을 보여줍니다.

## 1. MNIST 데이터셋 소개

- **MNIST**: 딥러닝과 컴퓨터 비전 분야에서 모델의 성능을 시험하기 위해 가장 널리 사용되는 표준 데이터셋입니다.
- **구성**: 0부터 9까지의 손글씨 숫자 이미지로 구성되어 있습니다.
    - **훈련 데이터**: 60,000장
    - **테스트 데이터**: 10,000장
- **이미지 특성**: 각 이미지는 가로 28픽셀, 세로 28픽셀 크기의 흑백(grayscale) 이미지입니다. 각 픽셀은 0(흰색)부터 255(검은색)까지의 밝기 값을 가집니다.

우리의 목표는 28x28=784개의 픽셀 값을 입력받아, 이미지가 0~9 중 어떤 숫자인지 10개의 클래스로 분류하는 모델을 만드는 것입니다.

## 2. 데이터 로드 및 전처리

### 2.1. 데이터 로드

TensorFlow의 `keras.datasets` 라이브러리는 MNIST와 같은 유명한 데이터셋을 쉽게 불러올 수 있는 기능을 제공합니다.

```python
from tensorflow.keras.datasets import mnist

# Keras 라이브러리에서 데이터 로드
(X_train, y_train), (X_test, y_test) = mnist.load_data()
```
- `load_data()` 함수는 데이터를 훈련용(train)과 테스트용(test)으로 나누어 편리하게 제공합니다.

### 2.2. 데이터 전처리: 이미지 데이터를 위한 변환

딥러닝 모델(특히 `Dense` 층을 사용하는 DNN)에 이미지를 입력하기 위해서는 몇 가지 중요한 전처리 과정이 필요합니다.

1.  **2D 이미지를 1D 벡터로 변환 (Flattening)**:
    `Dense` 층은 1차원 형태의 입력을 받습니다. 따라서 (28, 28) 형태의 2차원 이미지 데이터를 (784,) 형태의 1차원 벡터로 펼쳐주어야 합니다.

    ```python
    # (60000, 28, 28) -> (60000, 784)
    train_X = X_train.reshape(60000, 784)
    ```

2.  **정규화 (Normalization)**:
    픽셀 값의 범위(0~255)를 0과 1 사이로 조정하여 모델의 학습을 안정화시키고 성능을 향상시킵니다. 가장 간단한 방법은 최댓값인 255로 나누는 것입니다.

    ```python
    train_X = train_X.astype('float32') / 255.0
    ```

3.  **타겟 변수 원-핫 인코딩 (One-Hot Encoding)**:
    이 문제는 10개의 클래스(0~9)로 분류하는 다중 분류 문제입니다. 따라서 타겟 변수(y)를 `to_categorical` 함수를 사용해 원-핫 인코딩해야 합니다. 예를 들어, 숫자 5는 `[0,0,0,0,0,1,0,0,0,0]` 과 같은 10차원 벡터로 변환됩니다.

    ```python
    from tensorflow.keras.utils import to_categorical

    train_Y = to_categorical(y_train, 10)
    ```

## 3. 모델 구성 및 학습

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(units=2, input_dim=784, activation='relu')) # 입력층 + 은닉층
model.add(Dense(units=10, activation='softmax'))          # 출력층

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

hist = model.fit(train_X, train_Y, epochs=500, batch_size=100, 
                 validation_data=(val_X, val_Y))
```
- **입력층**: `input_dim=784`로 설정하여 1차원으로 펼친 이미지 데이터를 입력받습니다.
- **출력층**: `units=10` (10개 클래스)과 `activation='softmax'`를 사용하여 각 숫자에 대한 확률을 출력합니다.
- **손실 함수**: 다중 분류이므로 `loss='categorical_crossentropy'`를 사용합니다.
- **학습**: 훈련 데이터(train_X, train_Y)로 모델을 학습시키고, 검증 데이터(val_X, val_Y)로 매 에포크마다 성능을 평가합니다.

## 4. 모델 성능 개선하기

노트북의 초기 모델은 은닉층의 뉴런 수가 2개뿐이라 매우 낮은 정확도를 보입니다. 이는 모델의 표현 능력(representational capacity)이 부족하여 복잡한 손글씨 패턴을 학습하기 어렵기 때문입니다. 노트북 후반부에서는 다음과 같은 방법으로 모델의 성능을 대폭 향상시킵니다.

1.  **데이터 양 증가**: 학습에 사용하는 데이터의 양을 늘립니다. (예: 700개 -> 50,000개)
2.  **모델 복잡도 증가**: 은닉층을 더 깊게 쌓고, 각 층의 뉴런(unit) 수를 늘려 모델이 더 복잡한 패턴을 학습할 수 있게 합니다.
3.  **과적합 방지**: `Dropout`을 추가하여 모델의 일반화 성능을 높입니다.
4.  **하이퍼파라미터 튜닝**: `epochs`, `batch_size`, `optimizer` 등을 조정하여 최적의 학습 조건을 찾습니다.

이러한 개선을 통해 모델의 정확도는 98% 이상으로 크게 향상됩니다. 이는 딥러닝 모델의 성능이 데이터의 양과 모델의 구조에 얼마나 크게 의존하는지를 잘 보여줍니다.

## 5. 더 깊은 학습을 위한 자료

- **MNIST 데이터셋 공식 페이지**
  - [http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/)
- **이미지 분류를 위한 더 발전된 모델: CNN (합성곱 신경망)**
  - [https://www.tensorflow.org/tutorials/images/cnn?hl=ko](https://www.tensorflow.org/tutorials/images/cnn?hl=ko) (DNN은 이미지의 공간적 구조를 무시하고 1차원으로 펼치지만, CNN은 이미지의 공간 정보를 유지하며 학습하여 훨씬 높은 성능을 보입니다.)

MNIST는 딥러닝 모델링의 전체 과정을 연습하고, 다양한 하이퍼파라미터와 기법들이 모델 성능에 미치는 영향을 실험하기에 가장 좋은 데이터셋 중 하나입니다.
