# Terminal Commands #

## Directories ##

* List Directory

  * `ls` displays the content of the current directory.

  * `ls -la` lists the detailed contents of the current directory, including hidden files.

* Print Working Directory

  * `pwd` displays the path to the directory you're currently in.

* Change Directory

  * `cd /\<directory>` opens the `/\<directory>` folder. This folder must be present in your current directory.

  * `cd ../` navigates to the parent directory, which is indicated by `../`. This command essentially exits the current folder and brings you to the folder that contains it.

  * `cd ~` navigates to the user's home directory.

* Make Directory

  * `mkdir /\<directory>` makes a new folder with the name `/\<directory>`.

* Remove Directory

  * `rm -r /\<directory>` deletes the folder /`\<directory>` and all the files within it.

* Copy Directory

  * `cp -r /\<sourceDirectory> /\<targetDirectory>`: Copies `/<sourceDirectory>` and its contents into `/\<targetDirectory>`. If there is already a folder named `/\<sourceDirectory>` within `/\<targetDirectory>`, the contents of the folder that was already present will be overwritten by the `/\<sourceDirectory>` you're copying into the folder.

* Move Directory

  * `mv /\<sourceDirectory> /\<targetDirectory>`: Moves `/\<sourceDirectory>` into `/\<targetDirectory>`. This won't work if there is already a folder in `/\<sourceDirectory>` with the name `/\<targetDirectory>`.

  * `mv /\<sourceDirectory> ../`: Moves `/\<sourceDirectory>` into the parent directory. `../` always refers to the parent directory.

## Files ##

* Create File

  * `touch /\<file>` creates a new `/\<file>` in the current directory. Remember to include the file extension. If there's already a file with the name `/\<file>`, it will just update the last modified time of the file.

* Delete File

  * `rm /\<file>` deletes the file with the name `/\<file>`.

* Copy File

  * `cp /\<file> /\<directory>`: Copies the `/\<file>` into the `/\<directory>` folder. If there's already a file named `/\<file>`, the file that's already present will be overwritten by the new `/\<file>` that you're copying in.

* Rename File

  * `mv /\<old-name> /\<new-name>`: Renames a file named `/\<old-name>` into `/\<new-name>`.

* Move File

  * `mv /\<file> /\<directory>`: Moves a file named `/\<file>` into the `/\<directory>` folder. If there's already a file named `/\<file>`, the file that's already present will be overwritten by the new `/\<file>` that you're moving in.

## Utility ##

* Clear Screen

  * `clear`: Clears the terminal screen so that you don't have to sift through the previous inputs.

* Previous Command

  * Use the up arrow to navigate to previous commands that you've used in terminal.

* Tab Completion

  * Use the Tab key to autocomplete the current file or directory you're typing in. If multiple names could be completed from what you've typed, continue typing to the point where the names diverge. You can use tab completion again once you've narrowed down the name that you're typing.

* Closing a Process

  * Ctrl+C (Windows) / Control+C (Mac): Ends the current process that's running in your terminal. This could be the `manual` or `node` or any of the many things that may take up the terminal window.
