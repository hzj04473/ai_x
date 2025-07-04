# 딥러닝 모델링 심화: 다양한 DNN 아키텍처와 Keras API 활용

이전 노트북에서 우리는 붓꽃(Iris) 데이터셋을 사용하여 기본적인 다중 클래스 분류 모델을 만들었습니다. 이번 `11_iris(다양한DNN).ipynb` 노트북에서는 한 걸음 더 나아가, 동일한 데이터셋을 사용하되 **더 유연하고 강력한 방법으로 딥러닝 모델을 설계하는 다양한 기법**들을 탐구합니다.

이 문서는 Keras의 `Sequential` API를 넘어, **클래스 기반 모델링**, **Scikit-learn의 MLPClassifier**, 그리고 가장 중요한 **Keras의 함수형 API(Functional API)**를 사용한 고급 모델 구축 방법을 소개합니다.

## 1. 핵심 개념: `sparse_categorical_crossentropy`

이전 예제들에서는 다중 분류 문제의 정답(y)을 원-핫 인코딩으로 변환했습니다. 하지만 타겟 데이터가 **정수 형태(0, 1, 2, ...)**로 되어 있을 때, 굳이 원-핫 인코딩을 하지 않고도 사용할 수 있는 손실 함수가 바로 `sparse_categorical_crossentropy`입니다.

- **`categorical_crossentropy`**: 타겟(y)이 원-핫 인코딩된 벡터일 때 사용합니다. (예: `[0, 1, 0]`)
- **`sparse_categorical_crossentropy`**: 타겟(y)이 정수 레이블일 때 사용합니다. (예: `1`)

내부적으로는 동일하게 작동하지만, `sparse` 버전을 사용하면 데이터를 명시적으로 원-핫 인코딩할 필요가 없어 코드가 간결해지고 메모리를 절약할 수 있습니다.

## 2. 다양한 모델링 접근법

### 2.1. Scikit-learn을 이용한 신경망: `MLPClassifier`

TensorFlow/Keras 외에도, Scikit-learn 라이브러리는 자체적으로 다층 퍼셉트론(Multi-layer Perceptron), 즉 DNN을 구현한 `MLPClassifier`를 제공합니다.

```python
from sklearn.neural_network import MLPClassifier

mlp_model = MLPClassifier(hidden_layer_sizes=(50,30), # (은닉층1 뉴런 수, 은닉층2 뉴런 수)
                      activation='relu', 
                      solver='adam',
                      max_iter=1000, # 최대 에포크
                      early_stopping=True, # 조기 종료 사용
                      n_iter_no_change=50) # patience

mlp_model.fit(train_X, train_y)
```
- Keras에 비해 상대적으로 간단한 문법으로 표준적인 DNN 모델을 빠르게 만들고 실험해볼 수 있는 좋은 대안입니다.

### 2.2. 재사용성을 위한 설계: 클래스 기반 모델링

동일한 구조의 모델을 여러 번 만들어야 할 때, 모델 생성 및 컴파일 과정을 클래스(Class)로 캡슐화하면 코드를 더 깔끔하고 재사용하기 쉽게 만들 수 있습니다.

```python
class DNNClassifier:
    @staticmethod
    def build(input_dim=4, activation='relu'):
        model = Sequential([
            Input(input_dim),
            Dense(50, activation=activation),
            Dense(30, activation=activation),
            Dense(3, activation='softmax')
        ])
        model.compile(loss='sparse_categorical_crossentropy', ...)
        return model

# 모델 생성 및 학습
model = DNNClassifier.build()
hist = model.fit(train_X, train_y, ...)
```
- 이는 좋은 소프트웨어 공학 습관이며, 복잡한 프로젝트에서 코드의 구조를 체계적으로 관리하는 데 도움을 줍니다.

## 3. Keras의 꽃: 함수형 API (Functional API)

`Sequential` API는 층을 순서대로 쌓는 단순한 모델에만 적합합니다. 하지만 여러 개의 입력이나 출력을 갖거나, 층 간에 복잡한 연결 구조를 갖는 모델을 만들려면 **함수형 API**를 사용해야 합니다. 함수형 API는 각 층을 함수처럼 호출하고, 그 입출력을 명시적으로 연결하여 마치 그래프를 그리듯 모델을 자유롭게 설계할 수 있게 해줍니다.

### 3.1. 기본 함수형 모델

```python
from tensorflow.keras import Model
from tensorflow.keras.layers import Input, Dense

# 1. 입력층 정의
input_layer = Input(shape=(4,))

# 2. 층 연결
x = Dense(50, activation='relu')(input_layer)
x = Dense(30, activation='relu')(x)
output_layer = Dense(3, activation='softmax')(x)

# 3. 모델 생성
model = Model(inputs=input_layer, outputs=output_layer)
```
- `Input()`으로 모델의 입력을 정의하고, 각 `Dense` 층을 이전 층의 출력을 입력으로 받아 호출하는 방식으로 연결합니다.
- 마지막으로 `Model()`에 전체 모델의 입력과 출력을 지정하여 모델을 완성합니다.

### 3.2. 고급 아키텍처 예시

함수형 API를 사용하면 다음과 같은 더 복잡한 구조도 쉽게 만들 수 있습니다.

- **병렬 모델 (Ensemble-like Model)**: 입력 데이터를 두 개 이상의 다른 경로로 동시에 처리한 뒤, 그 결과를 합쳐 최종 예측을 수행하는 모델입니다. 각 경로가 데이터의 다른 측면을 학습하도록 유도할 수 있습니다.

  ```python
  from tensorflow.keras.layers import concatenate

  input_layer = Input(shape=(4,))
  # 경로 1
  path1 = Dense(10)(input_layer)
  # 경로 2
  path2 = Dense(10)(input_layer)

  # 두 경로의 결과를 합침
  concat_layer = concatenate([path1, path2])
  output_layer = Dense(3, activation='softmax')(concat_layer)
  ```

- **잔차 연결 모델 (Residual Model)**: 특정 층의 입력(Input)을 해당 층의 출력(Output)에 더해주는 구조입니다. (ResNet의 핵심 아이디어) 이는 매우 깊은 신경망에서 기울기가 소실되는 문제(Vanishing Gradient)를 완화하여 학습을 돕습니다.

  ```python
  from tensorflow.keras.layers import add

  input_layer = Input(shape=(4,))
  x = Dense(4, activation='relu')(input_layer) # 입력과 차원을 맞춰야 함

  # 입력(input_layer)과 출력(x)을 더함
  residual_output = add([input_layer, x])
  output_layer = Dense(3, activation='softmax')(residual_output)
  ```

## 4. 핵심 요약

- **`sparse_categorical_crossentropy`**: 원-핫 인코딩 없이 정수형 타겟을 사용할 때 편리한 손실 함수입니다.
- **함수형 API**: `Sequential` 모델의 한계를 넘어, 다중 입력/출력, 층 공유, 병렬/잔차 구조 등 복잡하고 유연한 딥러닝 아키텍처를 설계할 수 있는 강력한 도구입니다.
- **고급 아키텍처**: 병렬 구조나 잔차 연결과 같은 기법들은 모델이 더 복잡한 패턴을 효과적으로 학습하고, 깊은 네트워크의 학습을 안정시키는 데 도움을 줍니다.

이 노트북은 Keras를 사용한 모델링의 수준을 한 단계 높여, 자신만의 독창적이고 강력한 모델을 설계할 수 있는 기반을 마련해 줍니다.
