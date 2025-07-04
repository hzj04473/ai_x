# TensorFlow v1 기초 및 데이터 스케일링의 중요성

안녕하세요. 이번 문서에서는 `04_tensorflow_v1_feat.스케일조절.ipynb` 노트북을 기반으로, 최신 버전과는 다른 **TensorFlow v1**의 독특한 프로그래밍 방식을 알아보고, 머신러닝에서 매우 중요한 전처리 과정인 **데이터 스케일링(Feature Scaling)**의 필요성에 대해 깊이 있게 다룹니다.

## 1. TensorFlow v1: 그래프 기반 프로그래밍

최신 TensorFlow 2.x 버전은 Keras를 중심으로 직관적인 코드를 작성하지만, v1은 **계산 그래프(Computational Graph)**를 먼저 정의하고, **세션(Session)**을 통해 그래프를 실행하는 방식을 사용합니다. 이 개념을 이해하는 것이 v1 코드를 읽는 핵심입니다.

1.  **그래프 정의**: 먼저 데이터(Tensor)가 어떻게 흘러가며 연산될지를 설계도처럼 정의합니다. 이 단계에서는 실제 계산이 일어나지 않습니다.
2.  **세션 실행**: 정의된 그래프를 실행하기 위해 `tf.Session()`을 열고, `sess.run()`을 통해 원하는 노드의 계산 결과를 가져옵니다.

### 1.1. TFv1 핵심 구성 요소

- **`tf.constant`**: 이름 그대로 변하지 않는 '상수' 텐서를 정의합니다.
- **`tf.Variable`**: 학습을 통해 값이 계속 업데이트되는 '변수' 텐서입니다. 주로 가중치(W)나 편향(b)에 사용되며, 사용 전에 반드시 `tf.global_variables_initializer()`로 초기화해야 합니다.
- **`tf.placeholder`**: 그래프를 실행할 때 외부에서 데이터를 주입받는 '빈 그릇' 같은 존재입니다. `sess.run()`을 실행할 때 `feed_dict`를 통해 값을 전달합니다.

```python
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior() # v2 기능을 끄고 v1 모드로 전환

# 1. 그래프 정의
node1 = tf.constant(10)
node2 = tf.constant(20)
node3 = tf.add(node1, node2)

# 2. 세션 실행
sess = tf.Session()
result = sess.run(node3)
print(result) # 30
```

## 2. 선형 회귀와 데이터 스케일링

### 2.1. 스케일이 다른 데이터의 문제점

노트북의 예제에서는 여러 독립 변수의 단위나 값의 범위가 크게 다를 때, 학습이 제대로 이루어지지 않는 현상을 보여줍니다. `cost` 값이 더 이상 줄어들지 않고 특정 값에 머무는 것을 볼 수 있습니다.

- **왜 이런 문제가 발생할까요?** 값의 범위가 큰 특정 변수가 손실 함수(cost function)에 더 큰 영향을 미치게 됩니다. 이로 인해 손실 함수의 표면이 한쪽으로 길게 찌그러진 타원형 모양이 되어, 경사 하강법(Gradient Descent) 알고리즘이 최적의 최소 지점을 찾아가기 매우 어려워집니다. 이를 '경사면이 비효율적이다'라고 표현합니다.

### 2.2. 해결책: 데이터 스케일링 (Feature Scaling)

데이터 스케일링은 모든 변수(Feature)의 값의 범위를 비슷한 수준으로 맞춰주는 전처리 과정입니다. 이를 통해 손실 함수의 표면이 원형에 가까워져 옵티마이저가 훨씬 빠르고 안정적으로 최적해를 찾을 수 있습니다.

- **정규화 (Normalization)**: 데이터 값을 0과 1 사이의 범위로 조정합니다. `MinMaxScaler`를 주로 사용합니다.
  - `X_scaled = (X - X_min) / (X_max - X_min)`

- **표준화 (Standardization)**: 데이터의 분포를 평균이 0, 표준편차가 1이 되도록 조정합니다. `StandardScaler`를 사용하며, 이상치(outlier)가 있는 경우 정규화보다 안정적인 성능을 보입니다.
  - `X_scaled = (X - X_mean) / X_std`

