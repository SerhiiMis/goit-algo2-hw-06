import string
import requests
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt

def get_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        return None

def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))

def map_function(word):
    return word.lower(), 1

def shuffle_function(mapped_values):
    shuffled = defaultdict(list)
    for key, value in mapped_values:
        shuffled[key].append(value)
    return shuffled.items()

def reduce_function(key_values):
    key, values = key_values
    return key, sum(values)

def map_reduce(text, search_words=None):
    text = remove_punctuation(text)
    words = text.split()

    if search_words:
        search_words = [w.lower() for w in search_words]
        words = [word for word in words if word.lower() in search_words]

    with ThreadPoolExecutor() as executor:
        mapped = list(executor.map(map_function, words))

    shuffled = shuffle_function(mapped)

    with ThreadPoolExecutor() as executor:
        reduced = list(executor.map(reduce_function, shuffled))

    return dict(reduced)

def visualize_top_words(word_counts, top_n=10):
    top = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    words, counts = zip(*top)
    
    plt.figure(figsize=(10, 6))
    plt.barh(words[::-1], counts[::-1], color='skyblue')
    plt.xlabel("Frequency")
    plt.ylabel("Words")
    plt.title(f"Top {top_n} Most Frequent Words")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    url = "https://www.gutenberg.org/files/1342/1342-0.txt"  # Pride and Prejudice

    text = get_text(url)
    if text:
        result = map_reduce(text)  # Or use: map_reduce(text, search_words=['love', 'man', 'time'])
        print("Результат підрахунку слів:", dict(list(result.items())[:10]))
        visualize_top_words(result, top_n=10)
    else:
        print("Помилка: Не вдалося отримати текст з URL.")
