
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_model():
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    with open('model.pkl', 'wb') as f:
        pickle.dump((clf, data.feature_names, data.target_names), f)

if __name__ == '__main__':
    train_model()
