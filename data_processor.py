from data_models import passenger, ship


def populate(soup):
    passengers = []
    sections = soup.find_all('div', {'class': 'sixteen columns'})
    tables = [section.table for section in sections if section.table is not None]

    for table in tables:
        people = [element for element in table.contents[2:] if element != '\n']
        class_passengers = []
        for person in people:
            last_name, first_name, age, boarded, survived = [identifier.text for identifier in person.contents]
            class_passengers.append(passenger.Passenger(last_name, first_name.replace('Â', ''), age, boarded, survived))
        passengers.append(class_passengers)

    titanic = ship.Ship('Titanic', passengers)

    return titanic
