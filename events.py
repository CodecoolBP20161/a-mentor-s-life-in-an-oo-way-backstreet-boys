import csv


class Events():
    def __init__(self, name, event_type, delta):
        super().__init__()
        self.name = name
        self.event_type = event_type
        self.delta = delta

    def open_csv(self):
        with open('events.csv') as f:
            read_file = csv.reader(f, delimiter='\t')
            events = []
            nevek = []
            j = 0
            for i in read_file:
                data = i[0]
                events.append(data.split(','))
                k = Events(events[j][0], events[j][1], events[j][2])
                j += 1
                nevek.append(k)
        return nevek

name = Events('név', 'típus', 'lol')
lista = name.open_csv()
print(lista[0].event_type)
