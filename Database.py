import json
import datetime

cast_file = "cast.json"
today = datetime.date.today().strftime('%Y-%m-%d')


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()
        elif isinstance(o, datetime.date):
            return o.isoformat()
        return super().default(o)


def create_cast_table():
    with open(cast_file, 'w') as file:
        json.dump([], file)


def get_all_casts():
    try:
        with open(cast_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        create_cast_table()
        with open(cast_file, 'r') as file:
            return json.load(file)


def _save_cast_to_database(casts):
    with open(cast_file, 'w') as file:
        json.dump(casts, file, cls=DateTimeEncoder)


def add_cast(benefit, mold, number):
    casts = get_all_casts()
    # check if today's date exists in the list
    date_exist = False
    for cast in casts:
        if datetime.datetime.fromisoformat(cast.get('Date')).date() == datetime.date.today():
            date_exist = True
            break
    # if today's date doesn't exist, add a new dict to the list
    if not date_exist:
        new_cast = {
            'Date': today,
            'Benefit package': {
                'NHI': {},
                'own': {}
            }
        }
        casts.append(new_cast)
        cast = new_cast
    else:
        cast = next(cast for cast in casts if datetime.datetime.fromisoformat(cast['Date']).date() == datetime.date.today())
    # check if the benefit package exists in the dict
    if benefit == 'NHI':
        payment = cast['Benefit package']['NHI']
    else:
        payment = cast['Benefit package']['own']
    # check if the mold exists in the dict
    if mold not in payment:
        payment[mold] = 0
    # add the number to the mold
    payment[mold] += number
    # write the updated list to the json file
    _save_cast_to_database(casts)
