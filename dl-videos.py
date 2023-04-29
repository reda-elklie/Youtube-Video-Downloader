import pafy

url = input("Enter the YouTube video URL: ")
video = pafy.new(url)
best = video.getbest()

filename = best.download(filepath="./")

print(f"Video saved as {filename}")
