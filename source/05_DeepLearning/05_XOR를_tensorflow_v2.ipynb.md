# 딥러닝으로 XOR 문제 해결하기 (TensorFlow v2)

이전 장에서 우리는 단일 층 로지스틱 회귀 모델이 직선으로 데이터를 나누기 때문에 XOR와 같은 비선형 문제를 해결할 수 없다는 한계를 확인했습니다. 이번 `05_XOR을_tensorflow_v2.ipynb` 노트북에서는 이 문제를 **딥러닝(Deep Learning)**, 즉 여러 개의 층을 쌓아 해결하는 과정을 보여줍니다.

## 1. 왜 딥러닝이 필요한가? - 비선형성의 이해

XOR 문제는 데이터가 선형적으로 분리될 수 없는 대표적인 예시입니다. (0,0)과 (1,1)은 클래스 0, (0,1)과 (1,0)은 클래스 1로, 어떤 직선을 그어도 두 클래스를 완벽하게 나눌 수 없습니다.

딥러닝은 입력층과 출력층 사이에 **은닉층(Hidden Layer)**을 추가하여 이 문제를 해결합니다. 각 층은 **활성화 함수(Activation Function)**를 통해 데이터를 비선형적인 공간으로 변환(왜곡)시키는 역할을 합니다. 이렇게 여러 층을 거치며 데이터를 계속해서 왜곡시키다 보면, 원래는 직선으로 나눌 수 없었던 데이터가 마법처럼 선형적으로 분리 가능한 형태로 바뀌게 됩니다. 이것이 딥러닝이 비선형 문제를 해결하는 핵심 원리입니다.

## 2. TensorFlow v2 (Keras)를 이용한 딥러닝 모델 구현

이 노트북에서는 최신 TensorFlow 2.x 버전의 핵심 API인 **Keras**를 사용하여 직관적으로 딥러닝 모델을 구축합니다. TFv1과 달리, 그래프를 먼저 정의할 필요 없이 파이썬 코드를 작성하듯 모델을 만들고 학습시킬 수 있습니다.

### 2.1. 데이터 준비

```python
import numpy as np

X_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_data = np.array([[0], [1], [1], [0]])
```
- XOR 문제를 위한 입력(X)과 정답(Y) 데이터를 준비합니다.

### 2.2. 딥러닝 모델 구성 (Sequential API)

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 3. 모델 구성
model = Sequential()

# 입력층 + 첫 번째 은닉층
model.add(Dense(units=10, input_dim=2, activation='relu'))

# 두 번째 은닉층
model.add(Dense(units=20, activation='relu'))

# 세 번째 은닉층
model.add(Dense(units=10, activation='relu'))

# 출력층
model.add(Dense(units=1, activation='sigmoid'))

model.summary()
```
- `Sequential` 모델은 층을 순서대로 차곡차곡 쌓는 가장 간단한 방법입니다.
- `Dense` 층을 여러 개 추가하여 딥러닝 모델을 만듭니다.
- **입력층**: 첫 번째 `Dense` 층의 `input_dim=2`가 입력 데이터의 특성(feature)이 2개임을 정의하는 입력층의 역할을 합니다.
- **은닉층**: 중간에 있는 `Dense` 층들이 은닉층입니다. `activation='relu'`는 가장 널리 사용되는 활성화 함수 중 하나로, 입력이 0보다 크면 그대로 출력하고 0보다 작으면 0을 출력합니다. 이 함수를 통해 비선형성을 추가합니다.
- **출력층**: 마지막 `Dense` 층입니다.
    - `units=1`: 최종 출력값은 하나입니다 (0 또는 1).
    - `activation='sigmoid'`: 이진 분류 문제이므로, 최종 결과를 0과 1 사이의 확률 값으로 만들기 위해 시그모이드 함수를 사용합니다.

### 2.3. 모델 학습 과정 설정 및 실행

```python
# 4. 모델 학습과정 설정 (컴파일)
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['binary_accuracy'])

# 5. 모델 학습
hist = model.fit(X_data, y_data, epochs=1200, verbose=2)
```
- **컴파일 (`compile`)**: TFv1과 개념은 동일하지만, 더 직관적입니다.
    - `loss='binary_crossentropy'`: 이진 분류 문제이므로 크로스 엔트로피 손실 함수를 사용합니다.
    - `optimizer='adam'`: Adam은 경사 하강법을 개선한 옵티마이저로, 현재 가장 널리 사용되며 안정적인 성능을 보여줍니다.
    - `metrics=['binary_accuracy']`: 정확도를 측정하여 학습 과정을 모니터링합니다.
- **학습 (`fit`)**: `fit` 함수를 호출하면 지정된 `epochs`만큼 학습이 진행됩니다. `verbose=2` 옵션은 각 에포크마다의 학습 결과를 간략하게 출력해줍니다.

### 2.4. 모델 평가 및 사용

```python
# 6. 모델 평가
loss, acc = model.evaluate(X_data, y_data)
print(f"모델 정확도: {acc*100:.2f}%")

# 7. 모델 사용 (예측)
predictions = model.predict(X_data)
print(predictions)
```
- `evaluate`: 학습된 모델의 최종 손실과 정확도를 평가합니다. 딥러닝 모델을 사용한 결과, 정확도가 100%에 도달하여 XOR 문제를 완벽하게 해결했음을 확인할 수 있습니다.
- `predict`: 새로운 데이터에 대한 예측을 수행합니다. 결과는 시그모이드 함수를 거친 확률 값으로 나타납니다.

## 3. 결론: 딥러닝의 힘

이 노트북은 단일 층 퍼셉트론(로지스틱 회귀)의 한계를 명확히 보여주고, 은닉층과 비선형 활성화 함수를 추가하는 것만으로 어떻게 그 한계를 극복하고 복잡한 문제를 해결할 수 있는지를 보여주는 훌륭한 예제입니다. 딥러닝이 왜 강력한지를 직관적으로 이해할 수 있는 중요한 첫걸음이라 할 수 있습니다.

## 4. 더 깊은 학습을 위한 자료

- **신경망과 딥러닝 (마이클 닐슨)**
  - [http://neuralnetworksanddeeplearning.com/](http://neuralnetworksanddeeplearning.com/) (딥러닝의 수학적 원리를 깊이 있게 다루는 최고의 온라인 교재 중 하나입니다.)
- **3Blue1Brown - 신경망 시리즈 (강력 추천)**
  - [https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) (신경망의 작동 원리를 환상적인 시각화와 함께 설명합니다.)
- **TensorFlow Keras 공식 문서**
  - [https://www.tensorflow.org/guide/keras/sequential_model?hl=ko](https://www.tensorflow.org/guide/keras/sequential_model?hl=ko)
