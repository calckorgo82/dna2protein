Hello! This is a user's manual on how to use the flask application that I have created, DNA2Protein!

I have created a folder called "final," which contains all of the files necessary to compile, configure, and use my project. Inside the folder, I have the markdown files, which contain this file, as well as the DESIGN.md file that explains the technical aspects of my project. It also contains the application.py that has python code for my flask application. The static folder contains all of the images that I have used and the "styles.css" file that I used to add stylistic elements to my web application. The next folder is the templates folder, which contains the .html files that corresponds to different pages of the web application. Lastly, I have the test files, where I have added 7 different .txt files containing DNA sequences for you to test my web application with.

To start using the actual application, you need to go into the "final" directory, and run flask. Then, using the link provided by the CS50 IDE, it will direct you to the main page of my web application, where it says "DNA2PROTEIN" in a large font. On the bottom of the page, you can see visually how my program works! I will first transcribe the DNA to mRNA, and then translate the mRNA to protein. To actually use the program, you should see a form box with the label, "DNA sequence." In that box, you just need to plug in the DNA sequence that I have provided for you in the test files, or find a DNA sequence of your choice and input it into the box. Once you press "generate," you will be able to see the result page. On the top of the result page, you can see what your mRNA sequence was based on your DNA sequence input. Under that, you will see a highlighted row in the middle of the page. This is the first protein that was detected in your DNA sequence. If you are curious about how each amino acid looks in terms of its structures or if you want to know more about their features, please refer to the diagram on the bottom. Here, it gives you the chemical structures and groups them based on polarity and side chains.

Also, if you happen to input an invalid DNA sequence, such as putting a different character other than "A, G, C, or T," then it will direct you to an error page. You would just need to press back on your browser to return to the main page and resubmit a valid sequence. Another possibility for an error is when the sequence that you provide does not have a start codon. This means that there is no protein that can be synthesized using the sequence that you provided, and you would see an error message that says "There is no indication of a start codon!" Similarly to the last error, you just need to press back and resubmit a new sequence that is valid. Thank you for your time to use my program!

link to YouTube Video: https://youtu.be/4luiVMkNTfE