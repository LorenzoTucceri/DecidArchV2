from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain import chains
from langchain.llms import Ollama


class DecidArchAssistant:
    """
    Virtual assistant specialized in assisting with architectural design decisions based on stakeholder concerns, project state, and ongoing events.

    Attributes:
        configuration (object): Configuration object containing settings such as URI and model name for the LLM.
        system_template (str, optional): Custom system message template for the assistant. Defaults to a predefined template.
        llm (Ollama): Language model instance used to generate suggestions based on provided data.

    Methods:
        __init__(configuration, system_template=None): Initializes the assistant with configuration and an optional system template.
        create_chain(template): Creates and returns a language model chain based on a provided template.
        extract_suggestion(): Generates a chain with a predefined template for suggesting the best design decision.
        extract_suggestion_chain(project_description, stakeholders, current_design_decisions, current_qa_scores, ongoing_events, concern_card_description, design_options):
            Generates a suggestion for the best design decision based on various inputs.
    """

    def __init__(self, configuration, system_template=None):
        """
        Initializes the DecidArchAssistant object with the provided configuration and an optional system template.

        Args:
            configuration (object): Configuration containing settings for the assistant, including URI and model name for the LLM.
            system_template (str, optional): Custom template for the system message. Defaults to a predefined message that describes the assistant's role.
        """
        self.template = system_template or (
            "You operate as {self.assistant_name}, a virtual assistant specialized in assisting with design decisions "
            "based on concerns provided by stakeholders."
        )

        self.configuration = configuration

        # initializing an llm using the Ollama API with the provided configuration.
        self.llm = Ollama(
            base_url=self.configuration.uri_ollama,
            model=self.configuration.model_name,
            system=self.template,
        )

    def create_chain(self, template):
        """
        Creates a language model chain using the provided template and the initialized LLM.

        Args:
            template (str): The prompt template to be used for generating responses.

        Returns:
            chains.LLMChain: A chain object that links the prompt template with the language model.
        """
        prompt_template = ChatPromptTemplate(
            messages=[
                HumanMessagePromptTemplate.from_template(template)
            ]
        )

        chain = chains.LLMChain(
            prompt=prompt_template,
            llm=self.llm,
            verbose=1,
        )
        return chain

    def extract_suggestion(self):
        """
        Creates a chain with a predefined prompt for suggesting the best design option based on stakeholder concerns, project state, and ongoing events.

        The template used provides information about the project description, stakeholders' quality attribute priorities, current game state, concern card, and possible design options.

        Returns:
            chains.LLMChain: A chain object that will be used to generate the design suggestion.
        """
        template = """
        You are an AI assistant helping a team of software architects playing the game DecidArch. Your task is to suggest
        the best design option for a given concern card, taking into account the stakeholders' quality attribute priorities
        and any ongoing project events. Here's the information you'll need:

        Project Description:
        - {project_description}

        Stakeholders and their Quality Attribute Priorities:
        {stakeholders_info}

        Current Game State:
        - Current Design Decisions: {current_design_decisions}
        - Current QA-Scores: {current_qa_scores}
        - Ongoing Events: {ongoing_events}

        Concern Card Description:
        - {concern_card_description}

        Possible Design Options:
        - {design_options}

        Based on this information, suggest the best design option that satisfies the stakeholders' priorities and 
        considers any ongoing events. Provide a rationale for your suggestion.
        """

        return self.create_chain(template)

    def extract_suggestion_chain(self, project_description, stakeholders, current_design_decisions, current_qa_scores, ongoing_events, concern_card_description, design_options):
        """
        Generates a design suggestion based on project description, stakeholder information, design decisions, QA scores, ongoing events, and concern card.

        Args:
            project_description (str): A description of the project.
            stakeholders (list): A list of stakeholders, where each stakeholder contains a role and quality attributes.
            current_design_decisions (str): A description of the current design decisions in place.
            current_qa_scores (str): The current quality attribute scores.
            ongoing_events (str): A list of ongoing events in the project.
            concern_card_description (str): The description of the concern card.
            design_options (str): A list of possible design options to choose from.

        Returns:
            str: The assistant's suggestion for the best design option, including a rationale.
        """
        stakeholders_info = "\n".join([f"- {stakeholder.role}: {stakeholder.quality_attributes}" for stakeholder in stakeholders])
        suggestion = self.extract_suggestion().run(
            project_description=project_description,
            stakeholders_info=stakeholders_info,
            current_design_decisions=current_design_decisions,
            current_qa_scores=current_qa_scores,
            ongoing_events=ongoing_events,
            concern_card_description=concern_card_description,
            design_options=design_options
        )
        return suggestion