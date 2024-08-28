import time

import configuration
from decidarch_assistant import DecidArchAssistant
from models import Player, ProjectCard, StakeholderCard, ConcernCard, EventCard


class DecidArchGame:
    def __init__(self):
        self.configuration = configuration.Configuration()
        self.assistant = DecidArchAssistant(self.configuration)
        self.players = []
        self.project_card = None
        self.stakeholder_cards = []
        self.concern_cards = []
        self.event_cards = []
        self.decision_template = []
        self.current_concern_index = 0
        self.start_time = None
        self.end_time = None

    def setup_game(self):
        # giocatori
        num_players = int(input(f"Enter number of players (max {self.configuration.MAX_PLAYERS}): "))
        if num_players > self.configuration.MAX_PLAYERS:
            print(f"Number of players cannot exceed {self.configuration.MAX_PLAYERS}. Setting to {self.configuration.MAX_PLAYERS}.")
            num_players = self.configuration.MAX_PLAYERS
        elif num_players < self.configuration.MIN_PLAYERS:
            print(f"Number of players cannot exceed {self.configuration.MIN_PLAYERS}.")
            num_players = self.configuration.MIN_PLAYERS

        for _ in range(num_players):
            first_name = input("Enter player's first name: ")
            last_name = input("Enter player's last name: ")
            self.players.append(Player(first_name, last_name))

        # progetto
        project_name = input("Enter project name: ")
        project_purpose = input("Enter project purpose: ")
        self.project_card = ProjectCard(project_name, project_purpose)

        # stakeholder
        num_stakeholders = int(input(f"Enter number of stakeholders (max {self.configuration.MAX_STAKEHOLDERS}): "))
        if num_stakeholders > self.configuration.MAX_STAKEHOLDERS:
            print(f"Number of stakeholders cannot exceed {self.configuration.MAX_STAKEHOLDERS}. Setting to {self.configuration.MAX_STAKEHOLDERS}.")
            num_stakeholders = self.configuration.MAX_STAKEHOLDERS
        for _ in range(num_stakeholders):
            role = input("Enter stakeholder role: ")
            goal = input("Enter stakeholder goal: ")
            num_attributes = int(input(f"Enter number of quality attributes for {role}: "))
            quality_attributes = {}
            for _ in range(num_attributes):
                attr = input("Enter quality attribute: ")
                priority = int(input(f"Enter priority for {attr} (1-5): "))
                quality_attributes[attr] = priority
            self.stakeholder_cards.append(StakeholderCard(role, goal, quality_attributes))

        # concern cards
        num_concerns = int(input(f"Enter number of concern cards (max {self.configuration.MAX_CONCERNS}): "))
        if num_concerns > self.configuration.MAX_CONCERNS:
            print(f"Number of concern cards cannot exceed {self.configuration.MAX_CONCERNS}. Setting to {self.configuration.MAX_CONCERNS}.")
            num_concerns = self.configuration.MAX_CONCERNS
        for i in range(num_concerns):
            concern = input(f"Enter concern for card {i+1}: ")
            num_decisions = int(input(f"Enter number of design decisions for concern {concern}: "))
            design_decisions = {}
            for _ in range(num_decisions):
                attr = input("Enter design decision attribute: ")
                impact = int(input(f"Enter impact for {attr} (+/- value): "))
                design_decisions[attr] = impact
            self.concern_cards.append(ConcernCard(i+1, concern, design_decisions))

        # event cards
        num_events = int(input(f"Enter number of event cards (max {self.configuration.MAX_EVENTS}): "))
        if num_events > self.configuration.MAX_EVENTS:
            print(f"Number of event cards cannot exceed {self.configuration.MAX_EVENTS}. Setting to {self.configuration.MAX_EVENTS}.")
            num_events = self.configuration.MAX_EVENTS
        for _ in range(num_events):
            title = input("Enter event title: ")
            description = input("Enter event description: ")
            consequence = input("Enter event consequence: ")
            self.event_cards.append(EventCard(title, description, consequence))

    def calculate_score(self):
        qa_scores = {attr: 0 for stakeholder in self.stakeholder_cards for attr in stakeholder.quality_attributes.keys()}
        for decision in self.decision_template:
            for attr, impact in decision.items():
                qa_scores[attr] += impact

        if any(score < 0 for score in qa_scores.values()):
            return -1  # Immediate loss

        stakeholder_satisfaction = []
        for stakeholder in self.stakeholder_cards:
            satisfaction = sum(max(0, qa_scores[attr] - priority) for attr, priority in stakeholder.quality_attributes.items())
            stakeholder_satisfaction.append(satisfaction)

        final_score = sum(stakeholder_satisfaction)
        return final_score

    def play_game(self):
        self.setup_game()
        self.start_time = time.time()
        self.end_time = self.start_time + 30 * 60  # 30 minuti

        while time.time() < self.end_time and self.current_concern_index < len(self.concern_cards):
            for player in self.players:
                if time.time() >= self.end_time:
                    break

                concern_card = self.concern_cards[self.current_concern_index]
                print(f"{player.first_name} {player.last_name}'s turn:")
                print(f"Concern: {concern_card.concern}")

                # stakeholders_info = "\n".join([f"- {stakeholder.role}: {stakeholder.quality_attributes}" for stakeholder in self.stakeholder_cards])
                current_design_decisions = ", ".join([f"{k}: {v}" for decision in self.decision_template for k, v in decision.items()])
                current_qa_scores = ", ".join([f"{k}: {v}" for k, v in self.calculate_qa_scores().items()])
                ongoing_events = ", ".join([f"{event.title}: {event.description}" for event in self.event_cards])

                suggestion = self.assistant.extract_info_trip(
                    project_description=f"{self.project_card.name} - {self.project_card.purpose}",
                    stakeholders=self.stakeholder_cards,
                    current_design_decisions=current_design_decisions,
                    current_qa_scores=current_qa_scores,
                    ongoing_events=ongoing_events,
                    concern_card_description=concern_card.concern,
                    design_options=concern_card.design_decisions
                )
                print(f"Suggestion: {suggestion}")

                # Simulazione della decisione presa e registrazione
                self.decision_template.append(concern_card.design_decisions)
                self.current_concern_index += 1

                if self.current_concern_index >= len(self.concern_cards):
                    break

        # punteggio finale
        final_score = self.calculate_score()
        print(f"Final Score: {final_score}")

    def calculate_qa_scores(self):
        qa_scores = {attr: 0 for stakeholder in self.stakeholder_cards for attr in stakeholder.quality_attributes.keys()}
        for decision in self.decision_template:
            for attr, impact in decision.items():
                qa_scores[attr] += impact
        return qa_scores


if __name__ == "__main__":
    game = DecidArchGame()
    game.play_game()