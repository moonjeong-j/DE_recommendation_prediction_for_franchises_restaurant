from flask import Flask, render_template, request
import pandas as pd
import db
import model

#data load
df = db.data_load_sqlite()


#flask
app = Flask(__name__)

#서비스 2 - 프랜차이즈 추천 서비스 페이지
@app.route('/')
def user_input():
   #'index.html'를 찾아서 연다
   return render_template('index.html')

#'index.html'의 input값을 받아온다
@app.route('/result',methods = ['POST', 'GET'])
def result():
   global df
   
   if request.method == 'POST':
      
      category = request.form["category"]   
      cost = int(request.form["cost"]) 
      
      is_checked_1 = request.form.get('option1')
      is_checked_2 = request.form.get('option2')
      is_checked_3 = request.form.get('option3')
      is_checked_4 = request.form.get('option4')
      is_checked_5 = request.form.get('option5')
      is_checked_6 = request.form.get('option6')
      first = request.form["first"] 
      second = request.form["second"] 
      third = request.form["third"] 
      
  
      
      # db.data_load_sqlite()로 데이터 프레임 받아옴
      df = db.data_load_sqlite()
      #model.filtering_data로 필터링, 오더링
      df, is_error = model.filtering_data(df, category, cost, is_checked_1, is_checked_2, is_checked_3, is_checked_4, is_checked_5, is_checked_6, first, second, third)
      
      
      if is_error==1:
         #is_error==1 이면 조건을 다시설정하라는 문구가 뜨게 df_list =[]깂을 넘겨준다
         return render_template("result.html", df_list =[])
      else:
         df_list=df.values.tolist()
         #"result.html"페이지로 df_list =df_list 값을 넘겨준다
         return render_template("result.html", df_list =df_list)

      


#서비스 3 - 매출 예측 서비스 페이지
@app.route('/predict')
def predict():
   return render_template('predict.html')
   
#'predict.html'에서 input값을 받아온다
@app.route('/predict_result', methods = ['POST', 'GET'])
def predict_result():
   if request.method == 'POST':
      #user input 받아오기
      category_predict = request.form.get("category_predict")  
      start_cost = int(request.form.get("start_cost")) 
      cost_per_area = int(request.form.get("cost_per_area")) 
      nums_of_franchisees = int(request.form.get("nums_of_franchisees")) 
      new_nums_of_franchisee = int(request.form.get("new_nums_of_franchisee")) 
      statff_cnt = (request.form.get("statff_cnt")) 
      year = int(request.form.get("year")) 
      debt_ratio = int(request.form.get("debt_ratio")) 
      predicted_sales=int(model.predict_sales(statff_cnt, cost_per_area, 
      nums_of_franchisees, new_nums_of_franchisee, start_cost, category_predict, 
      year, debt_ratio) )
      predicted_sales_month =int(predicted_sales/12)
      
      #'predict_result.html' 페이지로 predicted_sales=predicted_sales, predicted_sales_month=predicted_sales_month 값을 넘겨준다
      return render_template('predict_result.html', predicted_sales=predicted_sales, predicted_sales_month=predicted_sales_month)
   
       
       
# 정보 제공 페이지
@app.route('/result_info')
def result_info():
   return render_template('info.html')

# 서비스 1- 대시보드
@app.route('/dashboard')
def dashboard():
   return render_template('dashboard.html')


if __name__ == '__main__':
   app.run('0.0.0.0', port=4000, debug=False)


