from flask import Flask, render_template
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd
from pycaret.regression import *

app = Flask(__name__)

@app.route('/')
def index():
    # อ่านข้อมูลจากไฟล์ CSV
    file_path = 'cleaned_air4thai.csv'
    data = pd.read_csv(file_path)

    # ลบแถวที่มีค่าที่ขาดหายไปใน 'PM25'
    data = data.dropna(subset=['PM25'])

    # โปรแกรม Setup ด้วยข้อมูล
    regression_setup = setup(data, target='PM25', session_id=123, fold_strategy='timeseries', fold=3, data_split_shuffle=False, fold_shuffle=False)

    # เลือกและเทรนโมเดล
    best_model = compare_models()

    # สร้าง DataFrame สำหรับทำนาย PM25 ล่วงหน้า 7 วัน
    predict_data = data.copy()
    predict_data['DATETIMEDATA'] = pd.to_datetime(predict_data['DATETIMEDATA']) + pd.DateOffset(days=7)

    # ทำนาย PM25 ล่วงหน้า 7 วัน
    predictions = predict_model(best_model, data=predict_data)

    # สร้างกราฟเส้น
    plt.figure(figsize=(10, 6))
    plt.plot(predictions['Label'], label='Predicted PM25')
    plt.plot(data['PM25'], label='Actual PM25', alpha=0.7)
    plt.title('Predicted vs Actual PM25')
    plt.xlabel('Index')
    plt.ylabel('PM25')
    plt.legend()
    
    # แปลงกราฟเป็นรูปภาพ
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    
    return render_template(plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)


