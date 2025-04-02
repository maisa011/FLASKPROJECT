from flask import Flask, render_template

from markupsafe import Markup
import plotly.graph_objects as go


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", username=name)

@app.route('/interactive')
def interactive_chart():
    x = ['იანვარი', 'თებერვალი', 'მარტი']
    y = [1200, 1500, 900]

    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    graph_html = fig.to_html(full_html=False)

    return render_template("interactive.html", chart=Markup(graph_html))

@app.route('/weather')
def weather():
    return render_template("weather.html")

if __name__ == "__main__":
    app.run(debug=True)
