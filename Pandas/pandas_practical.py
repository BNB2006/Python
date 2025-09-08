import pandas as pd

cars = {
    "Car": ["Honda", "Toyota", "Ford", "BMW"],
    "Model": ["Civic", "Corolla", "Mustang", "X5"],
    "Price": [20000, 18000, 35000, 60000]
}

df_cars = pd.DataFrame(cars)
print("\n\nCars DataFrame ->")
print(df_cars)

df_sorted = df_cars.sort_values(by="Price", ascending=True)
print("\nAfter sorting ->")
print(df_sorted)



# 3) Handle Missing Data in DataFrame
mobiles = {
    "Brand": ["Samsung", "Apple", "OnePlus"],
    "Model": ["S23", "iPhone 14", None],
    "Price": [70000, None, 30000]
}

df_mobiles = pd.DataFrame(mobiles)
print("\nMobile Dataframe ->")
print(df_mobiles)

# --- Method 1: dropna() ---
df_dropna = df_mobiles.dropna()
print("\nResult after using dropna() :")
print(df_dropna)

# --- Method 2: fillna() ---
df_filled = df_mobiles.fillna({
    "Model": "Unknown",
    "Price": df_mobiles["Price"].mean()   # replace missing price with average
})
print("\nResult after using fillna() :")
print(df_filled)
