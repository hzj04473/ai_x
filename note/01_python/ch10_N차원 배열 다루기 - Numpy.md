# NumPy 주말 집중 학습 커리큘럼

## 1일차: NumPy 기초와 배열 조작

### 1. NumPy 소개 (1시간)
- NumPy의 개념과 중요성
- 설치 및 환경 설정
- NumPy vs 파이썬 리스트

```python
# NumPy 설치 (필요한 경우)
# pip install numpy

# NumPy 불러오기
import numpy as np

# 버전 확인
print(np.__version__)

# 파이썬 리스트와 NumPy 배열 비교
python_list = [1, 2, 3, 4, 5]
numpy_array = np.array([1, 2, 3, 4, 5])

print("파이썬 리스트:", python_list)
print("NumPy 배열:", numpy_array)

# 성능 비교
import time

# 파이썬 리스트 연산
start_time = time.time()
result_list = [x * 2 for x in python_list]
list_time = time.time() - start_time

# NumPy 배열 연산
start_time = time.time()
result_array = numpy_array * 2
array_time = time.time() - start_time

print(f"리스트 연산 시간: {list_time:.10f}초")
print(f"배열 연산 시간: {array_time:.10f}초")
print(f"NumPy가 {list_time/array_time:.2f}배 빠름")
```

### 2. 배열 생성 방법 (2시간)
- 기본 배열 생성
- 특수 배열 생성 (zeros, ones, empty, eye, arange, linspace)
- 난수 배열 생성
- 다차원 배열 생성

```python
# 기본 배열 생성
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])  # 2차원 배열

print("1차원 배열:", arr1)
print("2차원 배열:\n", arr2)

# 특수 배열 생성
zeros = np.zeros((3, 4))        # 0으로 채워진 3x4 배열
ones = np.ones((2, 3))          # 1로 채워진 2x3 배열
empty = np.empty((2, 2))        # 초기화되지 않은 값으로 채워진 2x2 배열
identity = np.eye(3)            # 3x3 단위행렬
range_array = np.arange(0, 10, 2)  # 0부터 10까지 2 간격으로
linspace = np.linspace(0, 1, 5)    # 0부터 1까지 균등하게 5개 분할

print("\n0으로 채워진 배열:\n", zeros)
print("\n1로 채워진 배열:\n", ones)
print("\n초기화되지 않은 배열:\n", empty)
print("\n단위행렬:\n", identity)
print("\narange 배열:", range_array)
print("\nlinspace 배열:", linspace)

# 난수 배열 생성
random_array = np.random.rand(3, 3)       # 0~1 균일 분포 난수
normal_array = np.random.randn(3, 3)      # 정규 분포 난수
int_array = np.random.randint(0, 10, (3, 3))  # 0~9 정수 난수

print("\n균일 분포 난수:\n", random_array)
print("\n정규 분포 난수:\n", normal_array)
print("\n정수 난수:\n", int_array)

# 다차원 배열 생성 및 조작
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3차원 배열:\n", arr_3d)
print("3차원 배열의 형태:", arr_3d.shape)
```

### 3. 배열 속성 및 기본 조작 (2시간)
- 배열 속성 (shape, size, dtype, ndim)
- 배열 재구성 (reshape, flatten)
- 배열 연결 및 분할 (concatenate, vstack, hstack, split)
- 배열 데이터 타입 변환

```python
# 배열 속성
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("배열:\n", arr)
print("형태:", arr.shape)      # 배열의 형태
print("크기:", arr.size)       # 요소의 총 개수
print("데이터 타입:", arr.dtype)  # 데이터 타입
print("차원 수:", arr.ndim)     # 차원 수

# 배열 재구성
arr_reshaped = arr.reshape(3, 2)  # 3x2 형태로 재구성
arr_flattened = arr.flatten()     # 1차원으로 평탄화

print("\n재구성된 배열:\n", arr_reshaped)
print("평탄화된 배열:", arr_flattened)

# 배열 연결
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

vertical = np.vstack((arr1, arr2))    # 수직 연결
horizontal = np.hstack((arr1, arr2))  # 수평 연결
concat = np.concatenate((arr1, arr2), axis=0)  # axis=0: 수직, axis=1: 수평

print("\n수직 연결:\n", vertical)
print("\n수평 연결:\n", horizontal)
print("\n연결(axis=0):\n", concat)

# 배열 분할
arr = np.arange(16).reshape(4, 4)
print("\n분할할 배열:\n", arr)

v_split = np.vsplit(arr, 2)  # 수직 분할
h_split = np.hsplit(arr, 2)  # 수평 분할

print("\n수직 분할:")
for i, split_arr in enumerate(v_split):
    print(f"분할 {i}:\n", split_arr)

print("\n수평 분할:")
for i, split_arr in enumerate(h_split):
    print(f"분할 {i}:\n", split_arr)

# 데이터 타입 변환
arr = np.array([1, 2, 3, 4])
print("\n원본 배열:", arr, arr.dtype)

arr_float = arr.astype(np.float64)
print("float64로 변환:", arr_float, arr_float.dtype)

arr_bool = arr.astype(bool)
print("bool로 변환:", arr_bool, arr_bool.dtype)
```