노트북에서는 `MinMaxScaler`와 `StandardScaler`를 사용해 데이터를 변환한 뒤, 동일한 모델을 학습시켰을 때 `cost`가 안정적으로 감소하며 학습이 성공하는 것을 명확하게 보여줍니다.

**중요 포인트**: 모델을 학습할 때 스케일링을 적용했다면, 새로운 데이터로 예측할 때도 **반드시 동일한 스케일러(`scaler_x`)로 변환**한 후 모델에 입력해야 합니다. 그리고 모델이 예측한 결과(`scaled_y_hat`)는 스케일링된 값이므로, **원래 단위로 되돌리기 위해 `scaler_y.inverse_transform()`**을 사용해야 합니다.

## 3. 다중 변수 회귀 및 로지스틱 회귀

### 3.1. 다중 변수 선형 회귀

입력 변수가 여러 개일 경우, 가중치(W)는 입력 변수의 개수만큼 차원을 갖는 행렬이 됩니다. 가설(Hypothesis)은 행렬 곱셈으로 표현됩니다.

- `H = tf.matmul(X, W) + b`

노트북에서는 `ozone.csv` 데이터를 `pandas`로 읽어와 결측치를 처리하고, 3개의 독립 변수(Solar.R, Wind, Temp)로 오존 농도(Ozone)를 예측하는 다중 선형 회귀 모델을 구현합니다.

### 3.2. 이진 분류 (Logistic Regression)

결과를 0 또는 1로 분류하는 이진 분류 문제에서는 선형 회귀 모델을 그대로 사용할 수 없습니다. 예측값이 0과 1 사이의 확률 값으로 나와야 하기 때문입니다.

- **시그모이드 함수 (Sigmoid Function)**: 선형 회귀의 결과(`logits = tf.matmul(X, W) + b`)를 0과 1 사이의 값으로 변환해주는 활성화 함수입니다. 이 값이 0.5 이상이면 1(True), 미만이면 0(False)으로 분류합니다.
  - `H = tf.sigmoid(logits)`

- **비용 함수 (Cost Function)**: 로지스틱 회귀에서는 평균 제곱 오차(MSE) 대신 **크로스 엔트로피(Cross-Entropy)**를 비용 함수로 사용합니다. 이는 실제 값과 예측 확률 사이의 차이를 효과적으로 측정합니다.
  - `cost = tf.nn.sigmoid_cross_entropy_with_logits(...)`

## 4. XOR 문제: 딥러닝의 필요성

마지막으로, 단일 로지스틱 회귀 모델의 한계를 보여주는 고전적인 **XOR 문제**를 다룹니다. XOR 데이터는 직선 하나로는 두 클래스를 완벽하게 나눌 수 없는 **비선형(non-linear)** 문제입니다. 이 때문에 단일 층(single-layer) 모델로는 정확도가 0.75 이상 올라가지 못하는 한계를 보입니다.

이 문제를 해결하기 위해 여러 개의 층을 쌓아 복잡한 비선형 관계를 학습하는 **딥러닝(Deep Learning)**이 필요하며, 다음 노트북에서 이 내용을 다루게 됩니다.

## 5. 더 깊은 학습을 위한 자료

- **TensorFlow v1 vs v2 비교**
  - [https://www.linkedin.com/pulse/tensorflow-v1-vs-v2-whats-difference-chiso-okeke/](https://www.linkedin.com/pulse/tensorflow-v1-vs-v2-whats-difference-chiso-okeke/)
- **데이터 스케일링 (정규화와 표준화)**
  - [https://www.analyticsvidhya.com/blog/2020/04/feature-scaling-machine-learning-normalization-standardization/](https://www.analyticsvidhya.com/blog/2020/04/feature-scaling-machine-learning-normalization-standardization/)

이 문서를 통해 TensorFlow v1의 동작 방식과 데이터 스케일링의 중요성을 이해하는 데 도움이 되셨기를 바랍니다.
