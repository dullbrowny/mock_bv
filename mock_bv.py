from flask import Flask, jsonify, request

app = Flask(__name__)

mock_reviews = [{"id": 1, "productId": "PRODUCT_ID", "rating": 5, "title": "Amazing product", "text": "Highly recommend", "userId": "USER_ID"}]

@app.route('/cv2/reviewpreview', methods=['GET'])
def mock_review_preview():
    return jsonify({"productId": request.args.get('Filter'), "reviewPreview": "This is a preview of the review."})

@app.route('/cv2/reviewstats', methods=['GET'])
def mock_review_stats():
    return jsonify({"productId": request.args.get('Filter'), "averageRating": 4.5, "reviewCount": 100})

@app.route('/cv2/reviewsubmit', methods=['POST'])
def mock_review_submit():
    return jsonify({"status": "success", "review": request.json})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
