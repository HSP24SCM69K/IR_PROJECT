# INFORMATION RETRIEVAL PROJECT

- **HARINI KORADA**
- **CWID: A20546869**
- **my github repo link: https://github.com/HSP24SCM69K/IR_PROJECT/blob/main/README.md**
## Abstract

The project's goal is to create an extensive information retrieval system capable of traversing web documents, indexing them, and handling text queries. It comprises three primary components: a Scrapy-powered crawler for fetching web content, a Scikit-Learn-based indexer for building an inverted index, and a Flask-driven processor for managing user queries. The crawler is configured with seed URLs and parameters like maximum pages and depth, supporting concurrent and distributed crawling. The indexer utilizes TF-IDF scoring and cosine similarity for search indexing, with optional functionalities like word2vec embedding representation and kNN similarity using FAISS. The processor validates and prioritizes user queries, offering optional features such as spelling correction and query expansion. The objective is to deliver a scalable and effective information retrieval solution for diverse scenarios, with potential enhancements through hyperparameter tuning and addressing time constraints from external APIs.

## Development Summary

The project aims at creating an extensive information retrieval system, incorporating crawling, indexing, and query processing functionalities. The primary aim is to effectively retrieve pertinent information from web documents.

### Objectives

1. **Develop a Scrapy-based web crawler to retrieve web content:** The crawler should possess the capability to fetch web documents based on specified parameters such as seed URLs, maximum pages, and depth.
2. **Implement a Scikit-Learn-based indexer to generate an inverted index:** The indexer will utilize TF-IDF scoring and cosine similarity techniques to index the downloaded documents, facilitating efficient search operations.
3. **Establish a Flask-based processor for managing user queries:** The processor will validate and rank free-text queries, delivering relevant search results based on the indexed documents.
4. **Incorporate optional features for enhanced functionality:** Additional functionalities such as word2vec embedding representation, kNN similarity using FAISS, spelling correction, and query expansion will be integrated into the system.
5. **Ensure scalability and efficiency:** The system will be designed to handle diverse use cases and scale effectively, ensuring optimal performance even with large datasets.
6. **Explore potential optimization avenues:** Investigation into further optimization possibilities through hyperparameter tuning and addressing time constraints imposed by external APIs will be conducted.
# Next Steps

1. **Develop and deploy the Scrapy-based web crawler to fetch web content.**
2. **Construct the Scikit-Learn-based indexer to create an inverted index of the retrieved documents.**
3. **Establish the Flask-based processor to manage user queries and provide relevant search results.**
4. **Integrate optional features such as word2vec embedding representation, kNN similarity using FAISS, spelling correction, and query expansion.**
5. **Perform thorough testing and validation of the information retrieval system to ensure functionality and performance.**
6. **Investigate opportunities for optimization through hyperparameter tuning and addressing time constraints from external APIs.**
7. **Deploy the system in a production environment and gather feedback for further refinement and improvement.**

## Overview

### Solution Outline

The project aims to develop a sophisticated information retrieval system that efficiently extracts relevant data from web documents. Comprising three primary components – a web crawler, indexer, and query processor – the system is designed for optimal performance.

### Literature Review

Existing research in information retrieval serves as the foundation for this project. Previous studies have explored methods for web crawling, document indexing, and query processing. Additionally, insights from literature on machine learning algorithms, including TF-IDF, cosine similarity, and word embeddings, have shaped the system's design.

### Proposed Approach

The proposed system will leverage cutting-edge technologies and methodologies to achieve its objectives. It will utilize a Scrapy-based web crawler for fetching web documents, a Scikit-Learn-based indexer for creating an inverted index, and a Flask-based query processor for managing user queries. Optional features, such as word2vec embeddings, kNN similarity with FAISS, and query expansion, will be integrated to enhance functionality. Through meticulous planning and execution, the system endeavors to deliver a scalable and effective solution for information retrieval tasks.

## Design

### System Capabilities

The information retrieval system is equipped with various capabilities aimed at enhancing the retrieval process. The web crawler component efficiently navigates through web documents, extracting relevant content based on predefined parameters such as seed URLs, maximum pages, and depth. Utilizing advanced algorithms like TF-IDF and cosine similarity, the indexer component constructs an inverted index, facilitating streamlined search operations. Meanwhile, the query processor component validates and prioritizes free-text queries, delivering precise and pertinent search outcomes to users.

### Interactions

Through a command-line interface, the system communicates with users, taking in their inquiries and returning relevant article links and content. The system components seamlessly interact to streamline the information retrieval process. As the web crawler retrieves web documents, it forwards them to the indexer, which in turn constructs an inverted index of the document contents. Upon receiving a user query, the query processor accesses this inverted index, retrieves relevant documents, and ranks them based on relevance scores before presenting the results to the user.

### Integration

