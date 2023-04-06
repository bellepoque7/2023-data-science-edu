# 정리 

## 모델의 구성요소
### 1. 레이어
1.1 MLP
- w(weight)x + b(bias) => perceptron(단일)
- 다층 -> Muliti layer perceptron -> MLP
- MLP =  분류기 =  FCL  = Dense = output Layer

1.2 컨볼루션 레이어
- 이미지나 매트릭스 형태의 데이터에서 Feature
- Kernel = Filter 필터의 크기만큼 합성곱(Convolution) 이미지혹은 행렬에서 Feature
- Kernel 의 갯수 = Output으로 나오는 Depth
- padding = 컨볼루션 레이어를 통과 한 후 이미지가 작아지는것을 방지하기 위해서 0(padding)
- strides = 필터가 컨볼루션 곱하면서 이동할때 몇 칸씩 이동할지

1.3 RNN LSTM
- 데이터의 시간의 흐름(Sequence)을 처리해 주기 위해 
- h(x)t = act(h(x)t-1 + wx + b)

### 2. 손실함수
- 모델이 학습하는 중, 얼마만큼 틀렸는지 정확한 점수를 계산하기 위한 '함수'
- MSE : sum(y - h) / m(갯수) = MAE(absolute) 회귀
- CE : 분류 문제 / 정답을 맞췄는지, 틀렸는지 , 정답에 얼마만큼 확신을 가지고 예측했는지

## 3. 최적화 함수
- GD -> SGD (batch - size) -> Momentum (누적합으로 보다 빠르게 Gradient를 계산)
- 보통 최신 최적화 함수가 좋은 경향을 보임

### 분야
### 이미지 처리
- 분류
- Bottle neck layer( google net - Inception)
- 분류라는 테스크지만, 모든 이미지 처리 논문의 어머니가 되는 분야

### 자연어 처리
- 번역 (Seq to Seq)
- 번역이나 Language Modeling 분야가 NLP쪽 어머니가 되는 분야

감정분류
### 추천 시스템
- Meta Learning, MetaHin(딥논읽)

### 음성/음향/오디오 처리


### Semisupervised learning
정답데이터가 있는 데이터와 정답데이터가 없는 데이터를 섞어서 학습

### fewshot learning(zero shot , one shot)
사전 학습 된 모델에, 우리의 아주 적은 데이터만 보여줘서 추가 학습을 시킴
