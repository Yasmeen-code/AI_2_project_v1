import pandas as pd

# تحميل البيانات
file_path = "Indoor_Plant_Health_and_Growth_Factors.csv"
df = pd.read_csv(file_path)

# تعريف الشروط لكل نبات
conditions = {
    "Aloe Vera": {"temp_range": (18, 30), "humidity_range": (30, 55), "sun_keywords": ["sun", "direct", "bright"]},
    "Peace Lily": {"temp_range": (18, 27), "humidity_range": (50, 80), "sun_keywords": ["indirect", "filtered", "shade"]},
    "Snake Plant": {"temp_range": (15, 29), "humidity_range": (30, 60), "sun_keywords": ["low", "indirect", "shade"]},
    "Spider Plant": {"temp_range": (18, 30), "humidity_range": (40, 70), "sun_keywords": ["indirect", "filtered", "soft"]},
    "Fern": {"temp_range": (16, 24), "humidity_range": (60, 90), "sun_keywords": ["low", "filtered", "shade", "indirect"]}
}

# دالة لحساب مدى قرب الصف من كل نبات
def match_score(row, cond):
    temp = row["Room_Temperature_C"]
    hum = row["Humidity_%"]
    light = row["Sunlight_Exposure"].lower()

    # فرق الحرارة والرطوبة (كل ما كان أصغر، كان أقرب)
    temp_diff = abs((cond["temp_range"][0] + cond["temp_range"][1]) / 2 - temp)
    hum_diff = abs((cond["humidity_range"][0] + cond["humidity_range"][1]) / 2 - hum)

    # تحقق من الكلمات المفتاحية للإضاءة
    light_match = any(word in light for word in cond["sun_keywords"])
    light_score = 0 if light_match else 5  # عقوبة بسيطة لو مفيش تطابق

    # إجمالي النقاط (الأقل = الأفضل)
    return temp_diff + hum_diff / 3 + light_score

# دالة لتحديد النبات الأقرب
def assign_plant(row):
    best_plant = None
    best_score = float("inf")
    for plant, cond in conditions.items():
        score = match_score(row, cond)
        if score < best_score:
            best_score = score
            best_plant = plant
    # لو الفرق كبير جدًا، نخليها Unknown
    return best_plant if best_score < 15 else "Unknown"

# تطبيق الدالة على البيانات
df["Plant_Type"] = df.apply(assign_plant, axis=1)

# عرض النتائج
print("✅ أول 10 صفوف بعد التحسين:")
print(df[["Plant_ID", "Room_Temperature_C", "Humidity_%", "Sunlight_Exposure", "Plant_Type"]].head(10))

# إحصائيات بسيطة
print("\n📊 عدد Unknown بعد التحديث:", (df["Plant_Type"] == "Unknown").sum(), "من", len(df))

# حفظ الملف النهائي
df.to_csv("Updated_Indoor_Plant_Data_v2.csv", index=False)
print("\n💾 تم حفظ الملف الجديد باسم 'Updated_Indoor_Plant_Data_v2.csv'")
