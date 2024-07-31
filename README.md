# Project: Movie Recommender System Using Machine Learning!
Recommendation systems are becoming increasingly important in today’s extremely busy world. People are always short on time with the myriad tasks they need to accomplish in the limited 24 hours. Therefore, the recommendation systems are important as they help them make the right choices, without having to expend their cognitive resources.

The purpose of a recommendation system basically is to search for content that would be interesting to an individual. Moreover, it involves a number of factors to create personalised lists of useful and interesting content specific to each user/individual. Recommendation systems are Artificial Intelligence based algorithms that skim through all possible options and create a customized list of items that are interesting and relevant to an individual. These results are based on their profile, search/browsing history, what other people with similar traits/demographics are watching, and how likely are you to watch those movies. This is achieved through predictive modeling and heuristics with the data available.
## Types of Recommendation System:

### 1) Content Based:

- Content-based systems, which use characteristic information and take item attributes into consideration.
- Examples: Twitter, YouTube.
- Analyzes user-specific actions or similar items recommendation.
- Creates a vector of item features for recommendations.
- **Pros:** Tailored recommendations based on user history.
- **Cons:** May lead to over-specialization and limit recommendations to specific categories.

### 2) Collaborative Based:

- Collaborative filtering systems, which are based on user-item interactions.
- Examples: Book recommendations, clustering users with similar ratings.
- **Pros:** Recommendations based on user similarity and interactions.
- **Cons:** Computationally expensive, may favor popular items, and struggle with new items.

### 3) Hybrid Based:

- Hybrid systems, which combine both content-based and collaborative filtering approaches.
- **Pros:** Combines the strengths of both methods to improve recommendation accuracy.
- **Cons:** Complex implementation and requires balancing both approaches.

## Concept Used to Build the `model.pkl` File: Cosine Similarity

1. **Cosine Similarity** is a metric that measures the similarity between documents.
2. Vectors are required to demonstrate cosine similarity, which are represented as numpy arrays.
3. Use the `cosine_similarity()` function to calculate the similarity between two vectors.
4. The result is a value between [0, 1], where 0 means completely different and 1 means completely similar.
5. For more details, check the URL: [Cosine Similarity Explanation](https://www.learndatasci.com/glossary/cosine-similarity/)

## Dataset Used:

* [Dataset link](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

## How to Run?

### STEPS:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/entbappy/Movie-Recommender-System-Using-Machine-Learning.git

2. **Create a Virtual Environment:**
   It is recommended to use a virtual environment to manage your project's dependencies. To create and activate a virtual environment, run:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
3. **Install the Dependencies:**
   Once the virtual environment is activated, install the required packages using `pip`:

   ```bash
   pip install -r requirements.txt

4. **Run the Application:**

   With the dependencies installed, you can now run the Streamlit application. Execute the following command:

   ```bash
   streamlit run app.py
   
5. **Access the Application:**

   Once the application is running, Streamlit will provide a local URL (usually http://localhost:8501) in your terminal. Open this URL in your web browser to interact with your Movie Recommender System.

   If you are running the application on a remote server or cloud service, make sure to use the appropriate URL provided by your hosting service.

