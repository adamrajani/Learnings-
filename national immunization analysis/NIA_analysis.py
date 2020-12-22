import pandas as pd

def proportion_of_education():
    df= pd.read_csv('NISPUF17.csv', index_col=0)
    num_of_vals= len(df['EDUC1'])
    vals= df['EDUC1'].value_counts().tolist()
    final={'less than high school': vals[3]/num_of_vals, "high school": vals[2]/num_of_vals,
        "more than high school but not college": vals[1]/num_of_vals,
        "college": vals[0]/num_of_vals}
    return final

print(proportion_of_education())

def average_influenza_doses():
    df= pd.read_csv('NISPUF17.csv', index_col=0)

    yea_bm = df[df.CBF_01==1].loc[:,['CBF_01','P_NUMFLU']].dropna()
    nah_bm = df[df.CBF_01==2].loc[:,['CBF_01','P_NUMFLU']].dropna()

    shots_yea= yea_bm['P_NUMFLU'].sum()
    final_a= shots_yea/len(yea_bm['P_NUMFLU'])

    shots_nah= nah_bm['P_NUMFLU'].sum()
    final_b= shots_nah/len(nah_bm['P_NUMFLU'])

    final=(final_a, final_b)
    return final

print(average_influenza_doses())

def average_influenza_doses1():
    import pandas as pd
    import numpy as np
    df = pd.read_csv("NISPUF17.csv", index_col=0)

    cbf_flu=df.loc[:,['CBF_01','P_NUMFLU']]


    cbf_flu1=cbf_flu[cbf_flu['CBF_01'] ==1].dropna()
    cbf_flu2=cbf_flu[cbf_flu['CBF_01'] ==2].dropna()

    flu1=cbf_flu1['P_NUMFLU'].values.copy()
    flu1[np.isnan(flu1)] = 0
    f1=np.sum(flu1)/len(flu1)

    flu2=cbf_flu2['P_NUMFLU'].values.copy()
    flu2[np.isnan(flu2)] = 0
    f2=np.sum(flu2)/len(flu2)

    aid =(f1,f2)
    return aid

print(average_influenza_doses1())

def chickenpox_by_sex1():
    import pandas as pd
    import numpy as np
    df = pd.read_csv("NISPUF17.csv", index_col=0)

    cpo_sex=df[df['P_NUMVRC'].gt(0) & df['HAD_CPOX'].lt(3)].loc[:,['HAD_CPOX','SEX']]
    #Male 1 Female 2
    cpo1_sex1=len(cpo_sex[(cpo_sex['HAD_CPOX']==1) & (cpo_sex['SEX']==1)])
    cpo1_sex2=len(cpo_sex[(cpo_sex['HAD_CPOX']==1) & (cpo_sex['SEX']==2)])
    cpo2_sex1=len(cpo_sex[(cpo_sex['HAD_CPOX']==2) & (cpo_sex['SEX']==1)])
    cpo2_sex2=len(cpo_sex[(cpo_sex['HAD_CPOX']==2) & (cpo_sex['SEX']==2)])

    cbs={"male":0,
        "female":0}
    cbs['male']=cpo1_sex1/cpo2_sex1
    cbs['female']=cpo1_sex2/cpo2_sex2
    return cbs
print(chickenpox_by_sex1())

def chickenpox_by_sex():
    df= pd.read_csv('NISPUF17.csv', index_col=0)

    x = len(df[(df.HAD_CPOX==1)&(df.P_NUMVRC >0)&(df.SEX==1)])
    y = len(df[(df.HAD_CPOX==2)&(df.P_NUMVRC >0)&(df.SEX==1)])
    a = len(df[(df.HAD_CPOX==1)&(df.P_NUMVRC >0)&(df.SEX==2)])
    b = len(df[(df.HAD_CPOX==2)&(df.P_NUMVRC >0)&(df.SEX==2)])

    num1=x/y
    num2=a/b
    final={'male': num1, 'female': num2}
    return final

print(chickenpox_by_sex())

def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd

    # this is the dataframe
    df= pd.read_csv('NISPUF17.csv', index_col=0)
    df=df[df['HAD_CPOX'].lt(3)].loc[:,['HAD_CPOX','P_NUMVRC']].dropna()
    df.columns=['had_chickenpox_column','num_chickenpox_vaccine_column']
    # here is some stub code to actually run the correlation
    corr, pval=stats.pearsonr(df["had_chickenpox_column"],df["num_chickenpox_vaccine_column"])

    # just return the correlation
    return corr

print(corr_chickenpox())
