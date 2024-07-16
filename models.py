class Player:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class ProjectCard:
    def __init__(self, name, purpose):
        self.name = name
        self.purpose = purpose

class StakeholderCard:
    def __init__(self, role, goal, quality_attributes):
        self.role = role
        self.goal = goal
        self.quality_attributes = quality_attributes

class ConcernCard:
    def __init__(self, card_id, concern, design_decisions):
        self.card_id = card_id
        self.concern = concern
        self.design_decisions = design_decisions

class EventCard:
    def __init__(self, title, description, consequence):
        self.title = title
        self.description = description
        self.consequence = consequence

# Example usage
player1 = Player("John", "Doe")
project_card = ProjectCard("New Project", "Develop a scalable web application")
owner_card = StakeholderCard("Owner", "Ensure project success", {"Availability": 3, "Security": 2, "Maintainability": 4})
user_card = StakeholderCard("User", "Use the application effectively", {"Usability": 5, "Security": 3, "Performance": 4})
concern_card = ConcernCard(1, "Scalability", {"Availability": -1, "Performance": 2})
event_card = EventCard("System Outage", "Unexpected system outage", "Review security protocols")