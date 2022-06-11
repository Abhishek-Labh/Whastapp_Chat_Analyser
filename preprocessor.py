import re
import pandas as pd


def preprocess(data):
    messages = re.findall('(\d+/\d+/\d+, \d+:\d+\d+ [A-Z]*) - (.*?): (.*)', data)

    # Convert list to a dataframe and name the columns

    df = pd.DataFrame(messages, columns=['date', 'name', 'message'])

    df['date'] = pd.to_datetime(df['date'], format="%m/%d/%y, %I:%M %p")

    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df