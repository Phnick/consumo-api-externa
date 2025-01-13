from infra.api_consumer import ApiConsumer
from data.usecase.starships_list_colector import StarshipsColector
from data.usecase.starships_information_colector import StarshipInformationColector


api_consumer = ApiConsumer()
starship_colector = StarshipsColector(api_consumer)
starship_information = StarshipInformationColector(api_consumer)

starship = starship_information.find_starship(page=3, limit=1, starship_id=75)
starship2 = starship_colector.list(page=8, limit=3)

print(f'lista {starship}')
print()
print(f'Lista 2 {starship2}')
