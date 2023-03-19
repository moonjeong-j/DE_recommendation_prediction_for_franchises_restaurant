import pandas as pd

#서비스2 : 프랜차이즈 추천 서비스
#index.html, result.html 페이지에서 쓰임
#주어진 조건으로 데이터 프레임을 필터링, 정렬하는 함수
def filtering_data(df, category, cost, is_checked_1, is_checked_2, is_checked_3, is_checked_4, is_checked_5, is_checked_6, first, second, third):
    
    #category 필터링, category 인것만
    df = df[df['category']==category]
    
    #cost 필터링, cost보다 작거나 같은 것만
    df=df[pd.to_numeric(df['cost'])<=int(cost)]
    
    #year 필터링
        # "is_checked_1" -> 상관없음 -> df 전체
        # "is_checked_2" -> 0년-4년 포함
        # "is_checked_3" -> 5년-9년 포함
        # "is_checked_4" -> 10년-19년 포함
        # "is_checked_5" -> 20년-29년 포함
        # "is_checked_6" -> 30년 이상 포함
    print(is_checked_1, 'is_checked_1')
    if is_checked_1 == "on":
        pass
    else:
        df_temp=None
        if is_checked_2 =="on":
            df_temp = pd.concat([df_temp ,df[df['year']<=4]])
            print(df, '데이터 입니다')   
        if is_checked_3 =="on":
            df_temp = pd.concat([df_temp ,df[(df['year']>=5) & (df['year']<=9)]])
        if is_checked_4 =="on":
            df_temp = pd.concat([df_temp ,df[(df['year']>=10) & (df['year']<=19)]])
        if is_checked_5 =="on":
            df_temp = pd.concat([df_temp ,df[(df['year']>=20) & (df['year']<=29)]])
        if is_checked_6 =="on":
            df_temp = pd.concat([df_temp ,df[df['year']>=30]])    
        df=df_temp
    
    #first 필터링, 
        #없으면 pass
        #first에 해당되는 컬럼은 4점 이상인 것만 필터링
        #단, fairness는 max값이 3이므로 3인것만 필터링
    if first == "없음":
        pass
    elif first =='profit':
        df=df[df['profit']>=4]
    elif first =="growth":
        df=df[df['growth']>=4]
    elif first =="fairness":
        df=df[df['fairness']>=3]
    elif first =="stability":
        df=df[df['stability']>=4]  
    
    #second 필터링
        #없으면 pass
        #second에 해당되는 컬럼은 3점 이상인 것만 필터링
        #단, fairness는 max값이 3이므로 2점 이상인 것만 필터링
    if first == "없음":
        pass
    elif second =='profit':
        df=df[df['profit']>=3]
    elif second =="growth":
        df=df[df['growth']>=3]
    elif second =="fairness":
        df=df[df['fairness']>=2]
    elif second =="stability":
        df=df[df['stability']>=3]  
        
    #third 필터링
        #없으면 pass
        #third 해당되는 컬럼은 2점 이상인 것만 필터링
        #단, fairness는 max값이 3이므로 1점 이상인 것만 필터링
    if first == "없음":
        pass
    elif third =='profit':
        df=df[df['profit']>=2]
    elif third =="growth":
        df=df[df['growth']>=2]
    elif third =="fairness":
        df=df[df['fairness']>=1]
    elif third =="stability":
        df=df[df['stability']>=2] 
    
    #필터링, 정렬
    check_list = ['profit', 'growth', 'fairness', 'stability']
    is_error=0
    #first, second, third 다 입력했을 때
    #(첫번째 중요한컬럼 -> 두번째 중요한컬럼-> 세번째 중요한컬럼-> 네번째 중요한컬럼 순) 기준으로 하여 정렬
    if ((first!="없음") & (second!="없음") & (third!="없음")):
        check_list.remove(first)
        check_list.remove(second)
        check_list.remove(third)
        check_list[0]
        df=df.sort_values(by=[first, second, third, check_list[0]], ascending=False)
    #first, second만 입력했을 때
    #(첫번째 중요한컬럼 -> 두번째 중요한컬럼-> 리스트의 남은 첫번째 원소 -> 리스트의 남은 두 번째 원소) 순 기준으로 하여 정렬
    elif ((first!="없음") &  (second!="없음") & (third=="없음")):
        check_list.remove(first)
        check_list.remove(second)
        df=df.sort_values(by=[first, second, check_list[0], check_list[1]], ascending=False)
    #first만 입력했을 때
    #(첫번째 중요한컬럼 -> 리스트의 남은 첫번째 원소 -> 리스트의 남은 두 번째 원소->리스트의 남은 세 번째 원소) 순 기준으로 하여 정렬
    elif ((first!="없음") &  (second=="없음") & (third=="없음")):
        check_list.remove(first)
        df=df.sort_values(by=[first,check_list[0],check_list[1],check_list[2]], ascending=False)
    #셋 다 입력하지 않았을 때
    #(리스트의 남은 첫번째 원소 -> 리스트의 남은 두 번째 원소->리스트의 남은 세 번째 원소 ->리스트의 남은 네 번째 원소)순 기준으로 하여 정렬
    elif ((first=="없음") &  (second=="없음") & (third=="없음")):
        df=df.sort_values(by=[check_list[0],check_list[1],check_list[2],check_list[3]], ascending=False)
    #위 4가지 경우에 해당하지 않았을 때
    #예를 들어 first를 입력하지 않고, second를 입력했을 때
    #is_error=1 로 변경
    else:
        is_error=1
    
    return df, is_error
    

#서비스3 : 매출 예측 서비스
#predict.html, predict_result.html 페이지에서 쓰임
# "5. ml_model.ipynb"를 통해 만든 "model_pickle.model"을 활용하여 매출 예측
def predict_sales(statff_cnt, cost_per_area, nums_of_franchisees, new_nums_of_franchisee, start_cost, category_predict, year, debt_ratio):
    # import pickle
    import joblib
    import sklearn
    
    model_pickle = joblib.load(open("sales_predict_model_new.model", 'rb'))
    predicted_sales=model_pickle.predict(pd.DataFrame([[statff_cnt, cost_per_area, nums_of_franchisees, new_nums_of_franchisee, start_cost, category_predict, year, debt_ratio]],
                                                       columns =["statff_cnt", "cost_per_area", "nums_of_franchisees", "new_nums_of_franchisee", "start_cost", "category", "year", "debt_ratio"]
                                                       )
                                          )
    return predicted_sales
