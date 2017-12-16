from sqlToCypherConverter.Converter import Converter

if __name__ == "__main__":
    relationship_tables = {
        'voraussetzen': {
            'from': "Nachfolger",
            'to': "Vorgänger"
        },
        'hoeren': {
            'from': "MatrNr",
            'to': "VorlNr"
        }
    }
    tables_to_convert = {
        'studenten': "MatrNr",
        'professoren': "PersNr",
        'vorlesungen': "VorlNr",
    }
    print(Converter().convert("./resources/05 uni-daten.sql", tables_to_convert, relationship_tables))
