from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chains import chains
from langchain.llms import Ollama


class DecidArchAssistant:
    def __init__(self, configuration, system_template=None):
        self.template = system_template or (
            "You operate as {self.assistant_name}, a virtual assistant specialized in assisting with design decisions "
            "based on concerns provided by stakeholders."
        )

        self.configuration = configuration

        # fare try catch
        self.llm = Ollama(
            base_url=configuration.uri_ollama,
            model=configuration.model_name,
            system=self.template,
        )

    def create_chain(self, template):
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

    def extract_info_trip(self, project_description, stakeholders, current_design_decisions, current_qa_scores, ongoing_events, concern_card_description, design_options):
        stakeholders_info = "\n".join([f"- {stakeholder.role}: {stakeholder.quality_attributes}" for stakeholder in stakeholders])
        info = self.extract_suggestion().run(
            project_description=project_description,
            stakeholders_info=stakeholders_info,
            current_design_decisions=current_design_decisions,
            current_qa_scores=current_qa_scores,
            ongoing_events=ongoing_events,
            concern_card_description=concern_card_description,
            design_options=design_options
        )
        return info