![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FDataNetworkAnalysis%2FBaseball-Crowd-Prediction)

# KBO 야구 관중객 수 예측
*Predicting KBO Game Attendance*

한국프로야구 관중 수는 1980년대 초반 약 140만 명을 시작으로 2018년에는 약 800만명으로, 한국 스포츠의 주요 종목으로 성장해왔습니다. 특히 2016년에는 840만 명으로 역대 최다 관중 수를 갱신하며, 한국프로야구의 입지를 증명했습니다.

![](https://github.com/bllfpc/DataNetworkAnalysis/blob/master/BaseballCrowdPrediction/images/attandence_year.png)

이처럼 한국 프로 스포츠 발전의 가장 중요한 관심사 중 하나는 관중 수라고 할 수 있습니다. 관중 수는 구단의 경영 측면과 직결되는 요소로써, 입장료부터 기타 시설의 이용료 등 다양한 수입을 통해 구단의 안정적인 재정 운영을 가능케합니다. 또한, 수요예측은 한국 프로 스포츠의 마케팅과 구단의 예산 전략 수립에 활용될 수 있습니다.[1]


## Data Source
- 수집기간 : 2017~2019년 정규시즌
- KBO 기록실에서 일자별 관중현황 데이터를 수집
  - https://bit.ly/33u7MIs
- 각 일자별 경기 기록(승, 패)을 statiz에서 수집
  - https://bit.ly/2YVDriB
- 기상청에서 지역별 일자별 데이터 수집
  - https://bit.ly/2KxGLgS
  
## Anaysis Precess
- [Page 1: Data Crawling](https://www.notion.so/tootouch/Page-1-2-1-57ca7c027cd34a0db3674a04e7eaf25b)
- [Page 2: Preprocessing & Analysis](https://www.notion.so/tootouch/Page-2-2-2-2036cdc86b33413b9fd60cbd3d7ea23a)

## Reference
1. Park, J., & Park, S. (2017). A Study on Prediction of Attendance in Korean Baseball League Using Artificial Neural Network. 정보처리학회논문지/소프트웨어 및 데이터 공학 제, 6(12), 12.
