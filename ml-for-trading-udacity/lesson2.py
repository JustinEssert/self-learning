import pandas as pd
import matplotlib.pyplot as plt

def print_csv(filename):
    df = pd.read_csv(filename)
    print(df)

def plot_csv(filename):
    df = pd.read_csv(filename)
    df['Close'].plot()
    plt.show()


if __name__ == "__main__":
    plot_csv('AAPL.csv')
    print('done')
