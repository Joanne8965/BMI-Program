height = input('請輸入身高(cm): ')
weight = input('請輸入體重(kg): ')

height = int(height)
weight = int(weight)

height = height / 100
bmi = weight / height / height

if bmi < 18.5:
    print('你的bmi值為', bmi,'體重過輕' )
elif bmi >= 18.5 and bmi < 24:
    print('你的bmi值為', bmi,'正常範圍' )
elif bmi >= 24 and bmi < 27:
    print('你的bmi值為', bmi,'稍重' )
elif bmi >= 35:
    print('你的bmi值為', bmi,'重度肥胖' )



