import tkinter as tk

news_list = [{"link": "https://www.namibian.com.na/109153/read/Geingob-urges-vaccination", "title": "Geingob urges vaccination", "summary": "PRESIDENT Hage Geingob has urged Namibians to get vaccinated against Covid-19, saying it is the only way to protect themselves and others from the virus."}, {"link": "https://www.namibian.com.na/109152/read/Police-arrest-rape-suspect", "title": "Police arrest rape suspect", "summary": "A 28-YEAR-OLD man was arrested on Wednesday for allegedly raping a 13-year-old girl at Oshakati in the Oshana region."}, {"link": "https://www.namibian.com.na/109151/read/Man-dies-after-being-stabbed-with-broken-bottle", "title": "Man dies after being stabbed with broken bottle", "summary": "A 25-YEAR-OLD man died on Wednesday after he was stabbed with a broken bottle at Okahao in the Omusati region."}]

# Creating a root window
root = tk.Tk()
root.title("News Aggregator")

# Creating a listbox to display the news titles
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Creating a scrollbar for the listbox
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

# Creating a text widget to display the news summary
text = tk.Text(root, width=40, height=10, wrap=tk.WORD)
text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Defining a function to show the summary of the selected news article
def show_summary(event):
    index = listbox.curselection()[0]

    summary = news_list[index]["summary"]

    text.delete(1.0, tk.END)

    text.insert(tk.END, summary)

# Bind the listbox to the function
listbox.bind("<<ListboxSelect>>", show_summary)

# Loop through the news list and insert the titles into the listbox
for news in news_list:
    listbox.insert(tk.END, news["title"])

# Start the main loop
root.mainloop()
