# 머신러닝 고전 예제: 붓꽃(Iris) 품종 분류

이번 `10_iris(다중분류).ipynb` 노트북에서는 머신러닝과 통계학의 역사에서 가장 유명한 데이터셋 중 하나인 **붓꽃(Iris) 데이터셋**을 사용하여 붓꽃의 품종을 예측하는 **다중 클래스 분류** 문제를 다룹니다. 이 예제는 매우 정제된 데이터를 사용하기 때문에, 데이터 전처리보다는 모델 자체의 구조와 학습, 평가 과정에 집중하여 기본기를 다지기에 매우 좋습니다.

## 1. 붓꽃(Iris) 데이터셋 소개

- **데이터셋**: 통계학자 피셔(Fisher)가 소개한 데이터로, 3가지 다른 품종의 붓꽃에 대한 데이터를 담고 있습니다.
- **독립 변수 (X)**: 꽃받침(sepal)의 길이와 너비, 꽃잎(petal)의 길이와 너비 (총 4개의 연속적인 숫자 데이터)
- **종속 변수 (Y)**: 붓꽃의 품종 (setosa, versicolor, virginica - 총 3개의 클래스)

우리의 목표는 4가지 측정치를 바탕으로 해당 붓꽃이 3가지 품종 중 어디에 속하는지를 정확하게 분류하는 모델을 만드는 것입니다.

## 2. 데이터 준비 및 전처리

이 노트북에서는 데이터 전처리 과정이 비교적 간단합니다.

1.  **데이터 로드**: `seaborn` 라이브러리에 내장된 `load_dataset('iris')` 함수를 사용해 데이터를 편리하게 불러옵니다. 이 데이터는 결측치가 없는 깨끗한 데이터입니다.

2.  **독립/종속 변수 분리**: `pandas` 데이터프레임에서 `.iloc`을 사용해 독립 변수(X)와 종속 변수(y)를 분리하고, `.values` 또는 `.to_numpy()`를 사용해 NumPy 배열로 변환합니다.

3.  **원-핫 인코딩**: 종속 변수인 붓꽃 품종(`species`)은 'setosa', 'versicolor', 'virginica'와 같은 문자열 데이터입니다. 이를 모델이 이해할 수 있도록 원-핫 인코딩으로 변환해야 합니다. 노트북에서는 두 가지 방법을 모두 보여줍니다.
    - **방법 1: `LabelEncoder` + `to_categorical`**
      ```python
      from sklearn.preprocessing import LabelEncoder
      from tensorflow.keras.utils import to_categorical

      le = LabelEncoder()
      y_labels = le.fit_transform(iris.species) # 문자 -> 숫자 (0, 1, 2)
      Y_onehot = to_categorical(y_labels)      # 숫자 -> 원-핫 벡터
      ```
    - **방법 2: `pandas.get_dummies`**
      ```python
      import pandas as pd
      Y_onehot = pd.get_dummies(iris.species).values
      ```
      `get_dummies` 함수는 문자열 데이터를 바로 원-핫 인코딩된 데이터프레임으로 만들어주어 더 간결합니다.

4.  **훈련/테스트 데이터 분할**: `train_test_split`을 사용해 데이터를 훈련셋(80%)과 테스트셋(20%)으로 나눕니다. `stratify=iris_Y` 옵션을 주어 각 품종이 훈련셋과 테스트셋에 동일한 비율로 포함되도록 합니다. (예: 각 품종별로 50개씩 있으므로, 훈련셋에는 40개씩, 테스트셋에는 10개씩 들어갑니다.)

## 3. 모델 구성 및 학습

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# 모델 구성
model = Sequential()
model.add(Dense(64, input_dim=4, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
# ... (추가적인 Dense, Dropout 층)
model.add(Dense(3, activation='softmax')) # 출력층

# 모델 컴파일
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 콜백 설정
early_stopping = EarlyStopping(patience=40)
model_checkpoint = ModelCheckpoint(filepath='./model_iris/best_model.h5', save_best_only=True)

# 모델 학습
hist = model.fit(X_train, Y_train, epochs=500, validation_split=0.2, 
                 callbacks=[early_stopping, model_checkpoint])
```
- **모델 구조**: 입력 특성이 4개이므로 `input_dim=4`로 설정하고, 여러 개의 `Dense` 층과 `Dropout` 층을 쌓아 깊은 신경망을 구성합니다.
- **출력층**: 3개의 품종을 분류해야 하므로 `units=3`으로 설정하고, 다중 클래스 분류의 표준인 `softmax` 활성화 함수를 사용합니다.
- **컴파일**: 다중 클래스 분류이므로 손실 함수로 `categorical_crossentropy`를 사용합니다.
- **학습**: `validation_split=0.2`를 사용해 훈련 데이터의 20%를 검증용으로 활용하며, `EarlyStopping`과 `ModelCheckpoint` 콜백을 통해 학습을 효율적으로 제어하고 최적의 모델을 저장합니다.

## 4. 모델 평가

학습이 완료된 후, 저장된 최적의 모델(`best_model.h5`)을 불러와 테스트셋으로 최종 성능을 평가합니다.

```python
from sklearn.metrics import confusion_matrix, f1_score

# 저장된 최고 성능의 모델을 불러옴
best_model = load_model('./model_iris/best_model.h5')

# 예측 수행
pred = best_model.predict(X_test).argmax(axis=1)
real = Y_test.argmax(axis=1)

# F1-Score 계산
f1 = f1_score(real, pred, average='weighted')
print(f"F1 Score: {f1:.4f}")

# 혼동 행렬 시각화
print(confusion_matrix(real, pred))
```
- 붓꽃 데이터는 비교적 분류가 쉬운 문제이기 때문에, 딥러닝 모델은 매우 높은 정확도(거의 100%)를 달성합니다.
- 혼동 행렬을 통해 모델이 각 품종을 얼마나 정확하게 구분했는지, 혹은 어떤 품종을 다른 품종으로 혼동했는지 시각적으로 확인할 수 있습니다.

## 5. 핵심 요약

- **붓꽃 데이터셋**: 머신러닝/딥러닝 분류 모델의 기본을 연습하기 위한 최고의 "교과서" 데이터셋입니다.
- **문자열 데이터의 원-핫 인코딩**: `pd.get_dummies`는 문자열 범주를 한 번에 원-핫 인코딩으로 변환하는 편리한 방법입니다.
- **`validation_split`**: `fit` 함수 내에서 별도의 검증셋을 지정하지 않고, 훈련셋의 일부를 간편하게 검증용으로 사용할 수 있는 유용한 기능입니다.
- **모델 평가**: 정확도뿐만 아니라, F1-Score와 혼동 행렬을 함께 사용하여 모델의 성능을 다각적으로 분석하는 것이 중요합니다.

이 예제를 통해 다중 클래스 분류 문제의 표준적인 해결 과정을 완벽하게 익힐 수 있습니다.
