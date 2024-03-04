import pandas as pd
from pycaret.regression import *

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
print(predictions)
