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

def demo_turn_with_concern_card():
    """
    Demo di un turno in cui un giocatore pesca una concern card e l'AI suggerisce la migliore opzione di design.
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

    # Pesca della concern card
    concern_card = ConcernCard(1, "Security Breach", {"Security": -2, "Performance": -1})

    # Opzioni di design disponibili
    design_options = {
        "Implement Advanced Encryption": {"Security": +2, "Performance": -1, "Cost": -2},
        "Reduce Security Testing to Meet Deadlines": {"Security": -2, "Cost": +2, "Performance": +1},
        "Add Redundancy to Servers": {"Availability": +3, "Cost": -3, "Security": -1},
        "Use Open-Source Security Tools": {"Security": +1, "Cost": +1, "Maintainability": -1}
    }

    # Suggerimento AI per la concern card
    suggestion = assistant.extract_suggestion_chain(
        project_description=f"{project_card.name} - {project_card.purpose}",
        stakeholders=stakeholder_cards,
        current_design_decisions=decision_template,
        current_qa_scores=qa_scores,
        ongoing_events="None",  # Nessun evento attivo
        concern_card_description=concern_card.concern,
        design_options=design_options
    )

    # Output del suggerimento
    print(f"AI Suggestion for Security Breach: {suggestion}")


def demo_turn_with_event_card():
    """
    Demo in cui un evento modifica le decisioni passate, e l'AI suggerisce come rivedere tali decisioni.
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

    # Evento imprevisto: Server Outage Incident
    event_card = EventCard(
        title="Server Outage Incident",
        description="A critical server outage has occurred, causing system downtime.",
        consequence="The project must ensure high availability and implement server redundancy."
    )

    # Revisione delle decisioni passate in base all'evento
    review_suggestion = assistant.extract_review_suggestion_chain(
        project_description=f"{project_card.name} - {project_card.purpose}",
        stakeholders=stakeholder_cards,
        current_design_decisions=decision_template,
        current_qa_scores=qa_scores,
        ongoing_events=f"{event_card.title}: {event_card.description}. {event_card.consequence}"
    )

    # Output del suggerimento AI per la revisione
    print(f"AI Suggestion after Server Outage: {review_suggestion}")

# Esegui la demo del turno con concern card
demo_turn_with_concern_card()

# Esegui la demo del turno con event card
demo_turn_with_event_card()