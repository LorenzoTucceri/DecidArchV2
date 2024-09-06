from models import Player, ProjectCard, StakeholderCard, ConcernCard, EventCard
from decidarch_assistant import DecidArchAssistant
import configuration

def demo_end_turn():
    config = configuration.Configuration()
    assistant = DecidArchAssistant(config)

    # players
    players = [Player("John", "Doe"), Player("Rick", "Harrington")]
    print("Actual players", [print(player.first_name, player.last_name) for player in players])

    # project's info
    project_card = ProjectCard("New Web App", "Develop a scalable web application for e-commerce")

    # stakeholders w priority
    stakeholder_cards = [
        StakeholderCard("Owner", "Ensure project success", {"Availability": 3, "Security": 2, "Cost": 1}),
        StakeholderCard("User", "Use the app effectively", {"Usability": 4, "Performance": 3, "Security": 1})
    ]

    # concern cards
    concern_cards = [
        ConcernCard(1, "Security Breach", {"Security": -2, "Performance": -1}),
        ConcernCard(2, "Scalability Issue", {"Availability": -1, "Performance": 2}),
        ConcernCard(3, "Cost Reduction", {"Cost": -2, "Maintainability": -1}),
    ]

    # actual decision and QA scores
    decision_template = [
        {"Security": -1, "Availability": 2},  # Decisione di mitigare la sicurezza ma migliorare la disponibilità
        {"Performance": 3, "Usability": -1}   # Aumento delle performance a scapito dell'usabilità
    ]

    # actual QA scores
    qa_scores = {
        "Security": 1,  # min security negative impact
        "Performance": 2,  # performance increment thanks to last decisions
        "Usability": 3,  # negative impact on usability
        "Availability": 3,  # higher disponibility thanks to last decisions
        "Cost": 0,  # no cost impact
        "Maintainability": 0  # neutral maintainability
    }

    # ongoing events with description
    ongoing_events = [
        EventCard("Budget Cut", "Reduction in available budget", "Resources are limited. Prioritize cost-saving measures."),
        EventCard("New Privacy Regulation", "New data privacy regulations require higher security measures", "Ensure compliance with strict privacy laws.")
    ]

    # current concern
    current_concern = concern_cards[0]  # Affrontiamo la preoccupazione "Security Breach"

    # demo of complex design options to discuss
    design_options = {
        "Implement Advanced Encryption": {"Security": +2, "Performance": -1, "Cost": -2},
        "Reduce Security Testing to Meet Deadlines": {"Security": -2, "Cost": +2, "Performance": +1},
        "Add Redundancy to Servers": {"Availability": +3, "Cost": -3, "Security": -1},
        "Use Open-Source Security Tools": {"Security": +1, "Cost": +1, "Maintainability": -1}
    }

    # formatting for prompt
    ongoing_events_desc = "\n".join([f"{event.title}: {event.description}. {event.consequence}" for event in ongoing_events])

    # suggestion given by assistant
    suggestion = assistant.extract_suggestion_chain(
        project_description=f"{project_card.name} - {project_card.purpose}",
        stakeholders=stakeholder_cards,
        current_design_decisions=decision_template,
        current_qa_scores=qa_scores,
        ongoing_events=ongoing_events_desc,  # ongoing event
        concern_card_description=current_concern.concern,
        design_options=design_options  # possible design decision
    )

    print(f"AI Suggestion: {suggestion}")

demo_end_turn()