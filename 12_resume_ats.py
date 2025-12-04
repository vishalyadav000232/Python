# Job Description  skills for industies Requirment

job_skills = "Python Machin Learning NLP , Sql Deep learning"

resume_text = """have experience in Python and Deep learning.
I also worked in NLP projects using SQL databases"""
resume = resume_text.lower()


# Extract the matching skills 

matched = [skill for skill in job_skills if skill in resume]

score = len(matched) *len(job_skills)/100


print("\n✅ Matched Skills:", matched)
print(f"🎯 Resume Match Score: {score}%")

count = job_skills.count("a")
print(count)