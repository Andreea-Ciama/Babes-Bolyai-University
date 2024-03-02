from services import Service
class UI:

    def __init__(self, service):
        self.service = service


    def display_players(self):
        self.service._repository.players.sort(reverse=True, key=lambda x: x.strength)
        for player in self.service._repository.players:
            print(str(player))

    def play_qualifications(self, players):
        """
        With this function we play the qualifications
        :param players: all the players from the qualifications
        :return: it doesn't return anything
        """
        winner_list = []
        length = len(players )//2
        while length != 0:
            made_pairs = self.service.choose_random_the_pairs(players)
            for player in made_pairs:
                print(str(player))
            winner = int(input("Choose the winner! Type 1 for the first player or 2 for the second "))
            length = length - 1
            if winner == 1:
                self.service._repository.update_players_strength(made_pairs[0].player_id,str(int(made_pairs[0].strength)+1))
                winner_list.append(made_pairs[0])
            else:
                winner_list.append(made_pairs[1])
                self.service._repository.update_players_strength(made_pairs[0].player_id,str(int(made_pairs[1].strength)+1))



    def start_qualifications(self):
        print("Qualifications")
        new_players = self.service.qualifications()
        self.play_qualifications(new_players)

    def start_tournament(self):
        if len(self.service._repository.players) == 0:
            print("There are no players!")
        if not self.service.check_qualifications():
            self.start_qualifications()

    def menu(self):
        print("1.Display all the players")
        print("2.play the qualifications")
        print("0.Exit")

    def start_command_ui(self):
        """
        It is the start function
        :return:  it doesn't return anything, but call other functions if the command given by the user is not invalid
        """

        self.menu()
        command_dict = {'1': self.display_players, '2': self.start_tournament}
        are_we_done_yet = False
        while not are_we_done_yet:
            command = input('\nWhat would you like to do? Enter command: \n')
            if command in command_dict:
                try:
                    command_dict[command]()
                except ValueError as ve:
                    print(ve)
            elif command == '0':
                print("Goodbye!")
                are_we_done_yet = True
            else:
                print("Invalid command!")
