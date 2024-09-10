from models import Player, ProjectCard, StakeholderCard, ConcernCard, EventCard
from decidarch_assistant import DecidArchAssistant
import configuration

def initialize_game():
    config = configuration.Configuration()
    assistant = DecidArchAssistant(config)

    # players
    players = [Player("John", "Doe"), Player("Rick", "Harrington")]
    print("Giocatori attivi:", [f"{player.first_name} {player.last_name}" for player in players])

    # progetto
    project_card = ProjectCard("New Web App", "Develop a scalable web application for e-commerce")

    # stakeholders
    stakeholder_cards = [
        StakeholderCard("Owner", "Ensure project success", {"Availability": 3, "Security": 2, "Cost": 1}),
        StakeholderCard("User", "Use the app effectively", {"Usability": 4, "Performance": 3, "Security": 1})
    ]

    return assistant, project_card, stakeholder_cards

def demo_1_security_breach_and_server_outage():
    assistant, project_card, stakeholder_cards = initialize_game()

    # Actual decision and QA attributes
    decision_template = [
        {"Security": -1, "Availability": 2},  # Migliora disponibilità a scapito della sicurezza
        {"Performance": 3, "Usability": -1}   # Aumento delle performance a scapito dell'usabilità
    ]

    qa_scores = {
        "Security": 1,
        "Performance": 2,
        "Usability": 3,
        "Availability": 3,
        "Cost": 0,
        "Maintainability": 0
    }

    # concern Card: security Breach
    concern_card = ConcernCard(1, "Security Breach", {"Security": -2, "Performance": -1})

    # Ai suggestion for concern card
    concern_suggestion = assistant.extract_suggestion_chain(
        project_description=f"{project_card.name} - {project_card.purpose}",
        stakeholders=stakeholder_cards,
        current_design_decisions=decision_template,
        current_qa_scores=qa_scores,
        ongoing_events="None",
        concern_card_description=concern_card.concern,
        design_options=concern_card.design_decisions
    )
    print(f"AI Suggestion for Security Breach: {concern_suggestion}")

    # Evento: Server Outage
    event_card = EventCard(
        title="Server Outage Incident",
        description="A critical server outage has occurred, causing system downtime.",
        consequence="The project must ensure high availability and implement server redundancy."
    )

    # Ai suggestion for event
    event_suggestion = assistant.extract_review_suggestion_chain(
        project_description=f"{project_card.name} - {project_card.purpose}",
        stakeholders=stakeholder_cards,
        current_design_decisions=decision_template,
        current_qa_scores=qa_scores,
        ongoing_events=f"{event_card.title}: {event_card.description}. {event_card.consequence}"
    )
    print(f"AI Suggestion for Server Outage: {event_suggestion}")

def demo_2_performance_degradation_and_cost_overrun():
    assistant, project_card, stakeholder_cards = initialize_game()

    # Actual decision and QA attributes
    decision_template = [
        {"Security": -1, "Availability": 2},  # Migliora disponibilità a scapito della sicurezza
        {"Performance": 3, "Usability": -1}   # Aumento delle performance a scapito dell'usabilità
    ]

    qa_scores = {
        "Security": 1,
        "Performance": 2,
        "Usability": 3,
        "Availability": 3,
        "Cost": 0,
        "Maintainability": 0
    }

    # concern Card: performance Degradation
    concern_card = ConcernCard(2, "Performance Degradation", {"Performance": -3, "Usability": -1})

    # Ai suggestion for concern
    concern_suggestion = assistant.extract_suggestion_chain(
        project_description=f"{project_card.name} - {project_card.purpose}",
        stakeholders=stakeholder_cards,
        current_design_decisions=decision_template,
        current_qa_scores=qa_scores,
        ongoing_events="None",
        concern_card_description=concern_card.concern,
        design_options=concern_card.design_decisions
    )
    print(f"AI Suggestion for Performance Degradation: {concern_suggestion}")

    # event: Cost Overrun
    event_card = EventCard(
        title="Cost Overrun",
        description="The project has exceeded the allocated budget due to unexpected infrastructure costs.",
        consequence="Need to revise design choices to reduce costs while maintaining project goals."
    )

    # Ai suggestion for event
    event_suggestion = assistant.extract_review_suggestion_chain(
        project_description=f"{project_card.name} - {project_card.purpose}",
        stakeholders=stakeholder_cards,
        current_design_decisions=decision_template,
        current_qa_scores=qa_scores,
        ongoing_events=f"{event_card.title}: {event_card.description}. {event_card.consequence}"
    )
    print(f"AI Suggestion for Cost Overrun: {event_suggestion}")

# demo 1
demo_1_security_breach_and_server_outage()
# demo 2
demo_2_performance_degradation_and_cost_overrun()
