import requests

def get_fun_fact(number):
    try:
        response = requests.get(f'http://numbersapi.com/{number}', timeout=5)
        
        # Check if the request was successful
        if response.status_code == 200:
            return response.text.strip()  # Remove any extra spaces or newlines
        
        return f"Could not retrieve a fun fact for {number}."
    
    except requests.exceptions.Timeout:
        return "Fun fact service is taking too long to respond."
    
    except requests.exceptions.ConnectionError:
        return "Unable to connect to the fun fact service."
    
    except requests.exceptions.RequestException:
        return "Fun fact service is currently unavailable."
