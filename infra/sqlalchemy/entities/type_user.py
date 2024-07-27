from enum import Enum, unique

@unique
class TypeUserEnum(Enum):
    
    ADMIN = 1, 'Admin'
    CLIENT = 2, 'Client'
