import requests

def count_words(text):
    response = requests.post('http://localhost:5000/read', json={'text': text})
    if response.status_code == 200:
        data = response.json()
        print("Debug info: response = ", data)
        return data.get('count', 0)
    else:
        print("Error:", response.text)
        return 0

# Example usage:
text = 'This is a sample paragraph with a series of words, some of which are long. Superfluous. Paradigm. Backspace. Passcode. Etcetera.'
word_count = count_words(text)
print("Number of words:", word_count)
if (word_count != 20):
    print("Test failed, the count was wrong!")
else:
    print("Test passed!")
