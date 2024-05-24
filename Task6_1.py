# Lesson 6: Python Strings
# 1. Product Review Analysis

def highlight_keywords(reviews):
    keywords = ["good", "excellent", "bad", "poor", "average"]

    for review in reviews:
        review_lower = review.lower()
        for keyword in keywords:
            if keyword in review_lower:
                highlighted_review = review.replace(keyword, keyword.upper())
                print(highlighted_review)
                break

def tally_sentiment(review, positive_words, negative_words):
    review_lower = review.lower()
    positive_count = sum(1 for word in positive_words if word in review_lower)
    negative_count = sum(1 for word in negative_words if word in review_lower)
    return positive_count, negative_count

def create_summary(review, max_length=30):
    if len(review) <= max_length:
        return review
    else:
        last_space = review.rfind(" ", 0, max_length)
        if last_space == -1:
            return review[:max_length] + "..."
        else:
            return review[:last_space] + "..."

# Given product reviews
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

# Given positive and negative words
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# Highlight keywords
highlight_keywords(reviews)

# Tally sentiment
for review in reviews:
    pos_count, neg_count = tally_sentiment(review, positive_words, negative_words)
    print(f"Review: {review}")
    print(f"Positive words count: {pos_count}")
    print(f"Negative words count: {neg_count}")

# Create summaries
for review in reviews:
    summary = create_summary(review)
    print(f"Original review: {review}")
    print(f"Summary: {summary}\n")
