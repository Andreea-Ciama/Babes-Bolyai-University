from ui import UI
from domain import Player
from repository import Repository

from services import Service


repository = Repository()
service = Service(repository)
console = UI(service)

console.start_command_ui()