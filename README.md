# Tech_career_roadmap
Tech Career Roadmap Personalized Guidance for Career Development using LinkedIn
# Overview:
Our project tackles the need for LinkedIn users, particularly those in the tech field, to navigate their career paths effectively. By harnessing artificial intelligence, we've developed a solution that enhances professional portfolios. Unlike conventional methods focused solely on profile presentation, our model identifies skill gaps, recommends tailored learning resources, and offers steps for career advancement. This initiative empowers users to bridge the gap between their current position and career aspirations, fostering efficiency and strategic advantages in professional development.
# System Description:
Our project delivers an innovative solution aimed at empowering LinkedIn users in the tech industry to strategically navigate their career paths. By leveraging artificial intelligence, we've developed a system that goes beyond mere profile enhancement. Our model identifies skill gaps and recommends personalized learning resources and career advancement steps, enabling users to effectively transition from their current roles to their desired career trajectories.

Key Features:

Skill Gap Identification: Pinpoints areas for professional growth.
Personalized Learning Recommendations: Suggests courses and certifications tailored to the user's specific needs.
Career Progression Strategy: Provides actionable steps for moving forward in one's career.
Our approach utilizes K-means Clustering for in-depth data analysis, categorizing users into junior, senior, and expert levels based on their experience. This classification helps tailor recommendations that resonate with the user's current professional stage. Unlike conventional methods, our algorithm focuses on suggesting new skills for development, supported by an analysis of degree fields, course titles, and certification titles.

For developers and tech enthusiasts interested in exploring the intricacies of our project or contributing to its evolution, this repository offers a comprehensive look at the algorithms, methodologies, and insights that underpin our solution.
# Getting Started:
## Setting up the Development Environment:
Pre-requisites: Git and Anaconda. 

