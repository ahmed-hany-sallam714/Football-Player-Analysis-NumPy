import numpy as np 
import pandas as pd 



'''
ملخص المشروع:
- قراءة بيانات لاعبي كرة القدم من ملف CSV (players_21.csv) باستخدام pandas.
- استخدام NumPy لتحويل بعض الأعمدة إلى مصفوفات وتحليل البيانات.
- حساب المتوسطات والإحصائيات الأساسية مثل متوسط العمر والقيمة السوقية.
- استخراج أفضل 10 لاعبين حسب معدل المهارات.
- مقارنة متوسط السرعة بين المهاجمين والمدافعين.
- حساب عدد اللاعبين لكل جنسية.
- حساب نسبة اللاعبين الذين أعمارهم أقل من 21 سنة.
- فلترة اللاعبين حسب شروط معينة (مثل القيمة والسرعة، أو المركز والعمر).
'''


# قراءة البيانات
data = pd.read_csv("players_21.csv")


# تحويل الأعمدة المهمة إلى NumPy arrays
age = data["age"].values
value = data["value_eur"].values
pace = data["pace"].values


# حساب عدد اللاعبين لكل جنسية باستخدام pandas
counts = data["nationality"].value_counts()
print("عدد اللاعبين لكل جنسية:")
print(counts)



print("\nعرض أول 5 صفوف من البيانات:")
print(data.head())



# حساب متوسط العمر ومتوسط القيمة السوقية باستخدام NumPy
print(f"\nمتوسط عمر اللاعبين هو: {round(np.mean(age))} سنة")
print(f"متوسط القيمة السوقية للاعبين هو: {round(np.mean(value))} يورو")




# حساب معدل المهارات لكل لاعب
shooting = data["shooting"].values
passing = data["passing"].values
dribbling = data["dribbling"].values
defending = data["defending"].values
physic = data["physic"].values

res = (pace + shooting + passing + dribbling + defending + physic) / 6

# استخراج أفضل 10 لاعبين حسب معدل المهارات
overall = np.argsort(res)[::-1][:10]
print("\nأفضل 10 لاعبين حسب معدل المهارات:")
print(data["long_name"][overall])




# مقارنة متوسط السرعة بين المهاجمين والمدافعين
attackers = 0
defenders = 0
n = 0
m = 0
for i in range(data.shape[0]):
    # التحقق إذا كان مركز اللاعب يحتوي على أحد المراكز الهجومية
    if any(pos in data["player_positions"][i] for pos in ["ST", "LW", "RW", "CF"]):
        n += 1
        attackers += pace[i]
    # التحقق إذا كان مركز اللاعب يحتوي على أحد المراكز الدفاعية
    elif any(pos in data["player_positions"][i] for pos in ["CB", "LB", "RB", "LWB", "RWB"]):
        m += 1
        defenders += pace[i]

print(f"\nمتوسط سرعة المهاجمين: {round(attackers / n)}")
print(f"متوسط سرعة المدافعين: {round(defenders / m)}")

# فلترة اللاعبين الذين قيمتهم أكبر من 80 وسرعتهم أكبر من 85
x = data["long_name"][(data["value_eur"] > 80000000) & (data["pace"] > 85)]
print("\nاللاعبين الذين قيمتهم السوقية أكبر من 80 مليون وسرعتهم أكبر من 85:")
print(x)

# حساب نسبة اللاعبين الذين أعمارهم أقل من 21 سنة باستخدام NumPy
under_21 = age < 21
percentage = round((np.sum(under_21) / len(age)) * 100)
print(f"\nنسبة اللاعبين الذين أعمارهم أقل من 21 سنة: {percentage} %")

# فلترة اللاعبين الذين يلعبون في مركز "ST" وعمرهم أقل من 25 سنة
y = (data["age"] < 25) & (data["player_positions"].str.contains("ST"))
percentage_st = round(np.sum(y) / data.shape[0] * 100)
print(f"\nنسبة اللاعبين في مركز 'ST' وأعمارهم أقل من 25 سنة: {percentage_st} %")

'''


✅ المهام اللي تعملها:
قراءة البيانات:

استخدم pandas لقراءة ملف players_21.csv.

تحويل البيانات:

حول الأعمدة اللي محتاجها إلى NumPy arrays.

تحليلات تستخدم فيها NumPy فقط:

حساب متوسط العمر، ومتوسط القيمة السوقية.

استخراج أفضل 10 لاعبين حسب معدل المهارات.

مقارنة متوسط السرعة بين اللاعبين حسب المركز (مثلاً: مهاجمين ضد مدافعين).

استخراج عدد اللاعبين لكل جنسية.

حساب نسبة اللاعبين اللي أعمارهم أقل من 21 سنة.

فلترة:

اللاعبين اللي قيمتهم أعلى من 80 وسرعتهم أكبر من 85.

اللاعبين اللي بيلعبوا في مركز "ST" وعمرهم تحت 25 سنة.



'''