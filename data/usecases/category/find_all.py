from typing import List
from data.repositories.category.find_all import FindAllRepository
from domain.category import CategoryModel

class FindAllUseCase():

    def find_all(self) -> List[CategoryModel]:
        
        return FindAllRepository().get_categories()