### 4. 배열 인덱싱과 슬라이싱 (2시간)
- 기본 인덱싱
- 슬라이싱
- 고급 인덱싱 (정수 배열, 불리언 배열)
- 조건 기반 인덱싱

```python
# 1차원 배열 인덱싱과 슬라이싱
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("배열:", arr)

# 기본 인덱싱
print("\n인덱스 5의 값:", arr[5])
print("마지막 요소:", arr[-1])

# 슬라이싱 [시작:끝:간격]
print("\n처음 3개 요소:", arr[:3])        # 0~2 인덱스
print("인덱스 3부터 끝까지:", arr[3:])     # 3~끝 인덱스
print("인덱스 2부터 7까지:", arr[2:8])     # 2~7 인덱스
print("처음부터 끝까지 2단계씩:", arr[::2])  # 간격 2로 슬라이싱

# 2차원 배열 인덱싱과 슬라이싱
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("\n2차원 배열:\n", arr_2d)

# 행 및 열 선택
print("\n첫 번째 행:", arr_2d[0])
print("두 번째 열:", arr_2d[:, 1])

# 부분 배열 선택
print("\n처음 2개 행, 처음 2개 열:\n", arr_2d[:2, :2])
print("마지막 2개 행, 마지막 2개 열:\n", arr_2d[1:, 2:])

# 고급 인덱싱
arr = np.array([10, 20, 30, 40, 50])
indices = np.array([1, 3, 4])
print("\n배열:", arr)
print("인덱스 [1, 3, 4]의 값:", arr[indices])  # 인덱스 배열로 인덱싱

# 2차원 인덱싱
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2차원 배열:\n", arr_2d)
print("행 인덱스 [0, 1], 열 인덱스 [1, 2]의 값:", arr_2d[[0, 1], [1, 2]])  # [1, 6] 반환

# 불리언 인덱싱
arr = np.array([1, 2, 3, 4, 5])
mask = np.array([True, False, True, False, True])
print("\n배열:", arr)
print("불리언 마스크:", mask)
print("마스크 적용 결과:", arr[mask])  # [1, 3, 5] 반환

# 조건 기반 인덱싱
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("\n배열:", arr)
print("5보다 큰 요소:", arr[arr > 5])  # [6, 7, 8, 9, 10] 반환
print("짝수 요소:", arr[arr % 2 == 0])  # [2, 4, 6, 8, 10] 반환
print("3의 배수 요소:", arr[arr % 3 == 0])  # [3, 6, 9] 반환
```

## 2일차: NumPy 연산과 활용

### 1. 기본 수학 연산 (2시간)
- 기본 산술 연산
- 유니버설 함수 (universal functions)
- 통계 함수
- 선형대수 연산

