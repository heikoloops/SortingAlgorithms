import tkinter as tk
import BubbleSort
import QuickSort
import SelectionSort
import MergeSort
#to set the frame for the visualizer
def sorting(algo, slider, name):
    algo.set_window(name)
    algo.set_data_size(slider.get())
    algo.program_loop()

root = tk.Tk(className=" Sorting Visualizer")
root.geometry("300x300")

bubble_sort = tk.Frame(root)
selection_sort = tk.Frame(root)
quick_sort = tk.Frame(root)
merge_sort = tk.Frame(root)

bubble_sort.grid(row=1, column=1, padx=50, pady=15)
selection_sort.grid(row=2, column=1, padx=50, pady=15)
quick_sort.grid(row=3, column=1, padx=50, pady=15)
merge_sort.grid(row=4, column=1, padx=50, pady=15)


sl1 = tk.Scale(bubble_sort, from_=10, to=200, orient=tk.HORIZONTAL)
sl2 = tk.Scale(selection_sort, from_=10, to=200, orient=tk.HORIZONTAL)
sl3 = tk.Scale(quick_sort, from_=10, to=200, orient=tk.HORIZONTAL)
sl4 = tk.Scale(merge_sort, from_=10, to=200, orient=tk.HORIZONTAL)

b1 = tk.Button(bubble_sort, text="Bubble Sort ", width=10, height=2, command=lambda: sorting(BubbleSort, sl1, "Bubble Sort"))
b2 = tk.Button(selection_sort, text="Selection Sort", width=10, height=2, command=lambda: sorting(SelectionSort, sl2, "Selection Sort"))
b3 = tk.Button(quick_sort, text="Quick Sort", width=10, height=2, command=lambda:  sorting(QuickSort, sl3, "Quick Sort"))
b4 = tk.Button(merge_sort, text="Merge Sort", width=10, height=2, command=lambda: sorting(MergeSort, sl4, "Merge Sort"))

b1.pack(side=tk.LEFT)
b2.pack(side=tk.LEFT)
b3.pack(side=tk.LEFT)
b4.pack(side=tk.LEFT)

sl1.pack(side=tk.RIGHT)
sl2.pack(side=tk.RIGHT)
sl3.pack(side=tk.RIGHT)
sl4.pack(side=tk.RIGHT)
root.mainloop()
