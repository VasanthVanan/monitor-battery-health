# Python App to Monitor Mac's Battery Health

Apple states: 
> "Batteries have a limited amount of charge cycles before their performance is expected to diminish. Once the cycle count is reached, a replacement battery is recommended to maintain performance. You can use your battery after it reaches its maximum cycle count, but you might notice a reduction in your battery life."

---

## Introduction:

This python script constantly monitors the battery usage of your Macbook (every 10 minutes; can be customized based on your need). 

- notifies & dictates if significant energy is being used,

- notifies if charges are past 80% (charging till 100% reduces your mac's battery life over time, don't ever do that!)

- provides analysis on the number of lasting days for each battery capacity

- displays the current cycle count (Automation App)

- creates a log for future observations

---

## Installation:

1. Clone the repository to your mac: 
     ```bash
     git clone https://github.com/VasanthVanan/monitor-battery-health.git
     ```
2. Change into the project directory:
    ```bash
    cd monitor-battery-health
    ```
3. Install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```
4. follow the instruction: [User Manual Document](https://github.com/VasanthVanan/monitor-battery-health/blob/main/user-manual.pdf)

## Screenshots:

* Notifies if charges are past 80% 
 <br>![Image 1](/images/image-2.png)
* Notifies if charge goes down to 1% 
 <br>![Image 2](/images/image-1.png)
* Notifies if significant battery energy is used 
 <br>![Image 3](/images/image-3.png)
* Automation App: Notification 
 <br>![Image 4](/images/image-4.png)
* Pushover Notification 
 <br>![Image 5](/images/image-5.png)

## Closing thoughts:

I've been using this script for years and it showed good results. Hereby, I wanted to share it with all the other Macbook users who are concerned about their battery health. Try it out and let me know your thoughts! 

Email: cr34u6rupg@pomail.net<br>
Instagram: <a href="https://www.instagram.com/vasanth_vanan">@vasanth_vanan</a>


