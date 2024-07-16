from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate, PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import Ollama
from langchain.prompts.few_shot import FewShotPromptTemplate


class DecidArchAssistant:
    def __init__(self, system_template=None):
        self.model_name = "llama2"
        self.assistant_name = "DecidArchAssistant"
        self.uri_ollama = "http://192.168.1.206:11434"

        self.template = system_template or (
            f"You operate as {self.assistant_name}, a virtual assistant specialized in assisting with design decisions based on concerns provided by stakeholders."
        )

        # Examples for Few Shot Learning
        examples = [
            {
                "commento": "How should we address the scalability concern?",
                "answer": "Given the importance of performance and availability, it is recommended to use a distributed architecture to improve scalability."
            },
            {
                "commento": "What should we do about the recent system outage?",
                "answer": "We should review and enhance our security protocols to prevent future outages and ensure system reliability."
            },
            {
                "commento": "The owner is concerned about maintainability. How can we address this?",
                "answer": "To enhance maintainability, we should implement modular design principles and ensure comprehensive documentation."
            },
            {
                "commento": "The user wants improved usability. Any suggestions?",
                "answer": "For better usability, we should focus on a user-friendly interface and conduct usability testing to identify and resolve issues."
            }
        ]

        # Create example prompts in the format required by FewShotPromptTemplate
        example_prompt = PromptTemplate(
            input_variables=["commento", "answer"],
            template="Comment: {commento}\nAnswer: {answer}"
        )

        self.few_shot_template = FewShotPromptTemplate(
            examples=examples,
            example_prompt=example_prompt,
            suffix="Consider the following comments about a design decision and make suggestions based on stakeholder concerns:",
            input_variables=["commento"]
        )

        self.prompt = ChatPromptTemplate(
            messages=[
                MessagesPlaceholder("few_shot_examples"),
                HumanMessagePromptTemplate.from_template("{user_input}" + "\n" + "DecidArch: "),
            ]
        )

        self.llm = self._initialize_llm()
        self.conversation = LLMChain(
            prompt=self.prompt,
            llm=self.llm,
            verbose=True,
        )

    def _initialize_llm(self):
        # Initialize the language model here
        return Ollama(
            base_url=self.uri_ollama,
            model=self.model_name,
            system=self.template,
        )

    def provide_suggestions(self, comment):
        # Prepare few-shot examples
        formatted_example = self.few_shot_template.format(commento=comment)

        # Create a list of example dictionaries
        few_shot_examples = [{"role": "assistant", "content": formatted_example}]

        # Use the conversation chain to get a response
        response = self.conversation.run({"user_input": comment, "few_shot_examples": few_shot_examples})
        return response