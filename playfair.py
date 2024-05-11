import tkinter as tk
from tkinter import simpledialog

def create_key_grid(keyword):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key_grid = ''
    seen = set()
    
    # Add keyword letters to the grid, skipping duplicates and 'J'
    for char in keyword.upper():
        if char not in seen and char in alphabet:
            seen.add(char)
            key_grid += char
    
    # Add remaining letters of the alphabet
    for char in alphabet:
        if char not in seen:
            key_grid += char
    
    return key_grid

def find_position(char, key_grid):
    index = key_grid.index(char)
    return index // 5, index % 5

def playfair_encrypt(plaintext, key_grid):
    plaintext = plaintext.upper().replace('J', 'I')
    ciphertext = ''
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = ''
        if i+1 < len(plaintext):
            b = plaintext[i+1]
        if a == b or b == '':
            b = 'X'
            i += 1
        else:
            i += 2
        
        row1, col1 = find_position(a, key_grid)
        row2, col2 = find_position(b, key_grid)
        
        if row1 == row2:
            ciphertext += key_grid[row1*5 + (col1+1)%5]
            ciphertext += key_grid[row2*5 + (col2+1)%5]
        elif col1 == col2:
            ciphertext += key_grid[((row1+1)%5)*5 + col1]
            ciphertext += key_grid[((row2+1)%5)*5 + col2]
        else:
            ciphertext += key_grid[row1*5 + col2]
            ciphertext += key_grid[row2*5 + col1]
    
    return ciphertext

def playfair_decrypt(ciphertext, key_grid):
    plaintext = ''
    i = 0
    while i < len(ciphertext):
        a = ciphertext[i]
        b = ciphertext[i+1]
        i += 2
        
        row1, col1 = find_position(a, key_grid)
        row2, col2 = find_position(b, key_grid)
        
        if row1 == row2:
            plaintext += key_grid[row1*5 + (col1-1)%5]
            plaintext += key_grid[row2*5 + (col2-1)%5]
        elif col1 == col2:
            plaintext += key_grid[((row1-1)%5)*5 + col1]
            plaintext += key_grid[((row2-1)%5)*5 + col2]
        else:
            plaintext += key_grid[row1*5 + col2]
            plaintext += key_grid[row2*5 + col1]
    
    return plaintext.replace('X', '')

def main():
    root = tk.Tk()
    root.title("Playfair Cipher GUI")
    
    def encrypt_action():
        keyword = keyword_entry.get()
        plaintext = plaintext_entry.get()
        key_grid = create_key_grid(keyword)
        encrypted_text = playfair_encrypt(plaintext, key_grid)
        result_label.config(text=f'Encrypted: {encrypted_text}')
    
    def decrypt_action():
        keyword = keyword_entry.get()
        ciphertext = plaintext_entry.get()
        key_grid = create_key_grid(keyword)
        decrypted_text = playfair_decrypt(ciphertext, key_grid)
        result_label.config(text=f'Decrypted: {decrypted_text}')
    
    tk.Label(root, text="Keyword:").grid(row=0, column=0)
    keyword_entry = tk.Entry(root)
    keyword_entry.grid(row=0, column=1)

    tk.Label(root, text="Plaintext / Ciphertext:").grid(row=1, column=0)
    plaintext_entry = tk.Entry(root)
    plaintext_entry.grid(row=1, column=1)
    
    encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_action)
    encrypt_button.grid(row=2, column=0)
    
    decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_action)
    decrypt_button.grid(row=2, column=1)
    
    result_label = tk.Label(root, text="Result will appear here...")
    result_label.grid(row=3, column=0, columnspan=2)
    
    root.mainloop()

if __name__ == "__main__":
    main()
