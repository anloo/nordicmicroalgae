import json

def get_list(db):
    """ Fetches a list of taxa from database """
    taxon_list = []
    cursor = db.cursor()
    cursor.execute("select name, author, rank from taxa")
    for (name, author, rank) in cursor.fetchall():
        taxon_list.append({
            'name': name,
            'author': author,
            'rank': rank
        })
    return taxon_list

def get_details(db, taxon_name):
    """ Fetches details for a taxon from database """
    cursor = db.cursor()
    cursor.execute(("select name, author, rank "
                    "from taxa where name = %(taxon_name)s"),
                    {'taxon_name': taxon_name})
    row = cursor.fetchone()
    if row is None:
        return None
    (name, author, rank) = row
    return {
        'name': name,
        'author': author,
        'rank': rank
    }
