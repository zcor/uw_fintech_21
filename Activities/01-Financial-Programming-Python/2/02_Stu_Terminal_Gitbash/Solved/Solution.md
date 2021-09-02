# Getting Familiar with the Terminal

In this activity, we'll practice a bit more with terminal commands.

## Solution

1. Navigate to your `FinTech_Workspace` folder, as shown in the following image:

    ![In the terminal, the user has navigated into the FinTech_Workspace folder.](Images/01.png)

2. Use the `ls` command to see the contents of that folder, as shown in the following image:

    ![A red arrow calls attention to the ls command in the terminal, listing Module-1 beneath it.](Images/02.png)

3. Use the `pwd` command to find the current path you're in, as shown in the following image:

    ![A red arrow calls attention to the pwd command in the terminal, listing FinTech_Workspace beneath it.](Images/03.png)

4. In `FinTech_Workspace`, create a new directory named `Activity-1`. Then list the contents of the current directory again to make sure it worked. You should see something like the following image:

    ![A red arrow points at the mkdir command, creating Activity-1 directory. Another red arrow points at the ls command below.](Images/04.png)

5. Navigate into the directory you just created. `Activity-1`, as shown in the following image:

    ![A red arrow calls attention to the cd command in the terminal, showing that the user has navigated into Activity-1.](Images/05.png)

6. Create a new file named `hello.md`. List the contents of the current directory again. You should see something like the following image:

    ![A red arrow points to "touch hello" in the terminal. Another red arrow points to the ls command, listing hello.md below.](Images/06.png)

7. Rename the `hello.md` file to `coding.md`, as shown in the following image:

    ![A red arrow points to command "mv hello.md coding.md" in the terminal. Below, coding.md is now listed in contents.](Images/07.png)

8. Inside the `Activity-1` directory, create a new directory named `terminal`, as shown in the following image:

    ![A red arrow points at "mkdir terminal". The ls command reveals the contents as coding.md and terminal.](Images/08.png)

9. Move the `coding.md` file into the `terminal` folder you just made. Navigate into the terminal folder to confirm that the file has been moved. You should see something like the following image:

    ![A red arrow points to command "mv coding.md terminal". Then cd terminal navigates into that directory.](Images/09.png)

10. Delete the `terminal` folder. Note that you have to move up a directory to `Activity-1` before you can delete the terminal directory. You cannot delete a directory that you're currently in. You should see something like the following image:

    ![Red arrows point to the following commands: "cd ..", "ls", "rm -r terminal", and "ls" again.](Images/10.png)

11. Delete the `Activity-1` folder. Again, note that you have to move up a directory to `FinTech_Workspace` before you can delete the Activity-1 directory. You should see something like the following image:

    ![Red arrows point to the following commands: "cd ..", "rm -r Activity-1", and "ls".](Images/11.png)

## Hints

Use the terminal cheat sheet to determine which terminal commands should be used for each step.