The system components are integrated using standardized interfaces and communication protocols to ensure smooth operation. Communication among the web crawler, indexer, and query processor occurs via universally accepted data exchange formats, ensuring compatibility and interoperability. Additionally, optional features such as word2vec embeddings, kNN similarity with FAISS, and query expansion are seamlessly incorporated into the system, enhancing its capabilities without compromising performance or scalability.

# Architecture

## Software Components

The project consists of three key software components:

1. **Web Crawler:**
   - Its primary role is to retrieve web documents from online sources.
   - Developed utilizing the Scrapy framework.
   - Configured with parameters such as the initial URL/domain, maximum page count, and depth.
   - Additional functionalities may include concurrent retrieval (AutoThrottle) and distributed retrieval (scrapyd).

2. **Indexer:**
   - Constructs an inverted index to facilitate search functionality.
   - Built using the Scikit-Learn library.
   - Utilizes TF-IDF scoring and cosine similarity to enhance search capabilities.
   - Optional features encompass embedding representation (word2vec) and neural/semantic search kNN similarity (FAISS).

3. **Query Processor:**
   - Manages user-submitted free-text queries.
   - Developed using the Flask framework.
   - Conducts query validation/error-checking and delivers top-K ranked results.
   - Supplementary functionalities may involve query spelling correction/suggestion (NLTK) and query expansion (WordNet).

Together, these components form a comprehensive information retrieval system adept at crawling, indexing, and processing queries across web documents.

## Interfaces

Each component interacts with others through clearly defined interfaces:

1. **TextData Interface:**
   - `load_data()`: Loads data from JSON files and preprocesses it.
   - `preprocess_text()`: Performs text preprocessing including lowercase conversion, punctuation removal, tokenization, stopword removal, and lemmatization.

2. **TextVectorizer Interface:**
   - `fit()`: Trains the TF-IDF vectorizer and Word2Vec model on the preprocessed text data.
   - `query()`: Accepts a query input, vectorizes it, calculates cosine similarity, and retrieves relevant documents.

3. **Main Script Interface:**
   - Accepts user queries through input prompts.
   - Displays search results to the user.

## Implementation

Implemented in Python, the system relies on a variety of libraries and frameworks:

- The web crawler is developed using the Scrapy framework.
- The indexer employs the Scikit-Learn library for constructing the inverted index.
- The query processor utilizes the Flask framework.
- Integration of optional functionalities such as word2vec embeddings and kNN similarity may require the use of additional libraries and frameworks.

Additional Implementation Details:

- The `TextData` class utilizes the `os` module to navigate through directories and load JSON files. It preprocesses text data through various techniques such as converting to lowercase, removing punctuation, tokenizing, eliminating stopwords, and lemmatizing words.
- The `TextVectorizer` class employs scikit-learn for TF-IDF vectorization and cosine similarity computation. Additionally, it utilizes gensim for Word2Vec embedding.
- Error handling is incorporated to manage FileNotFoundError exceptions that may occur during file loading and processing.
- The main script engages with users by requesting query inputs and presenting search results accordingly.

In essence, the system's architecture is carefully crafted to facilitate seamless communication and collaboration among its components, ensuring efficient operation and optimal performance.

# Operation

## Software Commands

The software is executed using the `python main.py` command in the terminal.

## Inputs

The user provides a query to search for relevant articles and links.

## Installation

The software requires Python, along with the following packages: nltk, gensim, scikit-learn, tqdm. These packages can be installed using pip (`pip install package_name`).

# Conclusion

## Success/Failure Results

### Success

The software effectively retrieves articles relevant to the user's queries. It achieves this by leveraging preprocessing techniques to clean and prepare the text data, followed by vectorization methods to quantify the textual information. Finally, it employs cosine similarity to identify the most relevant articles based on the user's query.

### Failure

Failure may occur under certain conditions:
- If the data directory specified by the user does not exist, the software will fail to load the data, resulting in an error.
- If the data files within the directory are not in the expected JSON format, the software will encounter parsing errors when attempting to read the files.

## Outputs

The output includes the article content and corresponding links based on the user query. This output provides the user with direct access to the articles of interest, along with contextual information to understand their relevance.

- <img width="464" alt="image" src="https://github.com/HSP24SCM69K/IR_PROJECT/assets/159409891/3a4ee5ce-0899-4bd9-89de-dea357953c46">


- <img width="488" alt="image" src="https://github.com/HSP24SCM69K/IR_PROJECT/assets/159409891/bb274caf-36d4-4903-b80b-8674b9efd49d">


- <img width="447" alt="image" src="https://github.com/HSP24SCM69K/IR_PROJECT/assets/159409891/72f9923e-5e8c-4db1-8ef8-f4dba0bb2e70">


- <img width="468" alt="image" src="https://github.com/HSP24SCM69K/IR_PROJECT/assets/159409891/aa806e0a-30a0-4d49-810d-503436a65046">


# Caveats/Cautions

