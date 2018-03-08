from data_models import passenger, ship

import pandas as pd
from pandas import DataFrame

titles = {
    'Male': ['Master', 'Mr', 'Don.', 'Señor', 'MrSark', 'Sir', 'Major', 'Father', 'Colonel', 'Captain'],
    'Female': ['Lucy', 'Miss', 'Doña', 'Señora', 'Mrs', 'Ms', 'Mme.', 'Mlle']
}
# {'Master', 'Lucy', 'Mr', 'Dr', 'Reverend', 'Captain', 'Miss', 'Don.', 'Doña', 'Señora', 'Señor', 'MrSark', 'Mrs',
# 'Sir', 'Major', 'Ms', 'Father', 'Colonel', 'Mme.', 'Mlle'}
# I'm being optimistic and assuming dr, reverend could be either...

def populate(soup):
    passengers = []
    sections = soup.find_all('div', {'class': 'sixteen columns'})
    tables = [section.table for section in sections if section.table is not None]
    for table in tables:
        people = [element for element in table.contents[2:] if element != '\n']
        class_passengers = []
        for person in people:
            last_name, first_name, age, boarded, survived = [identifier.text for identifier in person.contents]
            first_name = first_name.replace('Â', '')
            try:
                p = passenger.Passenger(last_name, first_name, int(age), boarded, survived=='S')

                for k, v in titles.items():
                    if first_name.split()[0] in v:
                        p.gender = k

                class_passengers.append(p)
            # throws ValueError on casting age to int (data quality == poor)
            except ValueError:
                pass


        passengers.append(class_passengers)

    titanic = ship.Ship('Titanic', passengers)

    return titanic

def analyse(dataset):
    df = DataFrame()
    for data in dataset:
        df1 = DataFrame([person.get_values() for person in data], columns=['Surname', 'First name', 'Age', 'Boarded', 'Survived', 'Gender'])
        df1['Class'] = [dataset.index(data)+1]*len(data)
        df = pd.concat([df, df1], ignore_index=True)

    survived_by_class(df)

def survived_by_class(df):
    df = pd.crosstab(df.Class, df.Survived).apply(lambda r: r/r.sum(), axis=1)
    print(df)
