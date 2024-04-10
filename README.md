# Tech_career_roadmap
Tech Career Roadmap Personalized Guidance for Career Development using LinkedIn
# Overview:
Our project tackles the need for LinkedIn users, particularly those in the tech field, to navigate their career paths effectively. By harnessing artificial intelligence, we've developed a solution that enhances professional portfolios. Unlike conventional methods focused solely on profile presentation, our model identifies skill gaps, recommends tailored learning resources, and offers steps for career advancement. This initiative empowers users to bridge the gap between their current position and career aspirations, fostering efficiency and strategic advantages in professional development.
# System Description:

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
1. To use the Gemini API in this project, you need to authenticate with your API key. Your personal key can be found in: 
   https://ai.google.dev/.

   Copy your key and run the following command in the terminal:

   For Windows:
   ```bash
   set API_KEY=your_api_key
   ```

   For Linux and macOS:
   ```bash
   export API_KEY=your_api_key

   ```
   
3. Run the command:
   ```bash
   python run.py /path/to/user_data.csv model_and_eval.ipynb

   ```
## scraping and cleaning:
### choosing users to scrape:
We utilized the users’ current company and current position, as described in the BrightData- profiles data set to determine if they are considered successful in the tech field
### Scraping and general cleaning:
Due to limitations in accessing users' skills directly in LinkedIn profiles, we resorted to scraping the titles and URLs of videos listed under the “Add new skills with these courses” section, which are tailored to enhance various competencies and closely reflect the actual skill sets of the users, as can be seen in figures (1)+(2) in the appendix. Additionally, we leveraged Bright Data's existing scraper to collect user profile URLs and IDs for identification. 
After collecting the names of the videos we aimed to transform them into meaningful skill names, to do this we employed Geminis API. After passing the names through the API with the prompt “I will provide you a list of video names, for each name write what skill the video teaches in the following format: "video name"@ "your answer":”
Given that some skill names were similar or highly related, we applied K-means Clustering to group them accordingly, representing the skills as TF-IDF vectors. We encountered some problematic clusters that encompassed a wide range of skills without distinctly corresponding to specific skill topics, as can be seen in figure (3) in the appendix. To address this issue, we conducted re-clustering exclusively on the problematic clusters. Additionally, using the Gemini API, we named all clusters, addressing any duplicate names. Finally, we mapped each user’s skills to the corresponding cluster names.
![image](https://github.com/yael-katsman/Tech_career_roadmap/assets/166139874/0955e5a2-d87c-4c3e-b160-dd273417822e)
Figure 1 represents a users recommended skills that appear on her LinkedIn page. Figure 2 represents the users actual skills as presented in her profile. As can be seen, the skills in the two figures highly correspond to one another, with the recommended skills closely reflecting the actual skills. 

## Data analysis:
Our data analysis primarily relied on K-means Clustering, which was applied to both skills and users' degree fields to identify patterns and group them accordingly. Additionally, we visually inspected the clusters to gain insights into their structure and composition.
To create an effective algorithm that would provide recommendations to users based on successful users in their experience level, we categorized users into three groups: junior, senior, and expert. Using figure (a), depicting users' experience distribution, we determined thresholds for each category. Users with less than 100 months of experience were classified as juniors, those with experience ranging from 100 to 250 months were labeled as seniors, and individuals with more than 250 months of experience were considered experts.
For our final algorithm, which utilized K-means clustering, we selected degree fields, course titles, and certification titles, as they offer valuable insights into each user. Skills were omitted from clustering to prioritize recommending new skills that a user can develop, rather than clustering based on existing ones. Figure (b) shows the final clusters in the junior category, represented in two dimensions.
![image](https://github.com/yael-katsman/Tech_career_roadmap/assets/166139874/224fc2c9-8cdc-476c-87be-0e4c73cd3cd3)
## AI Methodologies: 
In our project, we primarily leveraged Geminis API and K-means Clustering. Initially, we employed Geminis API to enhance the informativeness of skill names obtained through web scraping. Subsequently, K-means clustering was applied to the skills dataset, and Geminis API was again utilized to assign meaningful names to the resulting clusters. Furthermore, we conducted K-means clustering on the degree fields data, to reduce sparsity, and once more employed Geminis API for cluster naming, addressing any duplicated clusters. For both attributes, clustering was performed using TF-IDF vectors. 
In our final algorithm, we utilized K-means Clustering and PCA for dimensionality reduction for each experience category. Our feature representation included degree fields, course titles, and certification titles, encoded as multilabel binary vectors. Evaluation of the clusters was conducted using the silhouette score metric. For each category, the optimal value of K was determined to be 16, and PCA was applied with 5 


