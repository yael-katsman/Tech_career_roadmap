# Tech_career_roadmap
Tech Career Roadmap Personalized Guidance for Career Development using LinkedIn
# Overview:
Our project tackles the need for LinkedIn users, particularly those in the tech field, to navigate their career paths effectively. By harnessing artificial intelligence, we've developed a solution that enhances professional portfolios. Unlike conventional methods focused solely on profile presentation, our model identifies skill gaps, recommends tailored learning resources, and offers steps for career advancement. This initiative empowers users to bridge the gap between their current position and career aspirations, fostering efficiency and strategic advantages in professional development.
# System Description:
# Career Navigator for LinkedIn Users in Tech

Welcome to our project, a cutting-edge solution designed to empower LinkedIn users, especially those within the technology sector, to chart their career paths with confidence and strategy. By harnessing the capabilities of artificial intelligence, our system extends beyond simple profile enhancement, offering a multifaceted approach to professional development.

## Overview

In today's rapidly evolving tech landscape, standing out and staying ahead requires more than just a well-crafted LinkedIn profile. Recognizing this, we've developed a model that not only identifies skill gaps but also provides customized recommendations for learning resources and actionable steps for career advancement. Our goal is to facilitate a seamless transition for users aiming to move from their present roles to their desired career outcomes.

## Key Features

- **Skill Gap Identification**: Utilizing AI, our system efficiently identifies areas where users can grow, ensuring they remain competitive in their field.
- **Personalized Learning Recommendations**: Based on the identified skill gaps, our model suggests relevant courses and certifications, offering a tailored learning experience.
## Our Approach

Leveraging the power of K-means Clustering, we perform comprehensive data analysis to categorize users by experience level (junior, senior, and expert). This allows us to make more personalized and effective recommendations. Our unique algorithm eschews conventional profiling methods in favor of a focus on suggesting new skills to acquire, supported by a detailed analysis of users' degree fields, course titles, and certification titles.

## Getting Started

This repository contains all the necessary code, data analysis notebooks, and documentation to understand and contribute to our project. Whether you're a developer interested in AI and machine learning, a tech industry professional looking for career growth, or simply curious about the future of career navigation on LinkedIn, we invite you to explore our work.

We're excited to share this journey with you and look forward to your contributions and feedback. Together, let's redefine professional development on LinkedIn for the tech community.

# Getting Started:
## Setting up the Development Environment:
Pre-requisites: Git and Anaconda. 

