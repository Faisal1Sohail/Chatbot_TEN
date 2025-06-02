
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key='your_secret_key')

templates = Jinja2Templates(directory="templates")

# Questions and answers
questions = {
    0: "👋 Hello! I'm here to assist you with questions about The Entrepreneurship Network.",
    1: "What is the name of the company?",
    2: "What products or services does the company 💬 offer?",
    3: "Where is the company headquartered?",
    4: "How do I apply for an internship 👈 ?",
    5: "What is Pay After Placement?",
    6: "How does Pay After Placement work?",
    7: "Can I see a list of 📚 courses available for beginners?",
    8: "Can I choose how long I take to repay?",
    9: "Who is your target audience or ideal customer?",
    10: "What are the company’s key values or principles?",
    11: "What are the main goals for the company in the next few years?",
    12: "How has the company adapted to market trends?",
    13: "What internships do you offer ⚡ ?",
    14: "Free site for education?",
    15: "Free site for mentorship?",
    16: "Free site for resume building?",
    17: "Free site for influencer marketing?",
    18: "Free site for training?",
    19: "Free site for AI tools?",
    20: "Free site for idea to expansion?"
}

answers = {
    "What is the name of the company?": "The Entrepreneurship 😊 Network",
    "What products or services does the company offer?": "We provide education 🎓 , mentorship, training, and knowledge 👩‍💻 about AI tools...",
    "Where is the company headquartered?": "Delhi, India",
    "How do I apply for an internship?": "You can apply here 👉 : https://career.entrepreneurshipnetwork.net/",
    "What is Pay After Placement?": "Pay After Placement 💸 is a model where students pay after securing a job.",
    "How does Pay After Placement work?": "No upfront fees. Repayment starts after securing a job with a minimum salary threshold.",
    "Can I see a list of courses available for beginners?": "Check them out 👉 : https://ten-official.vercel.app/Courses",
    "Can I choose how long I take to repay?": "Repayment is usually pre-defined but may vary.",
    "Who is your target audience or ideal customer?": "Aspiring entrepreneurs, developers, and students.",
    "What are the company’s key values or principles?": "Innovation, ⚡ mentorship, and empowering entrepreneurs.",
    "What are the main goals for the company in the next few years?": "Expand services, enhance tech, and build partnerships.",
    "How has the company adapted to market trends?": "By evolving services and staying current with trends.",
    "What internships do you offer?": "Frontend, Android, MERN Stack, Python, Backend.",
    "Free site for education?": "👉 https://www.entrepreneurshipnetwork.net/",
    "Free site for mentorship?": "👉 https://mentor.entrepreneurshipnetwork.net/",
    "Free site for resume building?": "👉 https://resume.entrepreneurshipnetwork.net/",
    "Free site for influencer marketing?": "👉 https://www.entrepreneurshipnetwork.net/Influencer_Marketing",
    "Free site for training?": "👉 https://hrportal.entrepreneurshipnetwork.net/",
    "Free site for AI tools?": "👉 https://ailabs.entrepreneurshipnetwork.net/",
    "Free site for idea to expansion?": "👉 https://ideaengine.entrepreneurshipnetwork.net/",
    "Hello! I'm here to assist you with questions about The Entrepreneurship Network": "You can ask about the company 😊 , its services, Pay After Placement, internships, and more."
}

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    request.session.clear()
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    user_message = data.get("message", "").strip()

    if user_message.lower() == "hello":
        response = "Hello! I'm here to assist you with questions about The Entrepreneurship Network."
        should_close = False
    elif user_message.lower() == "quit":
        response = "Thank you for using the chatbot. Goodbye!"
        should_close = True
    else:
        response = answers.get(user_message, "I'm sorry 😑 , I didn't understand that. Please ask about The Entrepreneurship Network.")
        should_close = False

    return JSONResponse(content={"response": response, "should_close": should_close})

@app.get("/questions")
async def get_questions():
    return JSONResponse(content={"questions": list(questions.values())})
