import os
import re
import nltk
import json
import pickle
from tqdm import tqdm
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class TextData:
    def __init__(self, directory):
        self.directory = directory
        self.preprocessed_data = {}

    def load_data(self):
        files = os.listdir(self.directory)
        if os.path.exists("search_indexer/proceesed_data.pkl"):
            self.preprocessed_data = pickle.load(open('search_indexer/proceesed_data.pkl', 'rb'))
        else:
            progress_bar = tqdm(total=len(files))
            for filename in files:
                if filename.endswith(".json"):
                    filepath = os.path.join(self.directory, filename)
                    with open(filepath, 'r', encoding='utf8') as file:
                        data = json.load(file)
                        preprocessed_text = self.preprocess_text(data)
                        if preprocessed_text:
                            self.preprocessed_data[filepath] = preprocessed_text
                        progress_bar.update(1)
            pickle.dump(self.preprocessed_data, open('search_indexer/proceesed_data.pkl', 'wb'))
            progress_bar.close()

    def preprocess_text(self, data):
        text = ''
        lemmatizer = WordNetLemmatizer()

        def step_combo(x):
            return x["title"] + x["subtitle"] + str.join("", x["sub-points"])

        def point(x):
            return x["name"] + str.join("", list(map(step_combo, x["steps"])))

        if 'article' in data and 'intro' in data:
            text = data['article'] + data['intro'] + str.join("", list(map(point, data['points'])))
        else:
            return ''  # Return empty string if the text cannot be processed

        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        words = nltk.word_tokenize(text)
        words = [lemmatizer.lemmatize(word) for word in words if word not in stopwords.words('english')]
        text = ' '.join(words)
        return text


class TextVectorizer:
    def __init__(self, texts: dict):
        self.texts: dict = texts
        self.tfidf_vectorizer = TfidfVectorizer()
        self.tfidf_matrix = None

    def fit(self):
        corpus = list(self.texts.values())
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(corpus)

    def query(self, query, k=10):
        if self.tfidf_matrix is None:
            raise ValueError("Vectorizer not fitted")

        # Preprocess the query text
        preprocessed_query = self.preprocess_text({'article': query})

        # Transform the query text using the same vectorizer
        query_vec = self.tfidf_vectorizer.transform([preprocessed_query])

        cosine_sim = cosine_similarity(query_vec, self.tfidf_matrix)
        index = cosine_sim.argsort()[0][-k-1:-1]
        filepaths = list(self.texts.keys())
        result = []

        for i in index:
            if i < len(filepaths):
                with open(filepaths[i], 'r', encoding='utf-8') as file:
                    jsonData = json.load(file)

                    item = {
                        "link": jsonData['link'],
                        "article": jsonData['article'],
                        "cosine_similarity": cosine_sim[0][i].item(),
                    }
                    result.append(item)

        return result

    def preprocess_text(self, data):
        text = ''
        lemmatizer = WordNetLemmatizer()

        def step_combo(x):
            return x["title"] + x["subtitle"] + str.join("", x["sub-points"])

        def point(x):
            return x["name"] + str.join("", list(map(step_combo, x["steps"])))

        if 'article' in data:
            text = data['article']
        else:
            return ''  # Return empty string if the text cannot be processed

        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        words = nltk.word_tokenize(text)
        words = [lemmatizer.lemmatize(word) for word in words if word not in stopwords.words('english')]
        text = ' '.join(words)
        return text

if __name__ == "__main__":
    data_directory = os.path.join(os.getcwd(), "crawler", "data")
    data = TextData(data_directory)
    data.load_data()
    vectorizer = TextVectorizer(data.preprocessed_data)
    vectorizer.fit()

    while True:
        query = input("Enter your query (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break

        search_results = vectorizer.query(query)
        print("Query Results:")
        for result in search_results:
            print(f"Article: {result['article']}")
            print(f"Link: {result['link']}")
            print(f"Cosine Similarity: {result['cosine_similarity']}")