download model_df

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
   python Lab_user_simulation.py <user URL> path/to/model_df (link to model_df drive was submitted in the sumbission box)

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
you can see our full analysis process in model_and_eval.ipynb and run it on collab using the links to expert_df, senior_df, junior_df and model_df
![image](https://github.com/yael-katsman/Tech_career_roadmap/assets/166139874/224fc2c9-8cdc-476c-87be-0e4c73cd3cd3)
## AI Methodologies: 
In our project, we primarily leveraged Geminis API and K-means Clustering. Initially, we employed Geminis API to enhance the informativeness of skill names obtained through web scraping. Subsequently, K-means clustering was applied to the skills dataset, and Geminis API was again utilized to assign meaningful names to the resulting clusters. Furthermore, we conducted K-means clustering on the degree fields data, to reduce sparsity, and once more employed Geminis API for cluster naming, addressing any duplicated clusters. For both attributes, clustering was performed using TF-IDF vectors. 
In our final algorithm, we utilized K-means Clustering and PCA for dimensionality reduction for each experience category. Our feature representation included degree fields, course titles, and certification titles, encoded as multilabel binary vectors. Evaluation of the clusters was conducted using the silhouette score metric. For each category, the optimal value of K was determined to be 16, and PCA was applied with 5 
## Evaluation and Results: 
### We chose to evaluate our project using three different metrics:
you can see our full evaluation process in model_and_eval.ipynb and run it on collab  using the links to expert_df, senior_df, junior_df and model_df
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
## Results: 
Following training, our model engaged with individual users, identifying the cluster most fitting to each based on the proximity of their profiles to existing clusters. Subsequently, the model provided personalized recommendations to each user, comprising five skills, three courses, and three certifications, tailored to advancing their career. These recommendations were curated based on the most frequent features within the identified cluster. Examples of these results are provided in figures 8 (a), (b) and (c). Through these examples, we can observe that the recommendations align closely with the user's existing knowledge and level of expertise, as evidenced by their skills, degree fields, and certifications, ensuring relevance and effectiveness in supporting their professional development journey.

Figure 8 (a) - https://www.linkedin.com/in/joselom23
The user's profile underscores a solid foundation in data analytics, machine learning, and statistical sciences, reflected in their skills, degree field, and completed courses. As a user belonging to the junior category, these recommendations are meticulously tailored to complement their existing expertise and bridge potential skill gaps, aligning closely with their career stage and aspirations. For instance, suggestions like Design Engineering and Test Engineering introduce fundamental concepts essential for professionals with a similar background, while courses and certifications such as artificial intelligence and Machine Learning further enrich their skill set and validate their proficiency in cutting-edge technologies relevant to their domain. Overall, the ![image](https://github.com/yael-katsman/Tech_career_roadmap/assets/166139874/50686471-0601-4270-957d-e0fcba2e50c3)

Figure 8 (b) - https://www.linkedin.com/in/yuan-anne-feng-821a7618
![image](https://github.com/yael-katsman/Tech_career_roadmap/assets/166139874/2fd35161-f28c-481e-b9c4-520a2ead2e87)
The user's profile portrays a seasoned software engineer with extensive experience in Kotlin development and a strong educational background in Electrical Engineering and Related Disciplines. Their involvement in design analysis algorithms and certification as a Unity Certified Developer underscores their expertise. As a user belonging to the senior category, the recommendations are carefully tailored to complement their existing knowledge and senior status. For instance, suggestions such as delving into component design and mastering Java modernization strategies aim to deepen their understanding of engineering principles and lead transformative projects. Similarly, exploring cloud security concepts and advanced AI techniques align with their role in overseeing complex projects and driving innovation. Overall, these recommendations are designed to empower them to remain at the forefront of technological advancements and continue excelling in their career.

Figure 8 (c) - https://www.linkedin.com/in/brent-bryan
![image](https://github.com/yael-katsman/Tech_career_roadmap/assets/166139874/44e0740e-9e4d-4f54-ab6c-cee6611fd433)
As a user belonging to the expert category, with extensive knowledge in cybersecurity and risk management and certifications like CISSP and CISA, the user possesses a deep understanding of IT infrastructure, cloud technologies, and security principles. Recommendations such as IT administration and cloud architecture design leverage their advanced knowledge, enabling them to develop tailored solutions for enterprise-level challenges. Additionally, suggestions like troubleshooting proficiency and risk assessment capitalize on their ability to identify and mitigate security threats effectively. Courses and certifications further enhance their expertise, ensuring they remain at the forefront of industry standards and reinforcing their leadership position in cybersecurity.


## Limitations and Reflection: 
Due to budget constraints, we were limited to scraping data for only 4500 users, and after cleaning, we ended up with 3600 users for analysis. Furthermore, we were not able to access the users’ skills directly, but only an approximation for three skills the user possesses. These limitations may have impacted the comprehensiveness of our dataset and influenced the robustness of our findings. 
With a larger dataset and more accurate skills, we could have potentially identified more nuanced patterns and insights. Additionally, the smaller sample size might have affected the generalizability of our results to a broader population, and the lack of skills limited our ability to evaluate our model. Despite these limitations, we made efforts to maximize the utility of the available data and provide meaningful insights.

## Conclusions: 
In conclusion, our project's evaluation revealed strong performance metrics across different experience categories. Notably, junior users benefited from a larger dataset, resulting in accurate clustering, while senior and expert categories showed distinct and well-defined clusters, indicating specialized expertise. Silhouette scores confirmed the algorithm's effectiveness in clustering, while analysis of cluster uniqueness highlighted diverse recommendations. Furthermore, our findings emphasized the enduring importance of data-related skills in the tech industry. Overall, our project provides valuable insights for personalized career guidance, shaping future advancements in AI-driven recommendations.
