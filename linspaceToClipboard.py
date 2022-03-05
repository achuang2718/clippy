import pandas as pd
import numpy as np

def linspace_array_to_clipboard():
    def user_input_endpoints():
        start_value = float(input('starting value: '))
        end_value = float(input('end value: '))
        n_points = int(input('number of points: '))
        return start_value, end_value, n_points
    start_value, end_value, n_points = user_input_endpoints()
    my_array = np.linspace(start_value, end_value, n_points)
    my_df = pd.DataFrame(my_array)
    my_df.to_clipboard(index=False, header=False)
    print(my_array)

if __name__ == "__main__":
    while True:
        linspace_array_to_clipboard()
        print('Copied to clipboard! \n \n')