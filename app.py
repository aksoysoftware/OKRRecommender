from flask import Flask, render_template, request, jsonify
import openai
import sqlite3
import datetime
import smtplib
from email.mime.text import MIMEText

 


app = Flask(__name__)
db = "prod.db"
openai.api_key = '' #uniq open ai key
conn = sqlite3.connect(db)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS historicalOkr (
    cv_id INTEGER PRIMARY KEY,
    name TEXT,
    request_date TEXT,
    background TEXT,
    okr TEXT,
    user_email TEXT,
    manager_email TEXT
);
""")
conn.commit()
messages = [{"role": "system", "content": "You are human resources  "}]


@app.route('/')
def index():
    return render_template('index.html')



def send_email(subject, message, manager_email,historicalValue):
    msg = MIMEText(message + "\n Old data:\n "+historicalValue)
    msg['Subject'] = subject
    msg['From'] = ''#email
    msg['To'] =  manager_email
    try:
        smtp_server = smtplib.SMTP('smtp.office365.com', 587)
        smtp_server.starttls()  
        smtp_server.login(msg['From'] , 'emailpassword')
        smtp_server.send_message(msg)
        smtp_server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Error sending email:", str(e))    


# user_email , manager_email eklendi
def add_okr(user_name, today, user_input, reply, user_email, manager_email):
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO historicalOkr (name , request_date ,background , okr, user_email , manager_email  ) VALUES (?,?,?,?,?,?)",
                       (user_name, today, user_input, reply, user_email, manager_email))
        conn.commit()
        return True

def get_historical_okr(user_name):
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        query = "SELECT name, request_date, background, okr FROM historicalOkr WHERE name = ? ORDER BY request_date DESC LIMIT 1"
        historical_okr = cursor.execute(query, (user_name,))
        historical_okr = cursor.fetchall()
        conn.commit()
        return historical_okr
    
    

@app.route('/generate_okr', methods=['POST'])
def generate_okr():
    user_name = request.json.get('userName')
    user_input = request.json.get('input')
    user_email = request.json.get('userEmail')
    manager_email = request.json.get('managerEmail')

    hr_prompt = (
        "Imagine you are an HR consultant tasked with assisting a company in improving its performance management process. "
        "Design a comprehensive proposal outlining how you will revamp their performance management system. "
        "In your proposal, address the importance of continuous feedback, goal alignment, and employee development. "
        "Explain how you will implement these concepts using modern HR technology and strategic communication. "
        "Emphasize the benefits of your proposed changes in terms of employee satisfaction, productivity, and overall company success."
    )
    okr_recommendation_process = (
        "Your role as an HR consultant is to recommend suitable OKR (Objective and Key Result) choices for employees. Create only 3 okr choices each okr choice 200 character long. "
        "based on the provided information. The employees only understand Turkish, so you should provide the OKR recommendations in Turkish. "
        "You will need to analyze the background details I provide and generate appropriate OKRs using your expertise."
        "We will give you swot analysis of employees for your OKR generation"
        "Also if employees old records exist in our database we can give you some old swot analysis of employees"
        "If old analysis is not available we will inform you like this 'Old Swot Analysis : [],' "
        "After this step we will give you new swot analysis of employees like this New Swot : []"
        "Create only 200 chracters response and generate only 3 okr choice for each request. I will give each employee equals okr's"
    )
    employee_backgrounds = "Employee background information in Turkish."
    historicalValues = get_historical_okr(user_name)
    
    if (historicalValues):
        historicalValue = '\n'.join(
            [', '.join(map(str, row)) for row in historicalValues])
    else:
        historicalValue = "[]"
    openai_prompt = (
        hr_prompt
        + "\n\n"
        + okr_recommendation_process
        + "\n\n"
        + "Your task is to recommend suitable OKRs for the following employee backgrounds:\n"
        + "New Swot : " + user_input
        + "\n\n"
        + employee_backgrounds
    )
    today = datetime.datetime.today()
    if (openai_prompt):
        messages.append({"role": "user", "content": openai_prompt})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = chat.choices[0].message['content']
        messages.append({"role": "assistant", "content": reply})
        subject = "Your OKR Results"
        user_message = f"Hello {user_name},\n\nHere are your OKR results:\n\n{reply}"
        manager_message = f"Hello Manager,\n\n{user_name} has generated OKRs. Here is the OKR:\n\n{reply}"
        send_email(subject, user_message,  user_email,historicalValue)
        send_email(subject, manager_message, manager_email,historicalValue)
        add_okr(user_name, today, user_input, reply,user_email, manager_email )

        return jsonify({"response": reply})
    else:
        return jsonify({"response": "Please provide input."})


if __name__ == 'main':
    app.run(debug=True)