```python
import numpy as np

# 기본 산술 연산
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

print("배열1:", arr1)
print("배열2:", arr2)

print("\n덧셈:", arr1 + arr2)  # 또는 np.add(arr1, arr2)
print("뺄셈:", arr1 - arr2)    # 또는 np.subtract(arr1, arr2)
print("곱셈:", arr1 * arr2)    # 또는 np.multiply(arr1, arr2)
print("나눗셈:", arr1 / arr2)  # 또는 np.divide(arr1, arr2)

# 스칼라 연산
print("\n스칼라 덧셈:", arr1 + 10)
print("스칼라 곱셈:", arr1 * 2)

# 유니버설 함수
print("\n제곱:", np.square(arr1))
print("제곱근:", np.sqrt(arr1))
print("지수:", np.exp(arr1))
print("로그(자연로그):", np.log(arr1))
print("사인:", np.sin(arr1))
print("코사인:", np.cos(arr1))

# 통계 함수
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("\n배열:", arr)
print("합계:", np.sum(arr))
print("평균:", np.mean(arr))
print("표준편차:", np.std(arr))
print("분산:", np.var(arr))
print("최소값:", np.min(arr))
print("최대값:", np.max(arr))
print("최소값 인덱스:", np.argmin(arr))
print("최대값 인덱스:", np.argmax(arr))

# 2차원 배열의 통계
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2차원 배열:\n", arr_2d)
print("전체 합계:", np.sum(arr_2d))
print("행별 합계:", np.sum(arr_2d, axis=1))  # axis=1: 행 방향으로 합계
print("열별 합계:", np.sum(arr_2d, axis=0))  # axis=0: 열 방향으로 합계

# 선형 대수 연산
# 행렬 곱셈
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("\n행렬 A:\n", A)
print("행렬 B:\n", B)
print("행렬 곱셈 (A @ B):\n", A @ B)  # 또는 np.matmul(A, B) 또는 np.dot(A, B)

# 전치 행렬
print("\n행렬 A의 전치행렬:\n", A.T)

# 역행렬
from numpy.linalg import inv
print("\n행렬 A의 역행렬:\n", inv(A))

# 행렬식
from numpy.linalg import det
print("\n행렬 A의 행렬식:", det(A))

# 고유값과 고유벡터
from numpy.linalg import eig
eigenvalues, eigenvectors = eig(A)
print("\n행렬 A의 고유값:", eigenvalues)
print("행렬 A의 고유벡터:\n", eigenvectors)
```

### 2. 브로드캐스팅 (1시간)
- 브로드캐스팅 규칙
- 형태가 다른 배열 간의 연산
- 브로드캐스팅 예제

```python
import numpy as np

# 브로드캐스팅 기본 예제
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("배열:\n", arr)

# 스칼라 브로드캐스팅
print("\n모든 요소에 10 더하기:\n", arr + 10)

# 벡터와 행렬 간의 브로드캐스팅
row_vector = np.array([10, 20, 30])  # 행 벡터 (1x3)
print("\n행 벡터:", row_vector)
print("행 벡터와 행렬 덧셈:\n", arr + row_vector)  # 각 행에 벡터 더하기

col_vector = np.array([[10], [20], [30]])  # 열 벡터 (3x1)
print("\n열 벡터:\n", col_vector)
print("열 벡터와 행렬 덧셈:\n", arr + col_vector)  # 각 열에 벡터 더하기

# 브로드캐스팅 차원 맞추기
a = np.array([1, 2, 3])  # 형태: (3,)
b = np.array([[4], [5], [6]])  # 형태: (3, 1)
print("\n배열 a:", a, "형태:", a.shape)
print("배열 b:\n", b, "형태:", b.shape)
print("브로드캐스팅 결과:\n", a + b)  # 형태: (3, 3)

# 실제 활용 예: 표준화
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mean = np.mean(arr, axis=0)  # 열별 평균
std = np.std(arr, axis=0)    # 열별 표준편차

print("\n배열:\n", arr)
print("열별 평균:", mean)
print("열별 표준편차:", std)
print("표준화된 배열:\n", (arr - mean) / std)  # Z-score 표준화

# 온도 변환 예제
celsius = np.array([0, 10, 20, 30, 40])
print("\n섭씨 온도:", celsius)
fahrenheit = celsius * 9/5 + 32
print("화씨 온도:", fahrenheit)
```

### 3. 고급 배열 조작 (2시간)
- 배열 전치 및 축 바꾸기
- 배열 복사 (얕은 복사, 깊은 복사)
- 팬시 인덱싱
- 마스킹 연산
- 배열 정렬

