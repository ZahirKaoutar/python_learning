from tkinter import *
from tkinter import scrolledtext, messagebox
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[-1].split("&")[0]
    return url.split("/")[-1].split("?")[0]

def resumer():
    url = entry_url.get()
    if not url or url == "Colle l'URL YouTube ici":
        messagebox.showerror("Erreur", "Entrez une URL YouTube")
        return
    try:
        btn_resumer.config(text="Chargement...", state=DISABLED)
        fenetre.update()
        video_id = get_video_id(url)
        ytt = YouTubeTranscriptApi()
        transcript = ytt.fetch(video_id)
        texte = " ".join([t.text for t in transcript])
        text_area.delete(1.0, END)
        text_area.insert(END, texte[:3000])
        btn_resumer.config(text="▶  Résumer", state=NORMAL)
    except Exception as e:
        messagebox.showerror("Erreur", str(e))
        btn_resumer.config(text="▶  Résumer", state=NORMAL)

def clear_placeholder(event):
    if entry_url.get() == "Colle l'URL YouTube ici":
        entry_url.delete(0, END)
        entry_url.config(fg="#ffffff")


fenetre = Tk()
fenetre.title("YouTube Résumé")
fenetre.geometry("800x600")
fenetre.configure(bg="#1e1e2e")
fenetre.resizable(False, False)


Label(fenetre, text="🎬 YouTube Transcript", font=("Helvetica", 18, "bold"),
      bg="#1e1e2e", fg="#cba6f7").pack(pady=(20, 5))

Label(fenetre, text="Extrait la transcription d'une vidéo YouTube",
      font=("Helvetica", 10), bg="#1e1e2e", fg="#a6adc8").pack()


frame_url = Frame(fenetre, bg="#1e1e2e")
frame_url.pack(pady=15)

entry_url = Entry(frame_url, width=45, font=("Helvetica", 11),
                  bg="#313244", fg="#a6adc8", insertbackground="white",
                  relief=FLAT, bd=8)
entry_url.insert(0, "Colle l'URL YouTube ici")
entry_url.bind("<FocusIn>", clear_placeholder)
entry_url.pack(side=LEFT, ipady=6, padx=(0, 10))

btn_resumer = Button(frame_url, text="▶  Résumer", font=("Helvetica", 10, "bold"),
                     bg="#cba6f7", fg="#1e1e2e", relief=FLAT, bd=0,
                     padx=12, pady=6, cursor="hand2", command=resumer)
btn_resumer.pack(side=LEFT)

text_area = scrolledtext.ScrolledText(fenetre, width=102, height=16,
                                       font=("Helvetica", 16),
                                       bg="#313244", fg="#cdd6f4",
                                       insertbackground="white",
                                       relief=FLAT, bd=0, padx=10, pady=10)
text_area.pack(padx=20)



fenetre.mainloop()