1. **File Paths:**
   Double-check that file paths specified in the TextData class are accurate and accessible on any machine where the code runs. Any discrepancies in directory structure or file paths could lead to FileNotFoundError issues.

2. **Data Serialization:**
   While pickle is convenient for storing processed data, ensure compatibility across different Python versions and environments to avoid issues during serialization and deserialization.

3. **Dependency Installation:**
   Confirm that all necessary dependencies like NLTK, scikit-learn, tqdm, and gensim are installed in the execution environment. Missing dependencies can cause ImportError exceptions.

4. **Resource Allocation:**
   Training the Word2Vec model might demand substantial computational resources, particularly for larger datasets. Ensure the machine running the code has enough memory and processing power for efficient model training.

5. **Exception Handling:**
   Although the code handles FileNotFoundError during file loading, be prepared to address other potential exceptions such as encoding errors or JSON parsing problems.

6. **Input Validation:**
   Implement input validation to handle unexpected user inputs gracefully, preventing errors or unexpected behavior during query processing.

7. **Documentation:**
   Thoroughly document the codebase with comments and docstrings to aid understanding and future maintenance by other developers. Clearly explain the purpose, functionality, and usage of each class and method.

By keeping these considerations in mind and exercising caution, you can improve the reliability and versatility of the code, making it easier to use in different environments.


# DATA SOURCES:

craeted json files:

- <img width="468" alt="image" src="https://github.com/HSP24SCM69K/IR_PROJECT/assets/159409891/4fcd49bc-b078-4f5c-b57e-ad85be6ac084">

# COVERAGE:

- This is my wikiHow link. I got this from output.

![image](https://github.com/HSP24SCM69K/IR_PROJECT/assets/159409891/7a01aef6-14a4-4eeb-9d26-1856e623fe51)

# SOURCE CODE: my main.py file

- <img width="468" alt="image" src="https://github.com/HSP24SCM69K/IR_PROJECT/assets/159409891/5d2940c0-b2bd-4bea-a8b6-753b0eb942a1">

- <img width="468" alt="image" src="https://github.com/HSP24SCM69K/IR_PROJECT/assets/159409891/e912b87d-d157-447f-bdcb-23d264988ad8">


- <img width="468" alt="image" src="https://github.com/HSP24SCM69K/IR_PROJECT/assets/159409891/e1e7f5d2-a428-41e8-a9d4-a2c748079c22">

- <img width="468" alt="image" src="https://github.com/HSP24SCM69K/IR_PROJECT/assets/159409891/7ab2bac6-3777-487f-a37d-0b06c11bb903">

# Processor.py

- <img width="468" alt="image" src="https://github.com/HSP24SCM69K/IR_PROJECT/assets/159409891/4b23a30a-e066-414b-8b37-8369f3176f0c">

# Indexer.py file

- <img width="468" alt="image" src="https://github.com/HSP24SCM69K/IR_PROJECT/assets/159409891/e2b9a549-920a-49f9-bd3d-63d82dcaa95a">

# Indexer2.py file:

- <img width="468" alt="image" src="https://github.com/HSP24SCM69K/IR_PROJECT/assets/159409891/ec6c40a8-2e4c-4a8a-9f8d-f34df858ba47">

# BIBILOGRAPHY-REFERENCE CITATIONS:

1. "Autothrottle Extension¶." AutoThrottle Extension - Scrapy 2.11.1 Documentation, 11 Apr. 2024, [docs.scrapy.org/en/latest/topics/autothrottle.html](https://docs.scrapy.org/en/latest/topics/autothrottle.html).

2. "Build K-Nearest Neighbor (K-NN) Similarity Search Engine with Elasticsearch." OpenSearch, [opensearch.org/blog/Building-k-Nearest-Neighbor-(k-NN)-Similarity-Search-Engine-with-Elasticsearch/](https://opensearch.org/blog/Building-k-Nearest-Neighbor-(k-NN)-Similarity-Search-Engine-with-Elasticsearch/).

3. Duke, Justin. "How to Crawl a Web Page with Scrapy and Python 3." DigitalOcean, DigitalOcean, 7 Dec. 2022, [www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3](https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3).

4. "Inverted Index." GeeksforGeeks, GeeksforGeeks, 11 Mar. 2024, [www.geeksforgeeks.org/inverted-index/](https://www.geeksforgeeks.org/inverted-index/).

5. Logunova, Inna. "Word2Vec: Why Do We Need Word Representations?" Word2Vec: Explanation and Examples, Serokell, 9 May 2023, [serokell.io/blog/word2vec](https://serokell.io/blog/word2vec).
   
6. Vembunarayanan, Jana, et al. “TF-IDF and Cosine Similarity.” Seeking Wisdom, 16 Nov. 2016, [janav.wordpress.com/2013/10/27/tf-idf-and-cosine-similarity/](https://janav.wordpress.com/2013/10/27/tf-idf-and-cosine-similarity/).




