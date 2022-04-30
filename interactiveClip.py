import pandas as pd
import numpy as np
from numpy import linspace, arange

def copy(ans):
    if isinstance(ans, np.ndarray):
        my_df = pd.DataFrame(ans)
        my_df.to_clipboard(index=False, header=False)
        print(str(ans) + ' copied to clipboard.')
    else:
        print('Use a numpy ndarray.')
    return None

while True:
    my_input = input('>> ')
    try:
        if my_input == 'round':
            ans = ans.astype('int32')
        else:
            ans = eval(my_input)
        copy(ans)
    except Exception as e:
        print(e)
    if ans is not None:
        print('\nans = ')
        print(ans)