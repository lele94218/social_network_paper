from sklearn.feature_extraction.text import CountVectorizer

train_set = ("The sky is blue.", "The sun is bright.")
test_set = ("The sun in the sky is bright.",
"We can see the shining sun, the bright sun.")

count_vectorizer = CountVectorizer()
vec1 = count_vectorizer.fit_transform(train_set)
print vec1.toarray()

freq_term_matrix = count_vectorizer.transform(test_set)
print freq_term_matrix.toarray()

from sklearn.feature_extraction import DictVectorizer
measurements = [
     {'city': 'Dubai', 'temperature': 33.},
     {'city': 'London', 'temperature': 12.},
     {'city': 'San Fransisco', 'temperature': 18.},
]

vec = DictVectorizer()

print vec.fit_transform(measurements).toarray()
print vec.get_feature_names()
