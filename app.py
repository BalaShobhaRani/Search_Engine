import pandas as pd
from flask import Flask, render_template, request
import random

df = pd.read_csv(r"C:\Users\hp\Downloads\search_engine\Search-Engine.csv")

# Fill NaN values in 'Movies&WebSeries' column with an empty string
df['Movies&WebSeries'].fillna('', inplace=True)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_text = request.form.get("search_text")
        if search_text:
            # Filter the DataFrame and handle NaN values in 'Movies&WebSeries' column
            filtered_df = df[df['Subtitles'].str.contains(search_text, case=False, na=False)]
            results = filtered_df['Movies&WebSeries'].tolist()
            random.shuffle(results)  # Randomize the order of results
            top_5_results = results[:5]  # Limit to top 5 results
            return render_template("results.html", search_text=search_text, results=top_5_results)
        else:
            return render_template("results.html", search_text="Nothing", results=None)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
