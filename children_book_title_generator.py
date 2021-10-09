import random

import pandas
from flask import Flask, render_template

SPREADSHEET_LINK = 'https://docs.google.com/spreadsheets/d/1hRFZct5hBlVuO-BElZHY3ZqSko6PFiIXk54t55A3R6Q'
SPREADSHEET_NAME = 'Kids book name generator'.replace(' ', '%20')

COLUMNS_OPTION1 = ['Start', 'Middle', 'End']
COLUMNS_OPTION2 = ['Start 2', 'End 2']
COLUMNS_OPTION3 = ['Start 3', 'Middle 3', 'End 3']
COLUMNS_OPTION4 = ['Start 4', 'Middle 4', 'End 4']

app = Flask(__name__)


def get_sheets_csv_link(sheets_link, sheets_name):
    return f'{sheets_link}/gviz/tq?tqx=out:csv&sheet={sheets_name}'


def generate_title():
    columns = random.choice([COLUMNS_OPTION1, COLUMNS_OPTION2, COLUMNS_OPTION3, COLUMNS_OPTION4])
    dataframe = pandas.read_csv(get_sheets_csv_link(SPREADSHEET_LINK, SPREADSHEET_NAME), usecols=columns)

    title = ''
    for column in dataframe:
        word = random.choice(dataframe[column].dropna().reset_index(drop=True))
        title += f'{word} '

    return title


@app.route("/")
def title_generator():
    generated_title = generate_title()
    return render_template('book_titles.html', generated_title=generated_title)
