from fastapi import FastAPI


app = FastAPI()
@app.get("/")


def greeting():


    return {"message": "Hello, World from Simra!"}


# echo "# Generative_AI_Quarter_04" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/Coderhubs/Generative_AI_Quarter_04.git
# git push -u origin main