```python
import numpy as np

# 배열 전치 및 축 바꾸기
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("원본 배열:\n", arr_2d)
print("전치 배열:\n", arr_2d.T)  # 행과 열 바꾸기

# 3차원 배열에서 축 바꾸기
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3차원 배열 (형태: %s):\n" % str(arr_3d.shape), arr_3d)
print("축 바꾸기 (0, 2, 1) 결과 (형태: %s):\n" % str(np.transpose(arr_3d, (0, 2, 1)).shape), np.transpose(arr_3d, (0, 2, 1)))
print("축 바꾸기 (1, 0, 2) 결과 (형태: %s):\n" % str(np.transpose(arr_3d, (1, 0, 2)).shape), np.transpose(arr_3d, (1, 0, 2)))

# 배열 복사
a = np.array([1, 2, 3])
b = a  # 참조(얕은 복사)
c = a.copy()  # 깊은 복사

print("\n원본 배열 a:", a)
print("참조 배열 b:", b)
print("복사 배열 c:", c)

a[0] = 10
print("\na[0]을 10으로 변경 후:")
print("배열 a:", a)
print("참조 배열 b:", b)  # a와 함께 변경됨
print("복사 배열 c:", c)  # 변경되지 않음

# 팬시 인덱싱
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
indices = [1, 3, 5]
print("\n배열:", arr)
print("팬시 인덱싱 [1, 3, 5] 결과:", arr[indices])  # [20, 40, 60]

# 2차원 팬시 인덱싱
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print("\n2차원 배열:\n", arr_2d)
print("특정 행 [0, 2, 3] 선택:\n", arr_2d[[0, 2, 3]])
print("(행, 열) 쌍 [(0, 0), (1, 1), (2, 2)] 선택:", arr_2d[np.arange(3), np.arange(3)])  # [1, 5, 9]

# 마스킹 연산
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
mask = arr > 5
print("\n배열:", arr)
print("마스크 (arr > 5):", mask)
print("마스킹 결과:", arr[mask])  # [6, 7, 8, 9]

# 복합 조건 마스킹
mask = (arr > 3) & (arr < 8)
print("\n마스크 ((arr > 3) & (arr < 8)):", mask)
print("마스킹 결과:", arr[mask])  # [4, 5, 6, 7]

# 배열 정렬
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5])
print("\n원본 배열:", arr)
print("정렬된 배열:", np.sort(arr))  # 원본 변경 없이 정렬된 배열 반환

# 원본 배열 정렬
arr.sort()
print("원본 배열 정렬 후:", arr)

# 2차원 배열 정렬
arr_2d = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
print("\n2차원 배열:\n", arr_2d)
print("행별 정렬:\n", np.sort(arr_2d))  # 각 행 정렬
print("열별 정렬:\n", np.sort(arr_2d, axis=0))  # 각 열 정렬

# 정렬 인덱스 반환
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5])
print("\n배열:", arr)
print("정렬 인덱스:", np.argsort(arr))  # [1, 3, 6, 0, 2, 4, 8, 7, 5]
```

### 4. 실전 응용 예제 (2시간)
- 데이터 분석 기초
- 이미지 처리 기초
- 시계열 분석 기초
- 머신러닝 기초

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. 데이터 분석 기초: 주식 수익률 계산
np.random.seed(42)
stock_prices = np.random.normal(loc=100, scale=10, size=(20,))  # 가상의 주식 가격 데이터
print("주식 가격 데이터:", stock_prices)

# 일별 수익률 계산
daily_returns = np.diff(stock_prices) / stock_prices[:-1]
print("\n일별 수익률:", daily_returns)
print("평균 일별 수익률:", np.mean(daily_returns))
print("일별 수익률 표준편차:", np.std(daily_returns))

# 누적 수익률
cumulative_return = np.prod(1 + daily_returns) - 1
print("누적 수익률:", cumulative_return)

# 그래프로 시각화
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(stock_prices)
plt.title('주식 가격')
plt.xlabel('날짜')
plt.ylabel('가격')

plt.subplot(1, 2, 2)
plt.plot(daily_returns)
plt.title('일별 수익률')
plt.xlabel('날짜')
plt.ylabel('수익률')
plt.tight_layout()
plt.savefig('stock_analysis.png')  # 그래프 저장
plt.close()

# 2. 이미지 처리 기초: 간단한 이미지 필터링
# 간단한 이미지 생성 (흑백)
image = np.zeros((10, 10))
image[3:7, 3:7] = 1  # 중앙에 흰색 사각형
print("\n원본 이미지:\n", image)

