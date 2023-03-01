## 외식업 예비 창업자를 위한 프랜차이즈 브랜드 추천과 창업시 매출 예상 프로그램
## 1. 프로젝트 설명


(1) 주제 및 데이터 소개
- 주제 : **외식업 예비 창업자 개인에 맞는 프랜차이즈 브랜드 추천 + 창업시 매출 예상**
- 데이터 : 경기도 가맹정보 시스템(https://fair.gg.go.kr/fran/search/searchList.do) bs4, selenuium을 통해 크롤링
- 16*5369 data

(2) 구현 파이프라인
<img width="776" alt="image" src="https://user-images.githubusercontent.com/102526342/222263135-c5b54bd6-9326-4493-a9f6-20c083fb6929.png">

(3) 앱의 전체 구성


## 2. 서비스 시연


### (1) 서비스1 : 대시보드
- 수익성, 면적당 매출 가성비, 총 매출, 브랜드화 등 창업시 고려 요소들에 대한 분석을 대시보드 메뉴에 제시
- 외식 분야 별 추천할만한 브랜드 TOP5 제시

![image](https://user-images.githubusercontent.com/102526342/222255550-3e6f634a-9d68-4c0d-8aad-c65187930880.png)
![image](https://user-images.githubusercontent.com/102526342/222255613-872cc13f-3e95-4038-8a9f-f744744290d6.png)
![image](https://user-images.githubusercontent.com/102526342/222255653-a9616a82-abb7-43af-ac68-ee3eb3e18927.png)

### (2) 서비스2 : 프랜차이즈 추천
- 카테고리, 창업비용, 본사업력, 중요하게 생각하는 요소(1-3순위)를 입력하면 외식업 프랜차이즈 브랜드를 추천
- 중요하게 생각하는 요소(1-3순위)에 따른 filtering, ordering

![image](https://user-images.githubusercontent.com/102526342/222256110-fdbeada5-e8f5-4316-8d42-1d81643fecdb.png)

![image](https://user-images.githubusercontent.com/102526342/222256267-c7b5e1a0-125a-42a1-ac39-f40d4ca1f38b.png)

### (3) 서비스3 : 매출 예측
- 총 창업 비용, 면적당 인테리어 비용, 전체 가맹점 수, 신규 가맹점 수 , 신규 개점 수, 가맹 사업 임직원 수, 본사 업력, 본사 부채 비율
- 연 평균 총 매출액과 월 평균 총 매출액을 예측하는 서비스

![image](https://user-images.githubusercontent.com/102526342/222256382-a8a020cb-a0a4-4774-830a-5a73f9b7b288.png)

### (4) 용어설명 페이지
- 서비스2(프랜차이즈 추천)에서 알아야 하는 수익성, 공정성, 성장성, 안정성에 대한 용어 설명

![image](https://user-images.githubusercontent.com/102526342/222256799-2251998a-5fc2-45dc-bd57-bb4028cdb0a2.png)

