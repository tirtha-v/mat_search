
from mp_api.client import MPRester


def get_mat(api_key, prop, min_value, max_value, num):
    '''This function will get elements with the desirable properties'''
    with MPRester(api_key=api_key) as mpr:
        k = mpr.materials.summary.search(**{prop:[min_value, max_value]})
    output=[]
    for i in range(int(num)):
        output.append(str(k[i].composition))
    return output

def get_summary(api_key, prop, min_value, max_value, num):
    with MPRester(api_key=api_key) as mpr:
        k = mpr.materials.summary.search(**{prop:[min_value,max_value]})
    return k
