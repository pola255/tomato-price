"""
The idea behind the prophet package is to decompose time series data into the following three components:

trends: these are non-periodic and systematic trends in the data,
seasonal effects: these are modelled as daily or yearly periodicities in the data (optionally also hourly), and
holiday/one-off effects: these are effectively outliers.
"""

import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt
from fbprophet.diagnostics import cross_validation


def preprocess(df):
    """This function takes a dataframe and preprocesses it so it is
    ready for the training stage.

    The DataFrame contains the time axis and the target column.

    Return the training time serie: ts

    :param df: the dataset
    :type df: pd.DataFrame
    :return: ts
    """
    # I do a copy of DataFrame
    ts = df.copy()
    # I modified DataFrame to adapt to Prophet: the prophet package expects input as a
    # dataframe with the first column indicating time and the second
    # indicating the time series we wish to forecast
    ts = ts.rename(columns={'date': 'ds', 'tomato_price': 'y'})

    return ts


def train(ts):
    """Trains a new model on ts and returns it.

    :param ts: the processed training time serie
    :type ts: pd.DataFrame
    :return: a trained model
    """
    outliers = pd.to_datetime(['2015-01-16',
                               '2015-01-30',
                               '2015-02-13',
                               '2015-02-20',
                               '2015-02-27',
                               '2015-03-04',
                               '2015-03-27',
                               '2016-01-01',
                               '2016-01-15',
                               '2016-01-22',
                               '2016-01-29',
                               '2016-03-25',
                               '2017-03-17',
                               '2017-03-24',
                               '2018-02-02',
                               '2018-02-03',
                               '2018-02-16',
                               '2018-02-23',
                               '2018-03-16',
                               '2018-03-23',
                               '2018-03-30',
                               '2018-09-21',
                               '2018-09-28',
                               '2019-05-04',
                               '2019-05-07',
                               '2019-09-13',
                               '2019-09-20',
                               '2019-12-13',
                               '2019-12-20',
                               '2019-12-27'])

    outliers_days = pd.DataFrame({
        'holiday': 'Atypical',
        'ds': outliers
    })
    # Prophet model
    forecast_model = Prophet(growth='linear', weekly_seasonality=3,
                             daily_seasonality='auto',
                             yearly_seasonality=3, holidays=outliers_days)
    model = forecast_model.fit(ts)
    return model


def predict(model, ts_test):
    """This functions takes your trained model and returns predictions.

    :param model: the trained model
    :param ts_test: a processed test time serie
    :return: y_pred, your predictions
    """
    preds = model.predict(ts_test)
    return preds
