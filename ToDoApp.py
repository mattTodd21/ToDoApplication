import tkinter as tk

class Task:
    def __init__(self, description):
        self.description = description
        self.is_completed = False

    def complete_task(self):
        self.is_completed = True

class ToDoAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.tasks = []
        
        self.layout = tk.Frame(root, padx=15, pady=15)
        self.layout.pack()
        
        self.task_input_field = tk.Entry(self.layout, width=30)
        self.task_input_field.insert(0, "Enter a new task")
        self.task_input_field.pack()
        
        self.add_task_button = tk.Button(self.layout, text="Add Task", command=self.add_task)
        self.add_task_button.pack()
        
        self.task_listbox = tk.Listbox(self.layout, selectmode=tk.SINGLE, width=40)
        self.task_listbox.pack()
        
        self.complete_task_button = tk.Button(self.layout, text="Complete Selected Task", command=self.complete_selected_task)
        self.complete_task_button.pack()
        
    def add_task(self):
        description = self.task_input_field.get()
        if description.strip():
            task = Task(description)
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, description)
            self.task_input_field.delete(0, tk.END)
    
    def complete_selected_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            selected_task = self.tasks[index]
            selected_task.complete_task()
            self.task_listbox.itemconfig(index, {'bg': 'light gray'})

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoAppGUI(root)
    root.mainloop()
