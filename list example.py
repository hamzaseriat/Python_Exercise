stocks = []

def adding():
    add = input("Please enter your Material to add: ")
    stocks.append(add)
    print(f"'{add}' successfully added!")

def remove():
    remove_item = input("Please enter full name of material which you remove: ")
    # Çökmemesi için önce listede var mı diye kontrol ediyoruz
    if remove_item in stocks:
        stocks.remove(remove_item)
        print(f"'{remove_item}' successfully removed!")
    else:
        print("This item is not in your list!")

def seeItems():
    if not stocks: # Liste boşsa uyarı ver
        print("Your list is currently empty.")
    else:
        print("\n--- Current Stocks ---")
        for index, item in enumerate(stocks, start=1):
            print(f"{index}. {item}")
        print("----------------------")

def main():
    while True: # Programın sürekli çalışması için döngü ekledik
        print("\nPlease Enter which activity do you want")
        print("1. adding")
        print("2. Remove")
        print("3. seeItems")
        print("4. Exit") # Çıkış seçeneği eklemek iyi bir pratik
        
        chose = int(input("Your choice: "))
        
        # Seçim kontrolü (1, 2, 3 veya 4 değilse)
        while chose < 1 or chose > 4:
            print("Invalid choice. Again")
            chose = int(input("Your choice: "))
            
        # Girintileri (indentation) hizaladık
        if chose == 1:
            adding()
        elif chose == 2:
            remove()
        elif chose == 3:
            seeItems()
        elif chose == 4:
            print("Goodbye!")
            break # Döngüden çıkar ve programı bitir

# Programı başlatan tetikleyici
main()