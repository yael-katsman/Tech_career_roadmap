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
    git clone https://github.com/hillysegal1/plant-interactive-model
    ```
2. ### Create and activate the conda environment
   After cloning the repository, navigate into the project directory:
    ```bash
    cd plant-interactive-model
    ```
    Then, use the following command to create a conda environment from the environment.yml file provided in the project:
    ```bash
    conda env create -f environment.yml
    ```
    Activate the environment with the following command:
   ```bash
    conda activate plant_system_env
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
   streamlit run app.py 
   ```
