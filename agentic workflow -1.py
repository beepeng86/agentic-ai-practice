"""
Program Management Knowledge Agent - Starter Code

This program demonstrates two approaches to answering program management questions:
1. Using hardcoded knowledge
2. Using an LLM API

Complete the TODOs to build your knowledge agent.
"""

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY_0")
print(f"OpenAI API Key: {openai_api_key}")

client = OpenAI(
    base_url="https://openai.vocareum.com/v1",
    api_key=openai_api_key)

def get_hardcoded_answer(question):
    """
    Return answers to program management questions using hardcoded knowledge.
    
    Args:
        question (str): The question about program management
        
    Returns:
        str: The answer to the question
    """
    question = question.lower()
    
    # Knowledge base with hardcoded answers
    knowledge_base = {
        "what is program management?": "Program management is the process of managing multiple related projects to achieve strategic objectives.",
        "what are the key roles in program management?": "Key roles include Program Manager, Project Managers, Stakeholders, and Team Members.",
        "how do you measure program success?": "Program success can be measured by evaluating if the program meets its objectives, stays within budget, and delivers value to stakeholders."
    }
    return knowledge_base.get(question, "I'm sorry, I don't have an answer for that question.")

def get_llm_answer(question):
    """
    Get answers to program management questions using an LLM API.
    
    Args:
        question (str): The question about program management
        
    Returns:
        str: The answer from the LLM
    """
    if not openai_api_key:
        return "OpenAI API key is not set. Cannot fetch answer from LLM."
    
    try:
        prompt = f"Please answer this question about program management: {question}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a program management expert. Provide concise, accurate answers to questions about program management concepts, methodologies, and best practices."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred while fetching the answer from LLM: {str(e)}"
    
    # TODO: Implement the API call to get an answer from the LLM
    # Use a system message to specify that the LLM should act as a program management expert
    
    # TODO: Add error handling for API calls
    pass

# Demo function to compare both approaches
def compare_answers(question):
    """Compare answers from both approaches for a given question."""
    print(f"\nQuestion: {question}")
    print("-" * 50)
    
    hardcoded_answer = get_hardcoded_answer(question)
    print(f"Hardcoded Answer:\n{hardcoded_answer}")
    
    llm_answer = get_llm_answer(question)
    print(f"LLM Answer:\n{llm_answer}")
    
    print("=" * 50)

# Demo with sample questions
if __name__ == "__main__":
    print("PROGRAM MANAGEMENT KNOWLEDGE AGENT DEMO")
    print("=" * 50)
    
    # TODO: Create a list of sample program management questions
    sample_questions = [
        "What is program management?",
        "What are the key roles in program management?",
        "How do you measure program success?"
    ]
    
    # TODO: Loop through the questions and compare answers
    for question in sample_questions:
        compare_answers(question)