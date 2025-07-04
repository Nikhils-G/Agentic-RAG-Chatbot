import cohere
import streamlit as st  # ✅ added this

# Initialize Cohere client with your API key
co = cohere.Client("2xTRZVraYBDx8GILR5d8CuTtwvyWnsiHayzM1TH5")

class LLMResponseAgent:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        dispatcher.register_agent("LLMResponseAgent", self.handle)

    def handle(self, message):
        context = message.payload["retrieved_context"]
        query = message.payload["query"]

        # Formulate prompt combining context and user query
        prompt = f"Context:\n{context}\n\nQuestion: {query}"

        # Call Cohere LLM
        response = co.generate(
            model="command-r-plus",  # Or 'command' if on free tier
            prompt=prompt,
            max_tokens=300,
            temperature=0.3
        )

        # Safety check for generations response
        if response.generations:
            answer = response.generations[0].text.strip()

            # ✅ Save result to Streamlit session state
            st.session_state["llm_response"] = answer

            print("Answer:", answer)  # optional for terminal log
        else:
            st.session_state["llm_response"] = "No response generated."
            print("No response generated.")
