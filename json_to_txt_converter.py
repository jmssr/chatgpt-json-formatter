import json
import sys
from datetime import datetime

def epoch_to_readable(epoch_time):
    """Convert epoch timestamp to human-readable format."""
    try:
        return datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')
    except:
        return str(epoch_time)

def process_message(message_data):
    """Extract and format relevant fields from a message."""
    output_lines = []
    create_time_value = None
    
    # Check if this message has the 'parts' field
    if 'content' in message_data and 'parts' in message_data['content']:
        
        # Extract create_time
        if 'create_time' in message_data and message_data['create_time'] is not None:
            create_time_value = message_data['create_time']
            create_time = epoch_to_readable(create_time_value)
            output_lines.append(f"Time: {create_time}")
        
        # Extract role and format it
        if 'author' in message_data and 'role' in message_data['author']:
            role = message_data['author']['role']
            if role == 'user':
                output_lines.append("Me:")
            elif role == 'assistant':
                output_lines.append("ChatGPT:")
            else:
                output_lines.append(f"{role}:")
        
        # Print parts as-is
        parts = message_data['content']['parts']
        for part in parts:
            output_lines.append(str(part))
        
        output_lines.append("")  # Add blank line for separation
    
    return output_lines, create_time_value

def json_to_filtered_text(json_file_path):
    """
    Convert JSON file to filtered plain text output.
    
    Args:
        json_file_path: Path to the input JSON file
    """
    try:
        # Read the JSON file
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        all_messages = []
        
        # Navigate through the nested structure and collect all messages
        # Structure: List → Conversation → mapping → message_id → message
        if isinstance(data, list):
            # Iterate through conversations
            for conversation in data:
                if isinstance(conversation, dict) and 'mapping' in conversation:
                    # Each conversation has a 'mapping' dictionary of messages
                    mapping = conversation['mapping']
                    for message_id, message_wrapper in mapping.items():
                        if isinstance(message_wrapper, dict) and 'message' in message_wrapper:
                            message = message_wrapper['message']
                            if message is not None:  # Some messages are null
                                message_lines, create_time = process_message(message)
                                if message_lines:  # Only add if there's content
                                    all_messages.append((create_time, message_lines))
        elif isinstance(data, dict):
            # If data is a single conversation dictionary
            if 'mapping' in data:
                mapping = data['mapping']
                for message_id, message_wrapper in mapping.items():
                    if isinstance(message_wrapper, dict) and 'message' in message_wrapper:
                        message = message_wrapper['message']
                        if message is not None:
                            message_lines, create_time = process_message(message)
                            if message_lines:
                                all_messages.append((create_time, message_lines))
        
        # Sort by create_time (oldest first)
        # Handle None values by putting them at the end
        all_messages.sort(key=lambda x: x[0] if x[0] is not None else float('inf'))
        
        # Print sorted messages
        for create_time, message_lines in all_messages:
            for line in message_lines:
                print(line)
            
    except FileNotFoundError:
        print(f"Error: File '{json_file_path}' not found.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: '{json_file_path}' is not a valid JSON file.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 json_to_txt_converter.py <input.json> > output.txt", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    json_to_filtered_text(input_file)