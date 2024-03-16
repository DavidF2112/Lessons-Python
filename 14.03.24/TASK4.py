user1 = input("Enetr user1 >> ").strip().lower()
user2 = input("Enetr user2 >> ").strip().lower()
user3 = input("Enetr user3 >> ").strip().lower()
user4 = input("Enetr user4 >> ").strip().lower()

friendships = {
    user1: {user2, user3, user4},
    user2: {user1, user3},
    user3: {user1, user2, user4},
    user4: {user1, user3}
}

print(f"Общие друзя {user1} и {user2}" ,friendships[user1] & friendships[user2] ,
      f"\nОбщие друзя {user1} и {user3}" , friendships[user1] & friendships[user3] ,
      f"\nОбщие друзя {user1} и {user4}" , friendships[user1] & friendships[user4])
print(f"\nОбщие друзя {user2} и {user3}" , friendships[user2] & friendships[user3] ,
      f"\nОбщие друзя {user2} и {user4}" , friendships[user2] & friendships[user4])
print(f"\nОбщие друзя {user3} и {user4}" , friendships[user3] & friendships[user4])
