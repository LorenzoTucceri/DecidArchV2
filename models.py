class Player:
    """
    Represents a player in the system.

    Attributes:
        first_name (str): The first name of the player.
        last_name (str): The last name of the player.
    """
    def __init__(self, first_name, last_name):
        """
        Initializes a Player object.

        Args:
            first_name (str): The first name of the player.
            last_name (str): The last name of the player.
        """
        self.first_name = first_name
        self.last_name = last_name

class ProjectCard:
    """
    Represents a project card with a name and purpose.

    Attributes:
        name (str): The name of the project.
        purpose (str): The purpose of the project.
    """
    def __init__(self, name, purpose):
        """
        Initializes a ProjectCard object.

        Args:
            name (str): The name of the project.
            purpose (str): The purpose of the project.
        """
        self.name = name
        self.purpose = purpose

class StakeholderCard:
    """
    Represents a stakeholder card, describing a stakeholder's role, goal, and quality attributes.

    Attributes:
        role (str): The role of the stakeholder.
        goal (str): The goal of the stakeholder.
        quality_attributes (str): Quality attributes important to the stakeholder.
    """
    def __init__(self, role, goal, quality_attributes):
        """
        Initializes a StakeholderCard object.

        Args:
            role (str): The role of the stakeholder.
            goal (str): The goal of the stakeholder.
            quality_attributes (str): Quality attributes important to the stakeholder.
        """
        self.role = role
        self.goal = goal
        self.quality_attributes = quality_attributes

class ConcernCard:
    """
    Represents a concern card that tracks a design concern and associated design decisions.

    Attributes:
        card_id (int): Unique identifier for the concern card.
        concern (str): The specific concern to address.
        design_decisions (list): A list of design decisions related to the concern.
    """
    def __init__(self, card_id, concern, design_decisions):
        """
        Initializes a ConcernCard object.

        Args:
            card_id (int): Unique identifier for the concern card.
            concern (str): The specific concern to address.
            design_decisions (list): A list of design decisions related to the concern.
        """
        self.card_id = card_id
        self.concern = concern
        self.design_decisions = design_decisions

class EventCard:
    """
    Represents an event card containing information about a specific event and its consequences.

    Attributes:
        title (str): The title of the event.
        description (str): A detailed description of the event.
        consequence (str): The consequence or impact of the event.
    """
    def __init__(self, title, description, consequence):
        """
        Initializes an EventCard object.

        Args:
            title (str): The title of the event.
            description (str): A detailed description of the event.
            consequence (str): The consequence or impact of the event.
        """
        self.title = title
        self.description = description
        self.consequence = consequence