import os
from groq import Groq

class LLMPEv01:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_name": (["llama3-70b-8192", "llama3-8b-8192", "mixtral-8x7b-32768", "gemma-7b-it"],),
                "image_prompt": ("STRING", {
                    "multiline": True,
                    "default": "[Insert image description here]"
                }),
            },
            "optional": {
                "api_environment_variable": ("STRING", {
                    "multiline": False,
                    "default": "[Name of the environment variable containing Groq API key]"
                }),
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": "[Insert Groq API key]"
                }),
                "llm_prompt": ("STRING", {
                    "multiline": True,
                    "default": """You are describing an image to a blind person. Be objective yet detailed.
You must always follow all these Rules:

##RULES##
Rule 1: Respond only with the [Output].

Rule 2: The [Output] must match the style of the provided examples.

Rule 3: The [Output] must only use visual adjectives to enhance the input [input].
]
Rule 4: If the [input] mentions some specific style (photography, drawing, anime, etc) the [output] MUST begin specifying the the style provided.

Rule 5: If the [input] mentions some specific view angle (front view, side view, profile, wide angle, etc) the [output] must also define the view angle, being adherent to the input.

Rule 6: The [Output] must be between 200 and 300 characters in length.

Rule 7: If the [input] contais expressions following the format "([text] : [float number])" the output must emphasize the information inside the brackets acordingly. the string "(at night :1.5)" means that the expression "at night" is very relevant and a bigger number of words related to it must be very present in the [output]. The expression "(at night :0.6)" means that "at night" is not very relevant and a smaller number of words related to it must be present in the [output].

##END RULES##

Considering the rules, process the [input] following this algorithm:

##ALGORITHM##

[Text] = [Input] translated to English.
if ([Input] is already in English) {[Text] = [Input]}
[Output] = AddDetails([Text])

##END ALGORITHM##

##EXAMPLES##

[Input]: A big yellow house
[Output]: A grand, two-story yellow house stands proudly, its walls bathed in sunlight. The roof is a classic red, contrasting with white-framed windows that gleam brightly. A large, inviting porch spans the front, adorned with potted plants. Surrounding the house is a lush, manicured lawn dotted with vibrant flowers and towering trees.

[Input]: A cyberpunk city
[Output]: A sprawling cyberpunk cityscape glows under a neon-lit sky. Skyscrapers with futuristic designs tower overhead, their facades adorned with holographic advertisements. Elevated walkways crisscross the scene, bustling with people in high-tech attire. Below, streets are filled with sleek vehicles and vibrant market stalls, while the air hums with the energy of advanced technology.

[Input]: A beautiful woman with green eyes wearing a red dress
[Output]: A beautiful woman stands gracefully, her green eyes sparkling with depth and intrigue. She wears a stunning red dress that accentuates her elegant silhouette, the fabric shimmering slightly as it catches the light. Her hair cascades in soft waves, framing her face perfectly, and a confident, warm smile graces her lips, adding to her captivating presence.

##END EXAMPLES##

[input]:"""
                }),
                "llm_prompt_from_file": ("STRING", {
                    "multiline": False,
                    "default": "[Insert path to file containing LLM Prompt. Example: c:\\prompt.txt]"
                }),
            },
        }

    RETURN_TYPES = ("STRING",)

    FUNCTION = "process_text"

    # OUTPUT_NODE = False

    CATEGORY = "LLMPE"

    def process_text(self, model_name, image_prompt, api_environment_variable="[Name of the environment variable containing Groq API key]",
                     api_key="[Insert Groq API key]", llm_prompt="[Insert prompt template here]", llm_prompt_from_file="[Insert path to file containing LLM Prompt. Example: c:\\prompt.txt]"):
        
        # Determinar a chave da API
        if api_environment_variable != "[Name of the environment variable containing Groq API key]":
            api_key = os.getenv(api_environment_variable, None)
            if api_key is None:
                raise Exception(f"Invalid environment variable: {api_environment_variable}")
        elif api_key == "[Insert Groq API key]":
            raise Exception("API key is not provided")

        if not api_key:
            raise Exception("API key is not provided")

        # Determinar o template do prompt
        default_file_prompt = "[Insert path to file containing LLM Prompt. Example: c:\\prompt.txt]"
        if llm_prompt_from_file != default_file_prompt and os.path.isfile(llm_prompt_from_file):
            with open(llm_prompt_from_file, 'r') as file:
                llm_prompt = file.read()
        elif llm_prompt_from_file != default_file_prompt:
            raise Exception(f"Invalid file path: {llm_prompt_from_file}")

        if llm_prompt == "[Insert prompt template here]":
            llm_prompt = ""

        # Concatenar o prompt template com o texto de entrada
        full_prompt = f"{llm_prompt}\n{image_prompt}".strip()
        response = self.call_llm(full_prompt, api_key, model_name)
        return (response,)

    def call_llm(self, prompt, api_key, model_name):
        client = Groq(
            api_key=api_key,
        )
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=model_name,
        )
        return chat_completion.choices[0].message.content

NODE_CLASS_MAPPINGS = {
    "LLMPE": LLMPEv01
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LLMPE": "LLM Prompt Enhancer 0.1"
}
