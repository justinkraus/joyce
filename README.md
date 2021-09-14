# Ulysses Connected
### Clustering the references in *Ulysses* by appearances together.

## Overview
References to external thoughts and ideas are a central component of the classic novel *Ulysses*. In order for modern grasp the novel in its entirety a companion guide is often necessary to provide supplementary detail about the references whose topics focus on literary, physical descriptions of Dublin, and personal incorporations. 

The Joyce Project is an online version of *Ulysses* with hyperlinks to notes that explain the novel's references. Each reference is color-coded to a broad topic and will often reoccur throughout the novel. Below is an example of what a page looks like on the Joyce Project, colored text links to a note.

<img src="/images/jpexample.png" height="30%" width="80%">

### Data
Note text was scraped from The Joyce Project with additional categorial information about the note using these scripts:
[Get Basic Note Info](/nongephi/01_Data/01_note_info.py)  
[Get Note Text](/nongephi/01_Data/02_note_text.py)  
[Cleanup](/nongephi/01_Data/03_note_cleanup.py)  
Data was aggregated into a single table that includes all available information, a portion is shown here:
<img src="/images/notes_table.png" height="25%" width="80%">

Chapters and the references made to each other were [connected using the following script](/nongephi/01_Data/04_edges.py) in order to visualize this information in Gephi.

### Visualization
#### Initial Iterations
Earlier iterations focused on showing how the notes (nodes) contained within each chapter linked to other chapters (edges). However due to the large number of notes and repetition of notes (aka many lines) it became difficult to extract meaning.
<img src="/images/uc_iter1.png" height="40%" width="80%">
In this version large groups represent a chapter, small circles represent a note, colors represent the note theme. Small patterns can be seen but it doesn't reveal meaningful insight.
<img src="/images/uc_iter2.png" height="40%" width="80%">
The chord diagram builds on the earlier version where the perimeter illustrates notes by chapter. Lines do a better job at indicating where certain chapters might share content but it is still not very revealing due to the high number of notes.
#### Final
The final visualization revisits how nodes and edges are created. Each note is connected to another when they occur within the same chapter, stronger weights are assigned to notes that occur in chapters together more often. This snippet of the dataset shows the notes that occur most frequently together.
<img src="/images/notes_table1.png" height="40%" width="80%">

Based on these connections Gephi was able to provide modularity clustering which separated the nodes into five distinct groups as shown in the final visual.
<img src="/images/uc_iter3.png" height="25%" width="80%">

#### Future Thoughts
Patterns between which notes occur with other notes could be improved if groupings smaller than chapters were established. Chapter groupings are too broad, smaller groups would enable more clusters that are consistently referenced with each other.
