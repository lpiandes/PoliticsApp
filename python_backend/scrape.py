import openai
import requests

openai.api_key = "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"

def get_political_info(name):
    prompt = f"Provide detailed information about the political party and key political ideas of {name}. Focus on their stance on major political issues."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()
    except openai.error.OpenAIError as e:
        print(f"Error retrieving political information: {e}")
        return "N/A"

# Function to query an API or news site for recent news
def get_recent_news(name):
    # Example using NewsAPI (replace with your preferred news API)
    news_api_key =  "d4641ec81e1d4812a73f60ec6976acda"
    url = f"https://newsapi.org/v2/everything?q={name}&sortBy=publishedAt&apiKey={news_api_key}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        news_data = response.json()

        if news_data['status'] == 'ok':
            articles = news_data.get('articles', [])
            if articles:
                return "\n\n".join([f"{article['title']} - {article['source']['name']}\n{article['url']}" for article in articles[:5]])
            else:
                return "No recent news found."
        else:
            return "Error retrieving news data."
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news data: {e}")
        return "N/A"

# Aggregation and display of information
def aggregate_and_display_info(name):
    political_info = get_political_info(name)
    recent_news = get_recent_news(name)

    print(f"Name: {name}")
    print("\nPolitical Information:")
    print(political_info)
    print("\nRecent News:")
    print(recent_news)

# Main function to prompt user input and retrieve data
def main():
    search_name = input("Enter the name of the politician you want to search for: ").strip()
    aggregate_and_display_info(search_name)

if __name__ == "__main__":
    main()