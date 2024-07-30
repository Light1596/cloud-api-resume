# Cloud API Resume Project
Welcome to the Cloud API Resume project! This project aims to create a serverless function that fetches resume data stored in a NoSQL database and returns it in JSON format. Additionally, GitHub Actions is integrated to automatically deploy updates to your cloud serverless function whenever you push to your repository.

# ARCHITECTURE DIAGRAM
![cloud resume api - Page 4 (1)](https://github.com/user-attachments/assets/604ad0ac-bc9e-4725-9e39-b8b2ada245f2)

## Project Overview

The key requirements for this project are:
- **NoSQL Database**: Containing sample resume data.
- **Serverless Function**: Fetch and return resume data.
- **GitHub Actions**: Automatically package and deploy your serverless function on every push to the repository.

## How It Works

1. **NoSQL Database**: The resume data is stored in a DynamoDB table named `Resumes`.
2. **Serverless Function**: An AWS Lambda function fetches the resume data from the DynamoDB table and returns it in JSON format.
3. **GitHub Actions**: A CI/CD pipeline is set up using GitHub Actions to automatically deploy the serverless function to AWS Lambda whenever changes are pushed to the repository.

## Features

- **Serverless Architecture**: Leverage AWS Lambda for a scalable and cost-effective serverless solution.
- **Automated Deployment**: GitHub Actions ensures continuous integration and deployment, making the development process efficient and streamlined.
- **NoSQL Database**: Utilize AWS DynamoDB for fast and flexible NoSQL data storage.

## Setup and Deployment

### Prerequisites

- AWS account with access to Lambda and DynamoDB.
- AWS CLI configured with appropriate credentials.
- GitHub account.

### Steps to Set Up and Deploy

1. **Clone the Repository**

    ```sh
    git clone https://github.com/Light1596/cloud-api-resume.git
    cd cloud-api-resume
    ```

2. **Create DynamoDB Table**

    Create a DynamoDB table named `Resumes` with `id` as the primary key. Add sample resume data to the table.

3. **Configure AWS Credentials**

    Add your AWS credentials as GitHub Secrets:
    - `AWS_ACCESS_KEY_ID`
    - `AWS_SECRET_ACCESS_KEY`
    - `AWS_REGION`
    - `TABLE_NAME`

4. **Create GitHub Secrets**

    Navigate to your repository on GitHub, go to `Settings` > `Secrets and variables` > `Actions`, and add the following secrets:
    - `AWS_ACCESS_KEY_ID`
    - `AWS_SECRET_ACCESS_KEY`
    - `AWS_REGION`
    - `TABLE_NAME`

5. **GitHub Actions Workflow**

    The GitHub Actions workflow (`.github/workflows/deploy.yml`) is already set up in the repository. This workflow will:
    - Install AWS CLI.
    - Package the Lambda function.
    - Deploy the Lambda function to AWS.

6. **Push Changes**

    Any changes pushed to the `main` branch will trigger the GitHub Actions workflow to deploy the updated Lambda function.

### API Endpoints

#### GET /resume

Fetches the resume data from the DynamoDB table and returns it in JSON format.

**Request**

```sh
(https://bq2oum8yzi.execute-api.us-east-1.amazonaws.com/light)
```
## Follow me
You can contact via [LinkedIn](https://www.linkedin.com/in/light-situma-35b522166/)
## Conclusion

This project demonstrates how to build a serverless application using AWS Lambda and DynamoDB, with automated deployment using GitHub Actions. By following the setup steps, you can easily deploy your own serverless function to fetch and return resume data in JSON format.

# Cloud Resume API Challenge
This project is a solution to the [Cloud Resume API Challenge](https://cloudresumeapi.dev/), created by [Rishab Kumar](https://github.com/rishabkumar7).
