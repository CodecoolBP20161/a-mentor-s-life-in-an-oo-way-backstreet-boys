import csv


class Events():
    def __init__(self, name, event_type, delta):
        super().__init__()
        # events = Events("fd", "fd", 3)
        # lista = events.open_csv()
        # m = lista[0].name
        self.name = name
        self.event_type = event_type
        self.delta = delta
        self.knowledge = []
        self.timewaster = []
        self.energizer = []

    def open_csv(self):
        self.events = []
        from mindsharpener import Mindsharpener
        from energizer import Energizer
        from timewaster import Timewaster
        with open('events.csv') as f:
            read_file = csv.reader(f, delimiter='\t')
            # events = []
            # nevek = []
            j = 0
            for i in read_file:
                data = i[0]
                events.append(data.split(','))
                # k = Events(events[j][0], events[j][1], events[j][2])
                if events[j][1] == "knowledge":
                    k = Mindsharpener(events[j][0], events[j][1], events[j][2])
                    self.knowledge.append(k)
                elif events[j][1] == "energizer":
                    k = Energizer(events[j][0], events[j][1], events[j][2])
                    self.energizer.append(k)
                elif events[j][1] == "timewaster":
                    k = Timewaster(events[j][0], events[j][1], events[j][2])
                    self.timewaster.append(k)
                j += 1

        return self.events
