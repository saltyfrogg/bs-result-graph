import matplotlib.pyplot as plt

from matplotlib import font_manager, rc

#폰트
font_path = "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

plt.rcParams['axes.unicode_minus'] = False


drinks = ['콜라', '오렌지', '핫식스']

#유무
ph_just = [3.15, 3.3, 3.52]
ph_bacteria = [2.6, 3.18, 3.32]
ph_bacteria_saliva100 = [6.088, 4.755, 4.801]

#농도별
ph_saliva_100 = [6.088, 4.755, 4.801]
ph_saliva_50 = [5.656, 4.259, 4.424]
ph_saliva_25 = [5.351, 4.029, 4.059]


#graph1
plt.figure(figsize=(10,6))
plt.plot(drinks, ph_just, marker='o', label='그냥 음료')
plt.plot(drinks, ph_bacteria, marker='o', label='세균 첨가')
plt.plot(drinks, ph_bacteria_saliva100, marker='o', label='세균 + 인공타액(100%)')
plt.title('음료별 pH 비교')
plt.xlabel('음료 종류')
plt.ylabel('pH')
plt.legend()
plt.grid(True)
plt.ylim(2, 7)
plt.savefig('ph_comparison_drinks.png')
plt.show()

#graph2
plt.figure(figsize=(10,6))
plt.plot(drinks, ph_saliva_100, marker='o', label='인공타액 100%')
plt.plot(drinks, ph_saliva_50, marker='o', label='인공타액 50%')
plt.plot(drinks, ph_saliva_25, marker='o', label='인공타액 25%')
plt.title('인공타액 농도별 pH 비교 (세균 포함)')
plt.xlabel('음료 종류')
plt.ylabel('pH')
plt.legend()
plt.grid(True)
plt.ylim(2, 7)
plt.savefig('ph_comparison_saliva_concentration.png')
plt.show()






