from models import Player, ProjectCard, StakeholderCard, ConcernCard, EventCard
from decidarch_assistant import DecidArchAssistant
import configuration

def initialize_game():
    """
    Funzione di inizializzazione del gioco: configurazione dell'assistente, dei giocatori, del progetto e degli stakeholder.
    """
    config = configuration.Configuration()
    assistant = DecidArchAssistant(config)

    # Giocatori
    players = [Player("John", "Doe"), Player("Rick", "Harrington")]
    print("Giocatori attivi:", [f"{player.first_name} {player.last_name}" for player in players])

    # Progetto
    project_card = ProjectCard("New Web App", "Develop a scalable web application for e-commerce")

    # Stakeholders
    stakeholder_cards = [
        StakeholderCard("Owner", "Ensure project success", {"Availability": 3, "Security": 2, "Cost": 1}),
        StakeholderCard("User", "Use the app effectively", {"Usability": 4, "Performance": 3, "Security": 1})
    ]

    return assistant, project_card, stakeholder_cards

def demo_1_security_breach_and_server_outage():
    """
    Demo 1: Affrontare sia una concern card (Security Breach) che un evento (Server Outage).
    """
    # Inizializzazione
    assistant, project_card, stakeholder_cards = initialize_game()

    # Decisioni attuali e punteggi QA
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

    # Concern Card: Security Breach
    concern_card = ConcernCard(1, "Security Breach", {"Security": -2, "Performance": -1})

    # Evento: Server Outage
    event_card = EventCard(
        title="Server Outage Incident",
        description="A critical server outage has occurred, causing system downtime.",
        consequence="The project must ensure high availability and implement server redundancy."
    )

    # Opzioni di design disponibili
    design_options = {
        "Implement Advanced Encryption": {"Security": +2, "Performance": -1, "Cost": -2},
        "Reduce Security Testing to Meet Deadlines": {"Security": -2, "Cost": +2, "Performance": +1},
        "Add Redundancy to Servers": {"Availability": +3, "Cost": -3, "Security": -1},
        "Use Open-Source Security Tools": {"Security": +1, "Cost": +1, "Maintainability": -1}
    }

    # Suggerimento AI per la concern card e l'evento
    suggestion = assistant.extract_suggestion_chain(
        project_description=f"{project_card.name} - {project_card.purpose}",
        stakeholders=stakeholder_cards,
        current_design_decisions=decision_template,
        current_qa_scores=qa_scores,
        ongoing_events=f"{event_card.title}: {event_card.description}. {event_card.consequence}",
        concern_card_description=concern_card.concern,
        design_options=design_options
    )

    # Output del suggerimento
    print(f"AI Suggestion for Security Breach and Server Outage: {suggestion}")

def demo_2_performance_degradation_and_cost_overrun():
    """
    Demo 2: Affrontare sia una concern card (Performance Degradation) che un evento (Cost Overrun).
    """
    # Inizializzazione
    assistant, project_card, stakeholder_cards = initialize_game()

    # Decisioni attuali e punteggi QA
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

    # Concern Card: Performance Degradation
    concern_card = ConcernCard(2, "Performance Degradation", {"Performance": -3, "Usability": -1})

    # Evento: Cost Overrun
    event_card = EventCard(
        title="Cost Overrun",
        description="The project has exceeded the allocated budget due to unexpected infrastructure costs.",
        consequence="Need to revise design choices to reduce costs while maintaining project goals."
    )

    # Opzioni di design disponibili
    design_options = {
        "Optimize Database Queries": {"Performance": +3, "Cost": -2, "Usability": 0},
        "Reduce Testing to Save Costs": {"Security": -1, "Cost": +3, "Maintainability": -2},
        "Implement Cloud Auto-scaling": {"Performance": +2, "Availability": +2, "Cost": -3},
        "Use Open-Source Tools": {"Cost": +2, "Maintainability": -1, "Performance": +1}
    }

    # Suggerimento AI per la concern card e l'evento
    suggestion = assistant.extract_suggestion_chain(
        project_description=f"{project_card.name} - {project_card.purpose}",
        stakeholders=stakeholder_cards,
        current_design_decisions=decision_template,
        current_qa_scores=qa_scores,
        ongoing_events=f"{event_card.title}: {event_card.description}. {event_card.consequence}",
        concern_card_description=concern_card.concern
    )

    # Output del suggerimento
    print(f"AI Suggestion for Performance Degradation and Cost Overrun: {suggestion}")

# Esegui la demo 1
demo_1_security_breach_and_server_outage()
# Esegui la demo 2
demo_2_performance_degradation_and_cost_overrun()
