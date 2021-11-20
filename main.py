import db
from models import Products

def run():
    rice = Products("Rice", 1.25)
    db.Session.add(rice)
    print(rice.id)
    water = Products("Water", 0.3)
    db.Session.add(water)
    db.Session.commit()
    print(water.id)


if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)