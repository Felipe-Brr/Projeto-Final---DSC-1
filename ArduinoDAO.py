import pandas as pd

class ArduinoDAO:

    def open(self):
        df = pd.read_csv("Arduino.csv")
        return df

    def save(self,df):

        df.to_csv("Arduino.csv", index=False)

    def create(self, Arduino):
        df = self.open()
        new_id = self.get_new_id(df)

        Arduino.id = new_id
        new_row = pd.DataFrame(data=[[
            Arduino.id, Arduino.temperatura, Arduino.presenca, Arduino.luminosidade
        ]],
            columns=df.columns)

        df = df.append(new_row)
        self.save(df)

    def get_new_id(self, df):

        if len(df) == 0:
            id = 1
        else:
            last = df.tail(1)
            id = last.id.values[0] + 1

        return id