To install and run the code on your local machine, follow these steps:
1. ### Clone the repository
   First, clone the repository to your local machine using Git. Open a terminal and run the following command:
    ```bash
    git clone https://github.com/yael-katsman/Tech_career_roadmap
2. ### Create and activate the conda environment
   After cloning the repository, navigate into the project directory:
    ```bash
    cd Tech_career_roadmap
    ```
    Then, use the following command to create a conda environment from the environment.yml file provided in the project:
    ```bash
    conda env create -f environment.yml
    ```
    Activate the environment with the following command:
   ```bash
    conda activate project_env
    ```
   ## Running the System: 
To run the project, follow these steps: 
3. Run the command:
   ```bash
   python Lab_user_simulation.py <user URL>

   ```
For this, you can use any URL in our scraping file or the following examples: 
https://www.linkedin.com/in/yuan-anne-feng-821a7618

https://www.linkedin.com/in/brent-bryan

https://www.linkedin.com/in/joselom23

## scraping and cleaning:
### choosing users to scrape:
We utilized the users’ current company and current position, as described in the BrightData- profiles data set to determine if they are considered successful in the tech field
you can see the code in the finding_users_to_scrape.ipynb and the chosen users in the scraping.zip file
### Scraping and general cleaning:
Due to limitations in accessing users' skills directly in LinkedIn profiles, we resorted to scraping the titles and URLs of videos listed under the “Add new skills with these courses” section, which are tailored to enhance various competencies and closely reflect the actual skill sets of the users, as can be seen in figures (1)+(2) in the appendix. Additionally, we leveraged Bright Data's existing scraper to collect user profile URLs and IDs for identification. 
After collecting the names of the videos we aimed to transform them into meaningful skill names, to do this we employed Geminis API. After passing the names through the API with the prompt “I will provide you a list of video names, for each name write what skill the video teaches in the following format: "video name"@ "your answer":”
Given that some skill names were similar or highly related, we applied K-means Clustering to group them accordingly, representing the skills as TF-IDF vectors. We encountered some problematic clusters that encompassed a wide range of skills without distinctly corresponding to specific skill topics, as can be seen in figure (3) . To address this issue, we conducted re-clustering exclusively on the problematic clusters. Additionally, using the Gemini API, we named all clusters, addressing any duplicate names. Finally, we mapped each user’s skills to the corresponding cluster names.
you can see the scraping code in the Scraping.ipynb and the scraped data file in the scraping.zip file or https://drive.google.com/file/d/1SJ1G9HmwvQ7vwlPNFwmojDp_SEeY4geW/view?usp=sharing
![image](https://github.com/yael-katsman/Tech_career_roadmap/assets/166139874/0955e5a2-d87c-4c3e-b160-dd273417822e)
![image](https://github.com/yael-katsman/Tech_career_roadmap/assets/166139874/c1c03974-de47-476e-ae86-6b5896638730)

Figure 1 represents a users recommended skills that appear on her LinkedIn page. Figure 2 represents the users actual skills as presented in her profile. As can be seen, the skills in the two figures highly correspond to one another, with the recommended skills closely reflecting the actual skills. 

## Data analysis:
Our data analysis primarily relied on K-means Clustering, which was applied to both skills and users' degree fields to identify patterns and group them accordingly. Additionally, we visually inspected the clusters to gain insights into their structure and composition.
To create an effective algorithm that would provide recommendations to users based on successful users in their experience level, we categorized users into three groups: junior, senior, and expert. Using figure (a), depicting users' experience distribution, we determined thresholds for each category. Users with less than 100 months of experience were classified as juniors, those with experience ranging from 100 to 250 months were labeled as seniors, and individuals with more than 250 months of experience were considered experts.
For our final algorithm, which utilized K-means clustering, we selected degree fields, course titles, and certification titles, as they offer valuable insights into each user. Skills were omitted from clustering to prioritize recommending new skills that a user can develop, rather than clustering based on existing ones. Figure (b) shows the final clusters in the junior category, represented in two dimensions.
you can see our full analysis process in model_and_eval.ipynb and run it on collab
![image](https://github.com/yael-katsman/Tech_career_roadmap/assets/166139874/224fc2c9-8cdc-476c-87be-0e4c73cd3cd3)
## AI Methodologies: 
In our project, we primarily leveraged Geminis API and K-means Clustering. Initially, we employed Geminis API to enhance the informativeness of skill names obtained through web scraping. Subsequently, K-means clustering was applied to the skills dataset, and Geminis API was again utilized to assign meaningful names to the resulting clusters. Furthermore, we conducted K-means clustering on the degree fields data, to reduce sparsity, and once more employed Geminis API for cluster naming, addressing any duplicated clusters. For both attributes, clustering was performed using TF-IDF vectors. 
In our final algorithm, we utilized K-means Clustering and PCA for dimensionality reduction for each experience category. Our feature representation included degree fields, course titles, and certification titles, encoded as multilabel binary vectors. Evaluation of the clusters was conducted using the silhouette score metric. For each category, the optimal value of K was determined to be 16, and PCA was applied with 5 
## Evaluation and Results: 
### We chose to evaluate our project using three different metrics:
you can see our full evaluation process in model_and_eval.ipynb and run it on collab
1.As our project primarily focuses on recommending relevant skills that users can develop, we elected to evaluate it based on the recommended skills for each user. To achieve this, we examined each user in our datasets across every experience category. For each category, we iterated over every cluster and retrieved the number of users that had at least one of their three skills appear in the five most frequent skills within their respective cluster. We define these users as ones who were successfully clustered. The top five skills in each cluster signify the ones we would suggest to new users within the same cluster. 

The results depicted in figures 4 (a), 4 (b), and 4 (c)  reveal interesting trends. Approximately half of the clusters in the junior category comprised more than 50% of successfully clustered users. In contrast, the senior category exhibited two prominent clusters, each encompassing 100% of users that were successfully clustered, whereas the expert category emerged as the most successful, with the majority of clusters containing 100% of users successfully clustered. This variation in success rates across experience categories could be attributed to the distribution of data within each category. It's worth noting that the junior category had the most abundant data. Conversely, the senior category had a smaller dataset, as individuals with extensive experience are relatively fewer. Consequently, the junior category's larger dataset facilitated more accurate clustering, potentially resulting in higher success rates compared to the senior category. Similarly, the expert category, although smaller in size, had more distinct and well-defined clusters due to the specialization and expertise of its users, potentially contributing to its high success rates.
![image](https://github.com/yael-katsman/Tech_career_roadmap/assets/166139874/08d1168c-97f0-4e88-be21-f3c144d7ff3c)

![image](https://github.com/yael-katsman/Tech_career_roadmap/assets/166139874/9865d5a4-6cdd-4a44-a934-bbd49aacf952)

2.We also evaluated our clustering algorithm based on the average silhouette score for each experience category. This metric offers valuable insights into the quality of our results, as the silhouette score measures the degree of cohesion and separation of data points within their assigned clusters, providing a quantitative assessment of clustering effectiveness. For our junior, senior, and expert experience categories respectively, we obtained the following average silhouette scores: 0.7386, 0.6887 and 0.6666. 

The values above suggest that the clustering quality is highest for users belonging to the junior category, followed by users in the senior category, and then those belonging to the expert category. Overall, while the clustering quality varies slightly across different experience categories, all three of them exhibit relatively high silhouette scores, indicating that the clustering algorithm performs well overall in partitioning users into meaningful clusters.


3.Another metric we employed for evaluating our algorithm was assessing the uniqueness of clusters within each experience category. This is crucial because it helps ensure that the algorithm generates distinct and diverse clusters, ensuring that users within each category are effectively differentiated based on their skills and experience levels.

Our results, as depicted in figure (5)  show that the number of unique clusters fluctuates slightly depending on the number of most frequent skills considered within each cluster. Specifically, in the junior category, we observed the largest variations. Conversely, the senior category consistently maintains 16 unique clusters across varying numbers of skills, ranging from 3 to 8, as does the expert category, spanning from 2 to 8 skills. Notably, across all three categories, we consistently obtained 16 unique clusters when considering the top five most frequent skills, indicating the effectiveness of this threshold in generating distinct clusters
![image](https://github.com/yael-katsman/Tech_career_roadmap/assets/166139874/3812fb46-fa14-449c-abb8-32d85c666729)
## Key findings from our project:
1.For each experience category, distinct clusters exhibited varying skill sets with differences in frequency compared to other clusters. An example of this is presented in figures 6 (a) and 6 (b). The figures depict the clusters that display the most significant dissimilarities from one another within the senior category. 
![image](https://github.com/yael-katsman/Tech_career_roadmap/assets/166139874/947fef03-59e9-4176-a2dd-6e34bb8db403)

2.Regardless of category and clusters, Data remains a relevant and prominent skill amongst successful users in the tech industry. This can be seen in figures 6 (a), 6 (b), as well as figure 7, which represents the skills that appear most frequently across all categories and clusters.

![image](https://github.com/yael-katsman/Tech_career_roadmap/assets/166139874/e39efc97-72d6-4bd5-8bc6-d30f5e7b4a0c)

## Limitations and Reflection: 
Due to budget constraints, we were limited to scraping data for only 4500 users, and after cleaning, we ended up with 3600 users for analysis. Furthermore, we were not able to access the users’ skills directly, but only an approximation for three skills the user possesses. These limitations may have impacted the comprehensiveness of our dataset and influenced the robustness of our findings. 
With a larger dataset and more accurate skills, we could have potentially identified more nuanced patterns and insights. Additionally, the smaller sample size might have affected the generalizability of our results to a broader population, and the lack of skills limited our ability to evaluate our model. Despite these limitations, we made efforts to maximize the utility of the available data and provide meaningful insights.

## Conclusions: 
In conclusion, our project's evaluation revealed strong performance metrics across different experience categories. Notably, junior users benefited from a larger dataset, resulting in accurate clustering, while senior and expert categories showed distinct and well-defined clusters, indicating specialized expertise. Silhouette scores confirmed the algorithm's effectiveness in clustering, while analysis of cluster uniqueness highlighted diverse recommendations. Furthermore, our findings emphasized the enduring importance of data-related skills in the tech industry. Overall, our project provides valuable insights for personalized career guidance, shaping future advancements in AI-driven recommendations.
