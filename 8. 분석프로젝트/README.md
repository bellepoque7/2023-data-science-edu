## 데이터 분석 프로세스 익히기

- 목적: 데이터 분석 프로젝트를 시작하기 위한 개괄적인 개념을 담습니다. 실습은 최소화하고 스스로 찾아서 공부하는 것을 지향합니다.

1. 가설설정
2. 데이터 수집
3. 분석 및 시각화
4. 모델링
5. 평가


## 개념
- 개념
  - 독립변수(입력 데이터)와 종속변수(정답 데이터)
  - 지도학습: 입력데이터와 정답데이터를 모두 알려주고 알고리즘에 학습 시키는 것. 종속 변수의 형태에 따라 회귀,분류문제로 구분 됩니다.
    - ex1) 타이타닉 승객의 정보에 따른 사망유무를 예측하자 -> 분류문제
    - ex2) 과거의 주가를 바탕으로 현재의 주가를 예측하자 -> 회귀문제
  - 비지도학습: 정답데이터 없이 입력데이터의 수치만으로 수행하는 알고리즘
    - ex3) 군집화(clustering)
    <img width="700" alt="image" src="https://user-images.githubusercontent.com/39439424/230241003-c004eb0b-3ca7-4b22-a754-9ff24b005a51.png">
    (트위터 심클러스터링)[https://github.com/twitter/the-algorithm/blob/main/src/scala/com/twitter/simclusters_v2/README.md]

- 머신러닝과 딥러닝: [한장요약](https://github.com/bellepoque7/2023-data-science-edu/blob/main/8.%20%EB%B6%84%EC%84%9D%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/MLvsDL.png)
    - 머신러닝: 통계적 알고리즘을 기반(모듈: sckit-learn)
    - 딥러닝: Perceptron 을 기반. 입력데이터에서 feature 를 추출하여 예측. 내부 구조가 복잡하여 해석력하기 힘듬 black box 형태를 띄고 있음.(모듈: tensorflow, pytorch)
      머신러닝의 발전 속에서 한줄기로 분화된 것이 딥러닝. 베타적인 구분을 하자면 통계적 알고리즘과 딥러닝으로 나눌 수 있겟지만, 현재는 머신러닝과 딥러닝으로 통용됨
      
      
 Q) 딥러닝이면 만사오케이 아닌가요? 그냥 입력 데이터 밀어넣고 정답 데이터 주면 알아서 학습하지 않아요?
 A) 네 아닙니다. Garbage In Garbage Out 이라는 오래된 격언이 있습니다. 그래서 탐색적 데이터 분석(Exploaratory Analysis)가 필요합니다.
 
 Q) 딥러닝은 선형적이지 않은 두 입력,정답데이터의 관계도 예측할 수 있으니까 굳이 산점도 등 선형분석이 필요하지 않지 않아요?
 A) 딥러닝과 같은 비선형적 관계를 도출하는 모델에서도 상관관계 분석을 하여 변수 중요도를 도출 할 수 있습니다. 변수 선택을 위한 방법은 다음 4가지가 있습니다.
 - 상관 관계 분석
 - 통계적 검정: t-test, ANOVA
 - 변수 선택 알고리즘: Lasso, Ridge, Elastic Net
 - 도메인 기반 검토
 
 Q) 어떤 독립변수가 종속변수에 영향이 있는지 모르겠습니다. 다 밀어넣으면 안되나요?
 A) Garbage In Garbage Out 입니다.  데이터를 가공하여 의미있게 만들고, 검증(validation)과 평가(test) 데이터를 구분하여 과적합을 방지해야합니다. 과적합을 방지하는 방법에는 다음과 같은 분류가 있습니다. 
 - 데이터의 양늘리기
 - 모델의 복잡도 줄이기
 - Regularization: L1,L2 규제
 - Drop out: 딥러닝의 경우 노드를 무시합니다.
 - Early Stopping: 학습과정에서 validation loss가 더이상 감소하지 않을 때 학습을 중지하는 방법 입니다.
 - 
  
