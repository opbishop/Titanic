from data_models import passenger, ship

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
    genders = set()
    for table in tables:
        people = [element for element in table.contents[2:] if element != '\n']
        class_passengers = []
        for person in people:
            last_name, first_name, age, boarded, survived = [identifier.text for identifier in person.contents]
            first_name = first_name.replace('Â', '')
            p = passenger.Passenger(last_name, first_name, age, boarded, survived=='S')

            for k, v in titles.items():
                if first_name.split()[0] in v:
                    p.gender = k

            class_passengers.append(p)

        passengers.append(class_passengers)

    titanic = ship.Ship('Titanic', passengers)

    return titanic
