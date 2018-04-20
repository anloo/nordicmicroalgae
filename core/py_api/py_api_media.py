import json

def get_list(db):
    """ Fetches a list of media items from database """
    media_list = []
    cursor = db.cursor()
    cursor.execute(("select media_id, media_type, user_name, metadata_json "
                    "from taxa_media"))
    for (media_id, media_type, user_name, metadata_json) in cursor.fetchall():
        media_list.append({
            'media_id': media_id,
            'media_type': media_type,
            'user_name': user_name,
            'metadata': json.loads(metadata_json)
        })
    return media_list

def get_details(db, media_id):
    """ Fetches details about media from database """
    cursor = db.cursor()
    cursor.execute(("select media_id, media_type, user_name, metadata_json "
                    "from taxa_media where media_id = %(media_id)s"),
                    {'media_id': media_id})
    row = cursor.fetchone()
    if row is None:
        return None
    (media_id, media_type, user_name, metadata_json) = row
    return {
        'media_id': media_id,
        'media_type': media_type,
        'user_name': user_name,
        'metadata': json.loads(metadata_json)
    }
