
import tkinter as tk
from model import PerceptronSpamFilter

def classify():
    email = email_text.get("1.0", tk.END)
    weights = [
        float(w1.get()),
        float(w2.get()),
        float(w3.get()),
        float(w4.get())
    ]
    bias_val = float(bias.get())
    
    model = PerceptronSpamFilter(weights, bias_val)
    pred, features, score = model.predict(email)
    
    result_var.set(f"Features: {features}\nScore: {score:.2f}\nPrediction: {'SPAM' if pred==1 else 'NOT SPAM'}")

root = tk.Tk()
root.title("Smart Email Spam Filter")

tk.Label(root, text="Enter Email:").pack()
email_text = tk.Text(root, height=6, width=50)
email_text.pack()

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="w_free").grid(row=0,column=0)
tk.Label(frame, text="w_offer").grid(row=0,column=1)
tk.Label(frame, text="w_length").grid(row=0,column=2)
tk.Label(frame, text="w_link").grid(row=0,column=3)
tk.Label(frame, text="bias").grid(row=0,column=4)

w1 = tk.Entry(frame); w1.insert(0,"2")
w2 = tk.Entry(frame); w2.insert(0,"2")
w3 = tk.Entry(frame); w3.insert(0,"0.05")
w4 = tk.Entry(frame); w4.insert(0,"3")
bias = tk.Entry(frame); bias.insert(0,"-3")

w1.grid(row=1,column=0)
w2.grid(row=1,column=1)
w3.grid(row=1,column=2)
w4.grid(row=1,column=3)
bias.grid(row=1,column=4)

tk.Button(root, text="Classify Email", command=classify).pack(pady=5)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, justify="left").pack()

root.mainloop()