# 필터 정의 (3x3 가우시안 블러 필터)
kernel = np.array([[1, 2, 1], 
                   [2, 4, 2], 
                   [1, 2, 1]]) / 16
print("\n블러 필터:\n", kernel)

# 컨볼루션 수행 (간단한 구현)
result = np.zeros((8, 8))  # 출력 이미지 크기
for i in range(8):
    for j in range(8):
        result[i, j] = np.sum(image[i:i+3, j:j+3] * kernel)

print("\n필터링 결과:\n", result)

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('원본 이미지')
plt.subplot(1, 3, 2)
plt.imshow(kernel, cmap='gray')
plt.title('필터')
plt.subplot(1, 3, 3)
plt.imshow(result, cmap='gray')
plt.title('필터링 결과')
plt.tight_layout()
plt.savefig('image_filtering.png')  # 그래프 저장
plt.close()

# 3. 시계열 분석 기초: 이동 평균
# 가상의 시계열 데이터 생성
time_series = np.cumsum(np.random.normal(0, 1, 100))  # 랜덤 워크 시계열
print("\n시계열 데이터 일부:", time_series[:10])

# 이동 평균 계산 함수
def moving_average(arr, window_size):
    weights = np.ones(window_size) / window_size
    return np.convolve(arr, weights, mode='valid')

# 여러 윈도우 크기로 이동 평균 계산
ma_5 = moving_average(time_series, 5)
ma_10 = moving_average(time_series, 10)
ma_20 = moving_average(time_series, 20)

plt.figure(figsize=(12, 6))
plt.plot(time_series, label='원본 시계열')
plt.plot(np.arange(4, len(time_series)), ma_5, label='5일 이동 평균')
plt.plot(np.arange(9, len(time_series)), ma_10, label='10일 이동 평균')
plt.plot(np.arange(19, len(time_series)), ma_20, label='20일 이동 평균')
plt.legend()
plt.title('시계열 데이터와 이동 평균')
plt.xlabel('시간')
plt.ylabel('값')
plt.tight_layout()
plt.savefig('time_series_ma.png')  # 그래프 저장
plt.close()

# 4. 머신러닝 기초: 선형 회귀
# 데이터 생성
X = np.random.rand(100, 1) * 10  # 특성 하나
y = 2 * X + 1 + np.random.randn(100, 1)  # y = 2x + 1 + 노이즈

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

print("\n선형 회귀 결과:")
print("기울기:", model.coef_[0][0])
print("절편:", model.intercept_[0])

# 그래프로 시각화
plt.figure(figsize=(10, 6))
plt.scatter(X_train, y_train, color='blue', label='학습 데이터')
plt.scatter(X_test, y_test, color='red', label='테스트 데이터')
plt.plot(X_test, y_pred, color='green', label='예측 선')
plt.title('선형 회귀')
plt.xlabel('X')

# NumPy 주말 집중 학습 커리큘럼 (계속)

## 2일차 (계속)

### 4. 실전 응용 예제 (계속)

```python
# 선형 회귀 그래프 계속
plt.ylabel('y')
plt.legend()
plt.tight_layout()
plt.savefig('linear_regression.png')  # 그래프 저장
plt.close()
```

### 5. 고급 NumPy 기능 (2시간)
- 구조화된 배열 (structured arrays)
- 메모리 뷰와 스트라이드
- 범용 함수 만들기 (ufunc)
- 병렬 처리와 최적화

