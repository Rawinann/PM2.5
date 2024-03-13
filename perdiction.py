import pandas as pd
from datetime import datetime, timedelta
from pycaret.regression import load_model, predict_model

# สมมติว่าวันสุดท้ายในชุดข้อมูลของคุณคือ '2024-01-02'
last_date_in_dataset = datetime(2024, 3, 3)

# สร้างช่วงเวลาสำหรับ 7 วันข้างหน้า, ทุก ๆ ชั่วโมง
future_dates = [last_date_in_dataset + timedelta(days=i, hours=h) for i in range(1, 8) for h in range(24)]

# สร้าง DataFrame
future_data = pd.DataFrame(future_dates, columns=['DATETIMEDATA'])

# คำนวณ features ที่จำเป็น
future_data['hour'] = future_data['DATETIMEDATA'].dt.hour
future_data['day_of_week'] = future_data['DATETIMEDATA'].dt.dayofweek
future_data['day'] = future_data['DATETIMEDATA'].dt.day
future_data['month'] = future_data['DATETIMEDATA'].dt.month

# เพิ่ม stationID เข้าไปใน future_data
# future_data['stationID'] = '44t'  # แทน 'your_station_id' ด้วยค่าที่ถูกต้อง

# ตรวจสอบ future_data
print(future_data.head())

# โหลดโมเดลที่บันทึกไว้
final_model = load_model('PM2.5/model/final_pm25_prediction_model')

# ทำนายค่า PM2.5 ในอนาคต
predictions = predict_model(final_model, data=future_data)

# แสดงผลลัพธ์การทำนาย
print(predictions)
# บันทึกผลลัพธ์เป็นไฟล์ CSV
predictions.to_csv("PM2.5/data/Hourly_predict.csv", index=False)





# สร้างข้อมูลที่จะใช้เก็บการทำนายรายวัน
daily_predictions = pd.DataFrame()

# นับจำนวนแถวในข้อมูลทำนาย
num_rows = len(predictions)

# สร้างลูปเพื่อรวมข้อมูลเข้ากัน
for i in range(0, num_rows, 24):  # รวมข้อมูลทุก 24 แถว (รายชั่วโมง) เป็นรายวัน
    daily_data = predictions.iloc[i:i+24, :]
    
    # นับค่าเฉลี่ยขอข้อมูลในแต่ละวัน
    daily_average = daily_data['prediction_label'].mean()
    
    # ให้วันที่ในชุดข้อมูลเป็นวันแรก (index 0) ของแต่ละวัน
    date_of_day = daily_data['DATETIMEDATA'].iloc[0].date()
    
    # เพิ่มข้อมูลลงใน DataFrame
    daily_predictions = daily_predictions.append({'DATETIMEDATA': date_of_day, 'prediction_label': daily_average}, ignore_index=True)

# แสดงผลลัพธ์ข้อมูลทำนายรายวัน
print(daily_predictions)

# บันทึกข้อมูลทำนายรายวันเป็นไฟล์ CSV
daily_predictions.to_csv("PM2.5/data/Daily_predict.csv", index=False)
