CREATE DATABASE IF NOT EXISTS Resume;
USE Resume;

CREATE TABLE IF NOT EXISTS Resume_Screening (
    Resume_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Skills TEXT,
    `Experience (Years)` FLOAT,
    Education VARCHAR(100),
    Certifications TEXT,
    `Job Role` VARCHAR(100),
    `Recruiter Decision` VARCHAR(20),
    `Salary Expectation ($)` FLOAT,
    `Projects Count` INT,
    `AI Score (0-100)` FLOAT,
    Recruiter_Decision_Encoded INT
);


-- Hiring Rate Percentage
SELECT 
    COUNT(*) AS Total_Candidates,
    SUM(Recruiter_Decision_Encoded) AS Total_Hired,
    (SUM(Recruiter_Decision_Encoded) / COUNT(*)) * 100 AS Hiring_Percentage
FROM Resume_Screening;


-- Average AI Score by Recruiter Decision
SELECT 
    `Recruiter Decision`,
    AVG(`AI Score (0-100)`) AS Avg_AI_Score
FROM Resume_Screening
GROUP BY `Recruiter Decision`;


-- Hiring Rate by Job Role
SELECT 
    `Job Role`,
    COUNT(*) AS Total_Applicants,
    SUM(Recruiter_Decision_Encoded) AS Total_Hired,
    (SUM(Recruiter_Decision_Encoded) / COUNT(*)) * 100 AS Hiring_Rate
FROM Resume_Screening
GROUP BY `Job Role`
ORDER BY Hiring_Rate DESC;