```python
import numpy as np

# 1. 구조화된 배열 (structured arrays)
# 여러 데이터 타입을 가진 배열 생성
dt = np.dtype([('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])
people = np.array([
    ('홍길동', 30, 68.5),
    ('김철수', 25, 75.2),
    ('이영희', 35, 58.7)
], dtype=dt)

print("구조화된 배열:")
print(people)
print("\n이름만 추출:", people['name'])
print("나이만 추출:", people['age'])

# 나이를 기준으로 정렬
print("\n나이순 정렬:")
print(np.sort(people, order='age'))

# 필드 추가
people_extended = np.zeros(3, dtype=dt.descr + [('height', 'f4')])
people_extended['name'] = people['name']
people_extended['age'] = people['age']
people_extended['weight'] = people['weight']
people_extended['height'] = [175.0, 180.5, 165.3]

print("\n확장된 배열:")
print(people_extended)

# 2. 메모리 뷰와 스트라이드
arr = np.arange(16).reshape(4, 4)
print("\n원본 배열:\n", arr)
print("모양:", arr.shape)
print("스트라이드:", arr.strides)  # 바이트 단위 스트라이드

# 스트라이드 조작으로 전치 행렬 만들기
arr_t = np.lib.stride_tricks.as_strided(arr, shape=(4, 4), strides=(arr.strides[1], arr.strides[0]))
print("\n스트라이드 조작으로 만든 전치 행렬:\n", arr_t)

# 3. 범용 함수 만들기 (ufunc)
# 기존 함수를 ufunc으로 변환
def custom_sigmoid(x):
    return 1 / (1 + np.exp(-x))

sigmoid_ufunc = np.frompyfunc(custom_sigmoid, 1, 1)

test_arr = np.array([-2, -1, 0, 1, 2])
print("\n테스트 배열:", test_arr)
print("사용자 정의 시그모이드 함수 결과:", sigmoid_ufunc(test_arr))

# 4. 병렬 처리와 최적화 설정
# NumPy가 사용하는 스레드 수 확인
print("\nNumPy가 사용하는 스레드 수:", np.show_config())
# 참고: 스레드 수는 환경에 따라 다를 수 있습니다.

# 행렬 연산 성능 테스트
import time

# 큰 행렬 생성
n = 1000
A = np.random.rand(n, n)
B = np.random.rand(n, n)

# 행렬 곱셈 시간 측정
start_time = time.time()
C = np.dot(A, B)
end_time = time.time()

print(f"\n{n}x{n} 행렬 곱셈 시간: {end_time - start_time:.4f}초")
```

### 6. 실전 프로젝트: 데이터 분석 미니 프로젝트 (3시간)
- 실제 데이터셋 분석
- 데이터 전처리, 탐색, 시각화
- NumPy를 활용한 통계 분석
- 결과 해석 및 보고서 작성

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# 1. 데이터 로드 (예: Iris 데이터셋) - pandas 사용
# 실제로는 다음과 같이 데이터를 로드할 수 있습니다:
# from sklearn.datasets import load_iris
# iris = load_iris()
# data = iris.data
# target = iris.target
# feature_names = iris.feature_names
# target_names = iris.target_names

# 간단한 예제를 위해 직접 데이터 생성
np.random.seed(42)
n_samples = 150
n_features = 4

# 세 개의 클러스터 특성 생성
centers = np.array([
    [5.0, 3.5, 1.5, 0.2],  # 클래스 0
    [6.5, 3.0, 5.5, 2.0],  # 클래스 1
    [5.5, 2.5, 4.0, 1.3]   # 클래스 2
])
cluster_std = [0.4, 0.5, 0.3]

# 각 클래스별로 50개 샘플 생성
X = np.vstack([
    np.random.normal(centers[0], cluster_std[0], (50, n_features)),
    np.random.normal(centers[1], cluster_std[1], (50, n_features)),
    np.random.normal(centers[2], cluster_std[2], (50, n_features))
])
y = np.concatenate([np.zeros(50), np.ones(50), np.ones(50) * 2])

feature_names = ['꽃받침 길이', '꽃받침 너비', '꽃잎 길이', '꽃잎 너비']
target_names = ['setosa', 'versicolor', 'virginica']

print("데이터 형태:", X.shape)
print("클래스별 샘플 수:", np.bincount(y.astype(int)))

# 2. 기본 통계 계산
print("\n기본 통계량:")
for i, feature in enumerate(feature_names):
    print(f"{feature}:")
    print(f"  평균: {np.mean(X[:, i]):.2f}")
    print(f"  표준편차: {np.std(X[:, i]):.2f}")
    print(f"  최소값: {np.min(X[:, i]):.2f}")
    print(f"  최대값: {np.max(X[:, i]):.2f}")

# 클래스별 통계량
print("\n클래스별 통계량:")
for target in range(3):
    print(f"\n{target_names[target]}:")
    class_data = X[y == target]
    for i, feature in enumerate(feature_names):
        print(f"  {feature} 평균: {np.mean(class_data[:, i]):.2f}")

# 3. 상관관계 분석
corr_matrix = np.corrcoef(X.T)
print("\n특성 간 상관관계 행렬:")
print(corr_matrix)

