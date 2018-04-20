import json

def get(db):
    """ Fetches system settings from database """
    settings = {}
    cursor = db.cursor()
    cursor.execute("selec settings_key, settings_value from system_settings")
    for (settings_key, settings_value) in cursor.fetchall():
        settings[settings_key] = json.loads(settings_value)
    return settings
