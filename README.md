# 📘 Word Frequency Analysis Using MapReduce in Python

## 🎯 Task Description

Create a Python script that:

1. Downloads text from a given URL
2. Analyzes word frequency using a simplified **MapReduce paradigm**
3. Visualizes the **Top N most frequent words** using `matplotlib`

---

## ✅ Functional Requirements

- Use a parallel MapReduce-like pipeline with:
  - `map_function(word) -> (word, 1)`
  - `shuffle_function(mapped_data)`
  - `reduce_function((word, [1,1,...])) -> (word, count)`
- Download text using `requests`
- Clean punctuation using `string.punctuation`
- Visualize results using `matplotlib.pyplot`
- Supports optional filtering by specific search words
- ThreadPoolExecutor used for parallel map/reduce stages

---

## 🧪 Example Usage

### 🔗 Example URL:

`https://www.gutenberg.org/files/1342/1342-0.txt` (Pride and Prejudice)

### 🔍 Search words (optional):

```python
search_words = ['love', 'war', 'peace']
```

### ✅ Example Output:

```
Результат підрахунку слів: {'the': 4622, 'of': 3825, 'and': 3123, 'to': 2761, 'a': 2164, 'in': 1904, 'was': 1846, 'that': 1644, 'it': 1571, 'her': 1564}
```

And a horizontal bar chart showing the **top 10 most frequent words**.

---

## 📈 Visualization Details

- Horizontal bar chart
- X-axis: frequency
- Y-axis: word
- Chart built using:

```python
plt.barh(words[::-1], counts[::-1])
```

---

## 🧩 Optional Enhancements

- Accept URL or `top_n` as CLI arguments
- Limit to search-specific words
- Export results to a file (CSV or JSON)

---

## 🛠️ Installation

Install required libraries:

```bash
pip install matplotlib requests
```

---

## 📂 Output Example (Terminal + Chart)

```
Результат підрахунку слів: {'the': 4622, 'of': 3825, 'and': 3123, 'to': 2761, 'a': 2164, 'in': 1904, 'was': 1846, 'that': 1644, 'it': 1571, 'her': 1564}
```

📊 Bar chart appears with most frequent words in descending order.