# 상관관계 히트맵 시각화
plt.figure(figsize=(10, 8))
plt.imshow(corr_matrix, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(np.arange(len(feature_names)), feature_names, rotation=45)
plt.yticks(np.arange(len(feature_names)), feature_names)
plt.title('특성 간 상관관계 히트맵')
for i in range(len(feature_names)):
    for j in range(len(feature_names)):
        plt.text(j, i, f'{corr_matrix[i, j]:.2f}', ha='center', va='center', color='black')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.close()

# 4. 데이터 표준화
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("\n표준화 전 첫 번째 샘플:", X[0])
print("표준화 후 첫 번째 샘플:", X_scaled[0])

# 5. 주성분 분석 (PCA)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
print("\nPCA 변환 후 형태:", X_pca.shape)
print("설명된 분산 비율:", pca.explained_variance_ratio_)
print("누적 설명된 분산:", np.sum(pca.explained_variance_ratio_))

# PCA 결과 시각화
plt.figure(figsize=(10, 8))
colors = ['red', 'green', 'blue']
for target, color in zip(range(3), colors):
    plt.scatter(X_pca[y == target, 0], X_pca[y == target, 1], color=color, alpha=0.7, label=target_names[target])
plt.title('PCA로 차원 축소된 꽃 데이터')
plt.xlabel('첫 번째 주성분')
plt.ylabel('두 번째 주성분')
plt.legend()
plt.tight_layout()
plt.savefig('pca_visualization.png')
plt.close()

# 6. 특성별 히스토그램
plt.figure(figsize=(12, 10))
for i, feature in enumerate(feature_names):
    plt.subplot(2, 2, i+1)
    for target, color in zip(range(3), colors):
        plt.hist(X[y == target, i], bins=10, color=color, alpha=0.5, label=target_names[target])
    plt.title(feature)
    plt.xlabel('값')
    plt.ylabel('빈도')
    if i == 0:
        plt.legend()
plt.tight_layout()
plt.savefig('feature_histograms.png')
plt.close()

# 7. 특성 간 산점도
plt.figure(figsize=(12, 10))
plt.subplot(2, 2, 1)
for target, color in zip(range(3), colors):
    plt.scatter(X[y == target, 0], X[y == target, 1], color=color, alpha=0.7, label=target_names[target])
plt.title(f'{feature_names[0]} vs {feature_names[1]}')
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[1])
plt.legend()

plt.subplot(2, 2, 2)
for target, color in zip(range(3), colors):
    plt.scatter(X[y == target, 2], X[y == target, 3], color=color, alpha=0.7)
plt.title(f'{feature_names[2]} vs {feature_names[3]}')
plt.xlabel(feature_names[2])
plt.ylabel(feature_names[3])

plt.subplot(2, 2, 3)
for target, color in zip(range(3), colors):
    plt.scatter(X[y == target, 0], X[y == target, 2], color=color, alpha=0.7)
plt.title(f'{feature_names[0]} vs {feature_names[2]}')
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[2])

plt.subplot(2, 2, 4)
for target, color in zip(range(3), colors):
    plt.scatter(X[y == target, 1], X[y == target, 3], color=color, alpha=0.7)
plt.title(f'{feature_names[1]} vs {feature_names[3]}')
plt.xlabel(feature_names[1])
plt.ylabel(feature_names[3])
plt.tight_layout()
plt.savefig('feature_scatterplots.png')
plt.close()

# 8. 간단한 분류: 결정 경계 시각화
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# 주성분 분석 결과로 로지스틱 회귀 학습
model = LogisticRegression(max_iter=1000)
model.fit(X_pca, y)

# 결정 경계 시각화를 위한 그리드 생성
h = 0.02  # 그리드 간격
x_min, x_max = X_pca[:, 0].min() - 1, X_pca[:, 0].max() + 1
y_min, y_max = X_pca[:, 1].min() - 1, X_pca[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(10, 8))
plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.coolwarm)
for target, color in zip(range(3), colors):
    plt.scatter(X_pca[y == target, 0], X_pca[y == target, 1], color=color, alpha=0.8, label=target_names[target])
plt.title('PCA 공간에서의 결정 경계')
plt.xlabel('첫 번째 주성분')
plt.ylabel('두 번째 주성분')
plt.legend()
plt.tight_layout()
plt.savefig('decision_boundary.png')
plt.close()

