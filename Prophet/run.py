import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt
from fbprophet.diagnostics import cross_validation
from fbprophet.diagnostics import performance_metrics
from model import preprocess
from model import train
from model import predict



def main():
    data_tomato_price = pd.read_csv("data/data_tomato_price.csv")
    # call preprocess function
    ts = preprocess(data_tomato_price)
    print("Training model...")
    # call train function
    model = train(ts)
    # I get a suitable dataframe that extends into the future a specified number
    #  of days using the helper method Prophet.make_future_dataframe
    ts_test = model.make_future_dataframe(periods=365, include_history=True)
    # call predict function
    
    preds = predict(model, ts_test)
    print("Price tomato prediction:")
    print(preds[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())
    # To see how the model fits existing data and what a forecast over 1 year looks like.
    # we can now study the fit of the model - in order to do so, we need to creat another df
    plot_pred = model.plot(preds)
    plt.legend(loc='best', fontsize=20)
    model.plot_components(preds, uncertainty=False)

    #Prophet Diagnostics:
    df_cv = cross_validation(model, initial='730 days', period='180 days', horizon = '365 days')
    print("Result using cross Validation:")
    print(df_cv.head())
    print("Diagnostics:  mae, mape...")
    df_p = performance_metrics(df_cv)
    print(df_p.head())


if __name__ == "__main__":
    main()
