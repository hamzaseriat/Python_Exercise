capitals = {
    "Afghanistan": "Kabul",
    "Albania": "Tirana",
    "Algeria": "Algiers",
    "Canada": "Ottawa",
    "China": "Beijing",
    "Norway": "Oslo",
    "USA": "Washington, D.C",

}
if __name__ == "__main__":
  
  if capitals.get("USA"):
    print("The capital of USA is:", capitals["USA"])
  else:
    print("The capital of USA is not found in the dictionary.")

capitals.update({"Germany": "Berlin"})
print("The capital of Germany is:", capitals["Germany"])

print(f"All capitals in the dictionary:")
print(capitals)
capitals.pop("Algeria")
print(capitals)

values = capitals.values()
print("All capital values in the dictionary:")
print(values)