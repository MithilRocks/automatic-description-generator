from flask import Flask, request
from duckduckpy import query
import bs4

app = Flask(__name__)

@app.route('/query', methods=['GET'])
def main():
    # get query term
    post_id = request.args.get('id')
    return post_id

    # call to duckduckgo to get results
    # collect all the urls
    # create introductory description out of results
    # create middle description by visiting random urls
    # create bottom description
    # return the result

if __name__ == "__main__":
    app.run(debug=True)