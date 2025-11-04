from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()

    parser.read(filename)

    db = {}

    if section in parser:
        for key in parser[section]:
            db[key] = parser[section][key]

    else:
        raise Exception(
            f"Section {section} is not found in {filename}."
        )
    
    return db