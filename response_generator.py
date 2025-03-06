# response_generator.py
def generate_response(query, search_results):
    if "Error" in search_results[0]:
        return "Sorry, I couldn’t fetch the info right now. Try again later!"
    
    if not search_results or "No relevant results" in search_results[0]:
        return f"I couldn’t find anything useful about '{query}'. Try rephrasing your question!"
    
    # Simple response generation: summarize the first few results
    response = f"Here’s what I found about '{query}':\n"
    for i, result in enumerate(search_results, 1):
        response += f"{i}. {result}\n"
    response += "Anything else you’d like to know?"
    
    return response