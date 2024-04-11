# -*- coding: utf-8 -*-
"""Lab_user_simulation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XOHYsFDkteH6xAiSZi5jBKEGSnhf7_ne

## user simulation

files needed:
junior_df (pre-clustering)
senior_df(pre-clustering)
expert_df(pre-clustering)
skill_dict (json file)
degree_dict (json file)
"""

from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MultiLabelBinarizer
import numpy as np
import pandas as pd
import json
from collections import Counter
import ast
import re


# Ignore all warning messages
warnings.filterwarnings("ignore")
pd.set_option('display.max_colwidth', None)

import pandas as pd
import ast
from collections import Counter
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import json

def map_exp_index(exp_duration):
    if exp_duration < 100:
        return 'junior'
    elif exp_duration > 250:
        return 'expert'
    else:
        return 'senior'

def exp_group_kmeans(model_df, test_df):
    # Extract features from the DataFrame
    features_df = model_df[['degree_field', 'courses_title', 'cert_titles', 'skills']]

    # Convert lists of strings into a list of lists
    degree_field_lists = features_df['degree_field'].tolist()
    courses_title_lists = features_df['courses_title'].tolist()
    skills_lists = features_df['skills'].tolist()
    cert_titles_lists = features_df['cert_titles'].tolist()

    # Extract features from the DataFrame
    test_features_df = test_df[['degree_field', 'courses_title', 'cert_titles', 'skills']]

    # Convert lists of strings into a list of lists
    test_degree_field_lists = test_features_df['degree_field'].tolist()
    test_courses_title_lists = test_features_df['courses_title'].tolist()
    test_skills_lists = test_features_df['skills'].tolist()
    test_cert_titles_lists = test_features_df['cert_titles'].tolist()

    # Create a set of all unique values
    unique_values = set()
    for lst in degree_field_lists + skills_lists + cert_titles_lists + courses_title_lists + test_degree_field_lists + test_skills_lists + test_cert_titles_lists + test_courses_title_lists:
        unique_values.update(filter(None, lst))

    # Create a MultiLabelBinarizer and fit it to the unique values
    mlb = MultiLabelBinarizer(classes=sorted(unique_values))
    degree_field_encoded = mlb.fit_transform(degree_field_lists)
    courses_title_encoded = mlb.transform(courses_title_lists)
    skills_encoded = mlb.transform(skills_lists)
    cert_titles_encoded = mlb.transform(cert_titles_lists)

    test_degree_field_encoded = mlb.fit_transform(test_degree_field_lists)
    test_courses_title_encoded = mlb.transform(test_courses_title_lists)
    test_skills_encoded = mlb.transform(test_skills_lists)
    test_cert_titles_encoded = mlb.transform(test_cert_titles_lists)

    # Combine one-hot encoded features into X
    X = pd.DataFrame(degree_field_encoded + cert_titles_encoded + courses_title_encoded, columns=mlb.classes_)
    X_test = pd.DataFrame(test_degree_field_encoded + test_cert_titles_encoded + test_courses_title_encoded, columns=mlb.classes_)
    concatenated_X = pd.concat([X, X_test])

    # Perform PCA
    pca = PCA(n_components=5)
    concatenated_X_pca = pca.fit_transform(concatenated_X)
    X_pca = concatenated_X_pca[:len(X)]
    X_test_pca = concatenated_X_pca[len(X):]

    # Perform clustering with KMeans on training data
    silhouette_scores = []
    for n_clusters in range(15, 30):
        kmeans = KMeans(n_clusters=n_clusters, random_state=42,n_init='auto')
        cluster_labels = kmeans.fit_predict(X_pca)
        silhouette_avg = silhouette_score(X, cluster_labels)
        silhouette_scores.append((silhouette_avg, n_clusters))

    # Find the best number of clusters based on silhouette score
    best_num_clusters = max(silhouette_scores, key=lambda x: x[0])[1]
    #print(f"Best number of clusters based on silhouette score: {best_num_clusters}")

    # Train the final KMeans model with the best number of clusters using training data
    kmeans = KMeans(n_clusters=best_num_clusters, random_state=42,n_init='auto')
    train_cluster_labels = kmeans.fit_predict(X_pca)

    # Predict clusters for the test data
    test_cluster_labels = kmeans.predict(X_test_pca)

    # Add cluster labels to the DataFrame
    model_df['cluster_label'] = train_cluster_labels

    # Mark which rows are train data (True) and which row is test data (False)
    test_df['cluster_label'] =  test_cluster_labels

    model_df_output = model_df[["skills", 'degree_field', 'courses_title', "cert_titles", 'cluster_label']]
    test_df_output = test_df[["skills", 'degree_field', 'courses_title', "cert_titles", 'cluster_label','exp_index']]
    # Return the modified DataFrame and the trained KMeans model
    return  model_df_output,test_df_output

