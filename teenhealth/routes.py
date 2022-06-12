from flask import render_template
from teenhealth.__init__ import app
from teenhealth import prompts

@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html', title="About")
# render about page when route is / or /about

@app.route('/info')
def info():
    return render_template('info.html', title="Info")

@app.route('/reflection')
def reflection():
    prompt = prompts.pick_prompt()
    #pick question
    category = prompts.find_category(prompt)
    #find category
    info = prompts.find_info(category)
    #find information associated with each category
    return render_template('reflection.html', title="Reflection", instr = prompts.pick_instr(), prompt=prompt, category=category, info=info)

@app.route('/rant')
def rant():
    return render_template('rant.html', title="Rant")