from infra.sqlalchemy.entities.sale import SaleEntity

class SaveRepository():
    
    def __init__(self, db) -> None:
        self.db = db

    def save_user(self, _entity: SaleEntity):
        self.db.add(_entity)
        self.db.commit()
        self.db.refresh(_entity)
        return _entity