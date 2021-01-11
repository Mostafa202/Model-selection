import statsmodels.formula.api as sm
def backward(x,y,sl):
    for i in range(x.shape[1]):
        fitting=sm.OLS(y,x).fit()
        mx=max((fitting.pvalues).astype(float))
        print(mx)
        if mx>sl:
            
            for j in range(x.shape[1]):
                print("-------->",j)
                if fitting.pvalues[j].astype(float)==mx:
                    x=np.delete(x,j,1)
        else:
            break
    
    print(fitting.summary())
    return x