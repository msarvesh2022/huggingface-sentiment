from flask import Flask, render_template_string, request
from transformers import pipeline

app = Flask(__name__)
pipe = pipeline("text-classification", model="tabularisai/multilingual-sentiment-analysis", truncation=True)

HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Sentiment Analysis</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body { background: #f8fafc; }
    .container { max-width: 600px; margin-top: 60px; }
    .card { box-shadow: 0 2px 12px rgba(0,0,0,0.07); }
    textarea { resize: vertical; }
  </style>
</head>
<body>
  <div class="container">
    <div class="card">
      <div class="card-body">
        <h2 class="card-title text-center mb-4">Sentiment Analysis</h2>
        <form method="post">
          <div class="mb-3">
            <label for="review" class="form-label">Enter your review:</label>
            <textarea class="form-control" id="review" name="review" rows="5" placeholder="Type your review here...">{{ review or '' }}</textarea>
          </div>
          <div class="d-grid gap-2">
            <button type="submit" class="btn btn-primary btn-lg">Analyze</button>
          </div>
        </form>
        {% if result %}
        <div class="alert alert-info mt-4" role="alert">
          <h5 class="alert-heading">Result</h5>
          <hr>
          <p><b>Label:</b> <span class="badge bg-success">{{ result[0]['label'] }}</span></p>
          <p><b>Score:</b> <span class="badge bg-secondary">{{ '{:.2f}'.format(result[0]['score']) }}</span></p>
        </div>
        {% endif %}
      </div>
    </div>
    <footer class="text-center mt-4 text-muted">
      <small>Powered by HuggingFace Transformers &middot; <a href="https://huggingface.co/tabularisai/multilingual-sentiment-analysis" target="_blank">Model Info</a></small>
    </footer>
  </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    review = ''
    if request.method == 'POST':
        review = request.form.get('review', '')
        if review.strip():
            result = pipe(review)
    return render_template_string(HTML_TEMPLATE, result=result, review=review)

if __name__ == '__main__':
    app.run(debug=True)