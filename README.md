# NLP Project: Sentiment Analysis & Spam Detection

## 📌 Introduction
This project focuses on performing **binary text classification** to distinguish between:
- **Ham** → Legitimate messages  
- **Spam** → Irrelevant/promotional messages  

Originally, the dataset had **279 unique sentiment labels**, which were too granular for modeling. The task was simplified into a **ham vs. spam** classification problem.  

### 🔧 Tech Stack
- **Data Handling:** pandas, numpy, joblib  
- **NLP Processing:** nltk (tokenization, stopwords, lemmatization), re (regex)  
- **ML & Feature Engineering:** scikit-learn (models, pipelines, metrics, GridSearchCV)  
- **Visualization:** wordcloud, matplotlib, seaborn  
- **Custom Utils:** Local `Custom_func.Functions` module  

---

## 📊 Dataset
- **File:** `3) Sentiment dataset.csv`  
- **Shape:** 732 rows × 13 columns (after cleaning)  

### Key Features:
- `Text`: Raw message content  
- `Sentiment`: Original 279-label sentiment category  
- `Timestamp`: Date of post (converted to datetime)  
- `Spam`: New binary target (ham vs. spam)  

### Class Distribution:
- **ham:** 652 (89.1%)  
- **spam:** 80 (10.9%) → ⚠️ Class imbalance issue  

---

## ⚙️ Data Preprocessing
1. Dropped redundant index columns  
2. Converted `Timestamp` to datetime  
3. Created **binary target (`Spam`)** using custom mapping  
4. Configured NLTK (stopwords, lemmatizer, tokenizer)  
5. Prepared for text preprocessing: cleaning, lowercasing, tokenization, stopword removal, lemmatization  

---

## 🔍 Exploratory Data Analysis (EDA)
- **Class Imbalance:** Strong skew toward `ham`  
- **Word Clouds:**  
  - Spam → words like `new`, `excitement`, `school`, `adventure`  
  - Ham → words like `life`, `dreams`, `feeling`, `heart`  

➡️ Distinct linguistic patterns show strong separation potential.  

---

## 🤖 Modeling Plan
A **scikit-learn pipeline** was prepared (but not executed yet):  
1. **Preprocessing:** Custom cleaning + `TfidfVectorizer`  
2. **Dimensionality Reduction (optional):** TruncatedSVD  
3. **Models to test:**  
   - Logistic Regression  
   - Linear SVC  
   - Multinomial Naive Bayes  
   - Random Forest / Decision Tree  
   - KNN  
4. **Evaluation Metrics:** accuracy, precision, recall, f1-score  
5. **Validation:** StratifiedKFold + GridSearchCV  

---

## ✅ Conclusion
- Converted a **complex multi-class sentiment dataset** into a practical **binary spam detection** task.  
- Preprocessing & EDA confirmed **distinct patterns** between ham and spam.  
- A robust ML pipeline was prepared for training, evaluation, and hyperparameter tuning.  

---

## 🚀 Future Work
- Handle imbalance: SMOTE or class weighting  
- Use embeddings: Word2Vec, GloVe, FastText  
- Try deep learning: LSTMs, GRUs, Transformers (BERT, DistilBERT)  
- Perform full GridSearch hyperparameter tuning  
- Deploy as API (Flask/FastAPI)  

---
```
✍️ Author: Ahmed Hamed  
```
