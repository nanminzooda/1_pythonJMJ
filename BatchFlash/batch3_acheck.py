bp_etoh = 351 # K
bp_h2o = 373 # K

# Rault's Law와 Antoine'sLaw를 혼합하여 a값(상대휘발도)를 구한다.
# 351K~ 373K에서의 a값을 구해서 평균값을 사용한다.

def antoine(a, b, c, t):
    return 10**(a-b/(t+c)) #Psat=10**(A-B / (T+C)); % kPa % T(K)

asum=0

for i in range(351,364+1):
    h2oPsat = antoine(5.08354, 1663.125, -45.622, i)
    etohPsat = antoine(5.24677, 1598.673, -46.424, i) # 에탄올의 Antoine Coefficient 구분

    a=etohPsat/h2oPsat
    asum+=a

for i in range(365,373+1):
    h2oPsat = antoine(5.08354, 1663.125, -45.622, i)
    etohPsat = antoine(4.92531, 1432.526, -61.819, i) # 에탄올의 Antoine Coefficient 구분

    a=etohPsat/h2oPsat
    asum+=a

print(asum/23)



