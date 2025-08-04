from .state_engine import get_current_state

def generate_prompt(user_message, memory_snapshot, config):
    state = get_current_state()
    # Спрощено: prompt формується на основі стилю та кімнати
    prompt = f"System state: Room = {state['room']}, Style = {state['style']}, Energy = {state['energy']}\n"
    prompt += f"Memory: {memory_snapshot}\n"
    prompt += f"User: {user_message}\n"
    return prompt