def create_dict(clustered_dfs,df_names):
    #create a dict with key [dataset,cluster,column] and gives a freq sorted list of values
    stats_dict = {}
    # Iterate over each dataset
    for i, dataset in enumerate(clustered_dfs):
        # Split the dataset by the value of the "cluster" column
        clusters = dataset.groupby('cluster_label')

        # Iterate over each cluster
        for cluster, data in clusters:
            # Iterate over each column
            column_values = 0
            for column in data.columns:
                # Skip the "cluster" column itself
                if column == 'cluster_label' or column == 'degree_field':
                    continue

                column_values = data[column].tolist()
                column_values = [ast.literal_eval(value) for value in column_values ]
                column_values = [sublist for sublist in column_values if any(sublist)]
                flat_values = [item for sublist in column_values for item in sublist]
                # Count the occurrences of each element
                counts = Counter(flat_values)
                # Sort the elements based on their frequency
                sorted_elements = sorted(counts.items(), key=lambda x: x[1], reverse=True)
                sorted_elements = [t[0] for t in sorted_elements]
                # Add the sorted elements to the result dictionary
                key = (df_names[i], cluster, column)
                #print(key)
                stats_dict[key] = sorted_elements
    return stats_dict

def map_new_skills(row):
    exp_index = row['exp_index']
    cluster_label = row['cluster_label']
    key = (exp_index, cluster_label)
    return

def user_recommendation(test_df):
    ## add a row that turns a csv into a pd df, not sure how when not in pandas
    exp_dfs = []
    exp_dfs.append(pd.read_csv('junior_df.csv'))
    exp_dfs.append(pd.read_csv('senior_df.csv'))
    exp_dfs.append(pd.read_csv('expert_df.csv'))
    df_names = ['junior', 'senior', 'expert']
    test_df['exp_index'] = test_df['exp_duration'].apply(lambda x: map_exp_index(x))
    exp_test_dfs = []
    for name in df_names:
        exp_test_dfs.append(test_df[test_df['exp_index'] == name])

    for i,test_df in enumerate(exp_test_dfs):
        if len(test_df)==0:
            updated_list = exp_dfs[:i] + exp_dfs[i + 1:]
            updated_list = df_names[:i] + df_names[i + 1:]

    exp_test_dfs = [df for df in exp_test_dfs if len(df)>0]
    clustered_dfs = []
    clustered_test_dfs = []
    for df, test_df, name in zip(exp_dfs,exp_test_dfs,df_names):
        clustered_df, clustered_test_df = exp_group_kmeans(df,test_df)
        clustered_dfs.append(clustered_df)
        clustered_test_dfs.append(clustered_test_df)


    stats_dict = create_dict(clustered_dfs,df_names)

    with open('clean_data\skill_dict.json', 'r') as json_file:
        skill_dict = json.load(json_file)

    with open('clean_data\degree_dict.json', 'r') as json_file:
        degree_dict = json.load(json_file)

    exp_index = clustered_test_dfs[0]['exp_index'].iloc[0]
    #exp_index = 'junior'
    #print(clustered_test_dfs[0].loc[0])
    cluster_label = clustered_test_dfs[0]['cluster_label'].iloc[0]
    #print(f"cluster: {cluster_label}")
    new_skills = stats_dict[exp_index,cluster_label,'skills']
    new_certifications = stats_dict[exp_index,cluster_label,'cert_titles']
    new_courses = stats_dict[exp_index,cluster_label,'courses_title']
    #recommended_skills = [skill_dict.get(skill[:4],skill) for skill in new_skills]

    print("Hello there! Based on your experience level and education, here are our recommendations for you:\n")

    print("Recommended Skills:")
    for idx, skill in enumerate(new_skills[4:9], start=1):
        recommended_skills = skill_dict.get(skill, skill)
        if isinstance(recommended_skills, list):
            recommended_skills = recommended_skills[4:5]
        print(f"{idx}. You should learn about {skill}: We suggest learning - {', '.join(recommended_skills)}")

    print("\nRecommended Courses:")
    for course in new_courses[3:6]:
        print(f"- {course}")

    print("\nRecommended Certifications:")
    for certification in new_certifications[:3]:
        print(f"- {certification}")

    print("\nWe hope you find these recommendations helpful for advancing your career and skillset!")

def run_user(url):
  junior = pd.read_csv('clean_data\junior_df.csv')
  senior = pd.read_csv('clean_data\senior_df.csv')
  expert = pd.read_csv('clean_data\expert_df.csv')
  merged_df = pd.concat([junior, senior, expert], ignore_index=True)
  test_user_url = url
  test_user = merged_df[merged_df['url']==test_user_url]
  test_user["exp_duration"] = 50
  print("The user's profile:")
  display(test_user[['skills','degree_field','courses_title','cert_titles']].head())
  user_recommendation(test_user)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        link = sys.argv[1]
        run_user(link)

