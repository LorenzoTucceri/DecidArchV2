import time
from models import Player, ProjectCard, StakeholderCard, ConcernCard, EventCard
from decidarch_assistant import DecidArchAssistant

assistant = DecidArchAssistant()

# Setup del gioco
players = [Player("John", "Doe"), Player("Jane", "Smith")]
project_card = ProjectCard("New Project", "Develop a scalable web application")

owner_card = StakeholderCard("Owner", "Ensure project success", {"Availability": 3, "Security": 2, "Maintainability": 4})
user_card = StakeholderCard("User", "Use the application effectively", {"Usability": 5, "Security": 3, "Performance": 4})

concern_cards = [
    ConcernCard(1, "Scalability", {"Availability": -1, "Performance": 2}),
    ConcernCard(2, "Security Breach", {"Security": -2, "Performance": -1}),
    ConcernCard(3, "Usability Issue", {"Usability": 3}),
    ConcernCard(4, "Maintenance Overhead", {"Maintainability": -1}),
    ConcernCard(5, "Performance Optimization", {"Performance": 2, "Availability": 1}),
    ConcernCard(6, "Cost Reduction", {"Cost": -2, "Maintainability": -1}),
    ConcernCard(7, "Feature Expansion", {"Functionality": 3, "Usability": -1}),
    ConcernCard(8, "Compliance Requirement", {"Security": 3, "Maintainability": -1}),
    ConcernCard(9, "Technical Debt", {"Maintainability": -2, "Performance": -1}),
]

event_cards = [
    EventCard("System Outage", "Unexpected system outage", "Review security protocols"),
    EventCard("New Legislation", "Compliance with new regulations required", "Reassess compliance and security measures"),
    EventCard("Market Shift", "Change in market demands", "Adapt to new user needs and expectations"),
    EventCard("Technology Update", "New technology available", "Consider integrating new technology"),
    EventCard("Budget Cut", "Reduction in available budget", "Reevaluate project priorities and costs")
]

def calculate_score(decision_template, stakeholders):
    qa_scores = {attr: 0 for stakeholder in stakeholders for attr in stakeholder.quality_attributes.keys()}
    for decision in decision_template:
        for attr, impact in decision.items():
            qa_scores[attr] += impact

    if any(score < 0 for score in qa_scores.values()):
        return -1  # Immediate loss

    stakeholder_satisfaction = []
    for stakeholder in stakeholders:
        satisfaction = sum(max(0, qa_scores[attr] - priority) for attr, priority in stakeholder.quality_attributes.items())
        stakeholder_satisfaction.append(satisfaction)

    final_score = sum(stakeholder_satisfaction)
    return final_score

# Simulazione del gioco
start_time = time.time()
end_time = start_time + 30 * 60  # 30 minuti
decision_template = []
current_concern_index = 0

while time.time() < end_time and current_concern_index < len(concern_cards):
    for player in players:
        if time.time() >= end_time:
            break

        concern_card = concern_cards[current_concern_index]
        print(f"{player.first_name} {player.last_name}'s turn:")
        print(f"Concern: {concern_card.concern}")

        comment = f"How should we address the following concern: {concern_card.concern}?"
        suggestion = assistant.provide_suggestions(comment)
        print(f"Suggestion: {suggestion}")

        # Simulazione della decisione presa e registrazione
        decision_template.append(concern_card.design_decisions)
        current_concern_index += 1

        if current_concern_index >= len(concern_cards):
            break

# Calcolo del punteggio finale
final_score = calculate_score(decision_template, [owner_card, user_card])
print(f"Final Score: {final_score}")