import pickle

# ระบุที่อยู่ของไฟล์ .pkl
file_path = 'final_pm25_prediction_model.pkl'

# เปิดไฟล์ .pkl และโหลดโมเดล
with open(file_path, 'rb') as file:
    loaded_model = pickle.load(file)

# ทำในส่วนที่ต้องการใช้โมเดลที่โหลดมา
# ...
