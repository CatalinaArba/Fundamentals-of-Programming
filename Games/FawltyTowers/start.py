from TextFileRepository import TextFileRepository
from TextFileRepository_rooms import TextFileRepositoryRoom
from service import Service
from UI import UI

reservations=TextFileRepository()
rooms=TextFileRepositoryRoom()

service=Service(rooms,reservations)
ui=UI(service)
UI.main(ui)