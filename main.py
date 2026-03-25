import datetime
import time
import os
import json

# --- DATA PERSISTENCE ---
DB_FILE = "database.json"

def save_data(posts_list):
    with open(DB_FILE, "w") as f:
        json.dump(posts_list, f, default=str)

def load_data():
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return []

# --- INITIALIZE ---
posts = load_data()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_tos():
    clear()
    print("="*30 + "\n   TERMS OF SERVICE\n" + "="*30)
    print("1. No cussing or inappropriate stuff.\n2. No unauthorized ads.\n3. Ads added by Admin only.")
    if input("\nType 'Agree' to enter: ").lower() != "agree":
        exit()

show_tos()

while True:
    clear()
    print("="*30 + "\n      GLOBAL TOWN SQUARE\n" + "="*30)
    print(" 1. POST\n 2. EXPLORE\n 3. ADMIN\n 4. TOP 3")
    choice = input("\nSelect: ")

    if choice == "1":
        while True:
            n = input("\nHeadline: "); d = input("Description: ")
            posts.append({"id": len(posts)+1, "name": n, "desc": d, "type": "User", "minutes": 0.0, "reviews": [], "created": str(datetime.datetime.now())})
            save_data(posts)
            if input(">> Published! 'x' to go back, Enter to post again: ").lower() == 'x': break

    elif choice == "2":
        if not posts:
            input("\nNo posts! Enter to return..."); continue
        for p in posts:
            clear()
            print(f"FOUND: {p['name']}")
            visit = input("Enter for next / Type 'Go' to enter: ").lower()

            if visit == "go":
                # TIMER STARTS ONLY HERE (Inside the Post)
                post_start_time = time.time() 
                while True:
                    clear()
                    print(f"-- {p['name'].upper()} --\nSTORY: {p['desc']}\n" + "-"*20 + "\nREVIEWS:")
                    for r in p['reviews']: print(f"- {r}")
                    action = input("\nReview or 'leave': ")
                    if action.lower() == "leave": break
                    elif action:
                        p['reviews'].append(action)
                        save_data(posts)

                # TIMER STOPS HERE
                session_duration = (time.time() - post_start_time) / 60
                p['minutes'] += session_duration
                save_data(posts) 
                print(f">> Session: {session_duration:.2f} mins added.")
                input("Press Enter to continue browsing...")
                break 

    elif choice == "3":
        if input("\nPasscode: ") == "Ch1mpsky":
            while True:
                clear()
                print("--- ADMIN ---\n1. Add Ad\n2. Stats\n3. Back")
                adm = input("Choice: ")
                if adm == "1":
                    n = input("Name: "); d = input("Body: ")
                    posts.append({"id": len(posts)+1, "name": n, "desc": d, "type": "Ad", "minutes": 0.0, "reviews": [], "created": str(datetime.datetime.now())})
                    save_data(posts)
                elif adm == "2":
                    print(f"\nTotal Time: {sum(float(p['minutes']) for p in posts):.2f} mins")
                    input("Enter to return...")
                elif adm == "3": break
        else:
            print("Denied."); time.sleep(1)

    elif choice == "4":
        while True:
            clear()
            print("#"*30 + "\n      WORLDWIDE TOP 3\n" + "#"*30)
            trending = sorted(posts, key=lambda x: float(x['minutes']), reverse=True)[:3]
            for i, t in enumerate(trending, 1):
                print(f"{i}. {t['name']} -- ({float(t['minutes']):.2f} mins)")
            if input("\n'x' to go back: ").lower() == 'x': break
