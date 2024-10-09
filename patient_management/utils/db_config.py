import configparser

def load_db_config():
    config = configparser.ConfigParser()
    config.read('C:\\Users\\muniz\\OneDrive\\Documents\\MunMedSolutions\\Code\\patient_management\\config.ini')
    return config['database']
