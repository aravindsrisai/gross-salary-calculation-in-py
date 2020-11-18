# gross-salary-calculation-in-py
def GrossSalary(sal):
  if sal<1500:
    hra=sal*0.1
    da=sal*0.8
    gs=sal+hra+da
    return int(gs)
  else:
    hra=sal*0.3
    da=sal*0.9
    gs=sal+hra+da
    return int(gs)
sal=int(input())
r=GrossSalary(sal)
print(r)
