import json

def mix(m1,t1,m2,t2):
    if m1<=0 or m2<=0:
        raise ValueError('Positive flows required.')
    return {'basis':'Constant-Cp hand calculation; not DWSIM output.','outlet_kg_h':m1+m2,'temperature_C':(m1*t1+m2*t2)/(m1+m2)}

if __name__=='__main__':
    print(json.dumps(mix(1000,20,500,60),indent=2))
