# 📘 Word Frequency Analysis Using MapReduce in Python

## 🎯 Task Description

Create a Python script that:

1. Downloads text from a given URL
2. Analyzes word frequency using a simplified **MapReduce paradigm**
3. Visualizes the **Top N most frequent words** using `matplotlib`

---

## ✅ Functional Requirements

- Use a parallelized MapReduce-like approach with:
  - `map_function(word) -> (word, 1)`
  - `shuffle_function(mapped_data)`
  - `reduce_function((word, [1,1,...])) -> (word, count)`
- Optional: filter only specific search words
- Download text using `requests`
- Clean punctuation using `string.punctuation`
- Visualize results using `matplotlib.pyplot`

---

## 🧪 Example

### 🔗 Example URL:

[https://gutenberg.org/files/1342/1342-0.txt](https://gutenberg.org/files/1342/1342-0.txt)

### 🔍 Search words:

```python
search_words = ['love', 'war', 'peace']
```

### ✅ Expected Output:

Terminal:

```
Результат підрахунку слів: {'war': 203, 'peace': 132, 'love': 245}
```

Bar chart:

- Horizontal bars
- X-axis: frequency
- Y-axis: top words

---

## 📈 Visualization

Use `matplotlib` to create a bar chart with:

- `plt.barh(words[::-1], counts[::-1])`
- Title: "Top N Most Frequent Words"
- X label: "Frequency"
- Y label: "Words"

---

## 🧩 Optional Enhancements

- Use `ThreadPoolExecutor` for parallel mapping/reducing
- Add CLI arguments for:
  - custom URL
  - number of top words
  - specific search terms

---

## 🛠️ Requirements

```bash
pip install matplotlib requests
```

---

## 📂 Output Example

```
Результат підрахунку слів: {'love': 245, 'war': 203, 'peace': 132}
```

And a bar chart displaying the top 10 most frequent words.
