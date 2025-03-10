import requests


access_token = "EAAOEdcV6NY8BOZBrNNucwV8VBEccuZBfvqCQrQzeoB0h6MFoWBg7ZCRyGTuZCaBiPSpBdQ3GdLPl0ZBdRgVD7CarItE6mhhjMOTdAiNr3xrLpmonXOHwHHMXOzevNfW84RjMlM9fMY9wERA8QFdLDlRyIpF8gSSZBJB4HD53IdlxJxugq7cIYbcvfnngiqpwIa9huyOHMXUmaXNW4vaWCnheiCJY0gE3W1vkZBHcJmll3DZBq4CTQcSU"


url = f"https://graph.facebook.com/me?fields=id,name,email,picture&access_token={access_token}"
response = requests.get(url)
print(response.json())

