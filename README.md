# LLMPE
Custom Node - LLM Prompt Enhancer for Comfy UI

LLMPE is a simple yet powerful custom node for Comfy UI that enhances prompts.
Using LLMs and a customizable instruction set, LLMPE allows for easily adding details, stylizing and formatting of Text to Image prompts unleashing the power of advanced LLM features like in-context learning.

Currently it supports four different LLM models, all hosted at Groq.com. 
As of June 2024, Groq API usage is free. 

Future versions will support other providers and models.

## Dependencies:
LLMPE relies on the Groq API.

## Installing:

1 - Copy LLMPEv01.py into Comfy UI\custom_nodes and restart Comfy UI.

2 - Install the Groq API dependencies going to the command prompt and typing: python -m pip install groq.

For Comfy UI portable:
If you are using the portable version of Comfy UI, first navigate to ComfyUI\python_embedded and then run python -m pip install groq.

## Overview:
LLMPE was created to be easy to use and highly customizable! 
This node has five fields:

Model_name (required): Select from the four models available: Llama 3 70b, Llama 3 8b, Mixtral 7x8b, or Gemma 7b. (Llama 3 70b is highly recommended!)

api_key (required): Insert your Groq API key.

Image Prompt (required): Text to image prompt to be enhanced by the LLM.

LLM Prompt (required): Set of instructions that will guide the LLM in the enhancement process.

File path to LLM Prompt (optional): Path to a file containing the set of instructions for the LLM.

## How to Use:

1 - Link LLM output to Positive Conditioning.

2 - Select the desired LLM Model.

3 - Paste your Groq API key into the api_key field.

4 - Describe your image and you are good to go!

## Customizing the enhancing algorithm:
It's possible to customize the default set of instructions for the LLM to fit your specific use case. 

Simply change the instruction set in the LLM Prompt field to your liking.

Optionally, the path to a text file containing the full set of instructions for the LLM may be provided, allowing for different enhancement algorithms tailored to different use cases and checkpoints.

An example instruction set is provided in the "Prompt1.txt" file.

**When loading the instruction set from a file, the instruction set from the node textbox is ignored.**

## Inspecting the LLM enhanced prompt:
Using Pythongosssss "Show Text" custom node connected to LLMPE output to inspect the enhanced prompt is recommended.

## Generating a new LLM enhanced prompt:
Any change to the Image prompt will trigger a new LLM call to enhance the prompt. 

To generate a new enhanced prompt, simply add/remove a space from the Image prompt field and queue again.

Have Fun! Cheers from Brazil!

### Disclaimer: LLMPE is my very first custom node, and this is its first version, so expect things to be broken or suboptimal.