# 9. 모델 평가
y_pred = model.predict(X_pca)
accuracy = accuracy_score(y, y_pred)
conf_matrix = confusion_matrix(y, y_pred)

print("\n모델 평가:")
print(f"정확도: {accuracy:.4f}")
print("\n혼동 행렬:")
print(conf_matrix)

# 10. 결과 요약 보고서 문자열
summary_report = """
# 꽃 데이터 분석 요약 보고서

## 1. 데이터 개요
- 샘플 수: 150개 (각 클래스당 50개)
- 특성 수: 4개 (꽃받침 길이, 꽃받침 너비, 꽃잎 길이, 꽃잎 너비)
- 클래스: setosa, versicolor, virginica

## 2. 탐색적 데이터 분석
- 꽃잎 길이와 꽃잎 너비는 강한 양의 상관관계를 보임
- 꽃받침 길이와 꽃받침 너비는 약한 상관관계를 보임
- 각 클래스는 꽃잎 크기에서 뚜렷한 차이를 보임

## 3. 주성분 분석 (PCA)
- 2개의 주성분으로 전체 분산의 약 {np.sum(pca.explained_variance_ratio_):.2%} 설명 가능
- 첫 번째 주성분만으로도 전체 분산의 약 {pca.explained_variance_ratio_[0]:.2%} 설명 가능
- PCA 공간에서 클래스 간 분리가 명확하게 나타남

## 4. 분류 모델
- 로지스틱 회귀 모델 사용
- 정확도: {accuracy:.2%}
- 혼동 행렬 분석: 클래스 간 오분류가 매우 적음

## 5. 결론
- 꽃잎의 특성이 꽃 종류 분류에 중요한 역할을 함
- PCA를 통한 차원 축소로도 높은 분류 성능 유지 가능
- 특성 간 상관관계 분석이 데이터 이해에 중요
"""

print("\n결과 요약 보고서:")
print(summary_report)

# 보고서를 텍스트 파일로 저장
with open('data_analysis_report.txt', 'w', encoding='utf-8') as f:
    f.write(summary_report)
```

## 학습 포인트 요약

### 1일차: NumPy 기초와 배열 조작
- NumPy의 기본 개념과 파이썬 리스트와의 차이점
- 다양한 배열 생성 방법 (zeros, ones, arange, linspace, random 등)
- 배열 속성 (shape, size, dtype) 및 기본 조작
- 인덱싱과 슬라이싱 기법
- 고급 인덱싱 (정수 배열, 불리언 마스킹)

### 2일차: NumPy 연산과 활용
- 기본 수학 연산 및 유니버설 함수
- 배열 브로드캐스팅의 규칙과 활용
- 고급 배열 조작 (전치, 축 변경, 정렬)
- 선형 대수 연산 (행렬 곱셈, 역행렬, 고유값)
- 실전 응용 예제 (데이터 분석, 이미지 처리, 시계열 분석)
- 구조화된 배열과 고급 NumPy 기능
- 데이터 분석 미니 프로젝트

## 추가 학습 리소스

1. 공식 NumPy 문서: https://numpy.org/doc/stable/
2. NumPy 치트 시트: https://numpy.org/doc/stable/user/cheatsheet.html
3. 양질의 튜토리얼:
   - Python Data Science Handbook: https://jakevdp.github.io/PythonDataScienceHandbook/
   - W3Schools NumPy Tutorial: https://www.w3schools.com/python/numpy/default.asp
   - Real Python NumPy Tutorials: https://realpython.com/tutorials/numpy/

## 학습 후 시도해볼 수 있는 프로젝트

1. 이미지 처리 프로젝트 (필터 적용, 이미지 변환)
2. 주식 데이터 분석 (수익률 계산, 이동 평균 계산, 상관관계 분석)
3. 시계열 데이터 분석 및 예측
4. 간단한 머신러닝 알고리즘 구현 (k-means 클러스터링, 선형 회귀)
5. 오디오 신호 처리 (푸리에 변환 적용)

이 커리큘럼을 통해 NumPy의 기본부터 실전 활용까지 체계적으로 학습할 수 있습니다. 꾸준히 실습하고 응용해보면서 데이터 과학의 기초를 다져보세요!
