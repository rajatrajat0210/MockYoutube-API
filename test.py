import requests

BASE = "http://127.0.0.1:5000/"

# Sample data
videos = [
    {"likes": 7, "name": "Joe", "views": 50000},
    {"likes": 20, "name": "Bob", "views": 80000},
    {"likes": 40, "name": "Chu", "views": 200000}
]

# --- 1. Add videos ---
print("Adding videos:")
for i, video in enumerate(videos):
    response = requests.put(BASE + f"video/{i}", json=video)
    print(f"PUT /video/{i} =>", response.status_code, response.json() if response.status_code == 201 else response.text)

# --- 2. Try adding a duplicate video ---
print("\nTrying to add duplicate video with ID 0:")
response = requests.put(BASE + "video/0", json=videos[0])
print("Expected 409 Conflict =>", response.status_code, response.text)

# --- 3. Update existing video ---
print("\nUpdating video ID 1 with new views and name:")
response = requests.patch(BASE + "video/1", json={"views": 123456, "name": "Updated Bob"})
print("PATCH /video/1 =>", response.status_code, response.json())

# --- 4. Update non-existing video ---
print("\nUpdating non-existent video ID 100:")
response = requests.patch(BASE + "video/100", json={"views": 500})
print("Expected 404 Not Found =>", response.status_code, response.text)

# --- 5. Get videos ---
print("\nFetching all videos (ID 0 to 2):")
for i in range(3):
    response = requests.get(BASE + f"video/{i}")
    print(f"GET /video/{i} =>", response.status_code, response.json())

# --- 6. Get non-existent video ---
print("\nFetching non-existent video ID 100:")
response = requests.get(BASE + "video/100")
print("Expected 404 Not Found =>", response.status_code, response.text)

# --- 7. Delete a video ---
print("\nDeleting video ID 2:")
response = requests.delete(BASE + "video/2")
print("DELETE /video/2 =>", response.status_code)

# --- 8. Try deleting the same video again ---
print("\nTrying to delete video ID 2 again:")
response = requests.delete(BASE + "video/2")
print("Expected 404 Not Found =>", response.status_code, response.text)

