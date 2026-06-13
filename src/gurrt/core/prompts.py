BLIP_CUSTOM_PROMPT = "A detailed description of what is going on in this picture: "

LLM_QUERY_PROMPT = """
Answer the question using only the information available below.
- Respond with a detailed descriptive answer only.
- If frames context is insufficient utilize audio context and vice versa
VIDEO:
{context_frame}

AUDIO:
{context_audio}

below is some previous chat context given if the user wants to reeally ask something from teh previous conversation
{previous_chat}

QUESTION:
{query}

ANSWER:
"""

GEMMA_CAPTION_PROMPT =  "Analyze this video lecture frame for a search indexing engine. Provide**On-Screen Content**: [Transcribe  any key text, equations, bullet points, or diagrams visible].Be concise to the point No prose.No formatting.No introductions.No explanations."