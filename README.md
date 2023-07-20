# Python App to Monitor Mac's Battery Health

Apple states: 
> "Batteries have a limited amount of charge cycles before their performance is expected to diminish. Once the cycle count is reached, a replacement battery is recommended to maintain performance. You can use your battery after it reaches its maximum cycle count, but you might notice a reduction in your battery life."

---

## Introduction:

This python script constantly monitors the battery usage of your Macbook (every 10 minutes; can be customized based on your need). 

- notifies & dictates if significant energy is being used,

- notifies if charges are past 80% (charging till 100% reduces your mac's battery life over time, don't do that!)

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
 <br>![Image 1](https://lh3.googleusercontent.com/pw/AIL4fc_zbMoV0wq5f1eKAXjC9CIlwxe332oDHrLYNuodCViNey4kvcRyjZrgCa962kfL0P93zL8FeOfT4wJ0pKX2fCBG_RKXRYvvjWokKnnGcO2LkE_fAcATeN0or-l5EhoWJ60ydddeo-JagxQf2Y9mdKwd=w755-h203-s-no)
* Notifies if charge goes down to 1% 
 <br>![Image 2](https://lh3.googleusercontent.com/pw/AIL4fc_T6QXciqqFyMmtJ-Et0elR8lzJ--chpjY04Q-vyYKJ3WYEKJNaSBS3-PqA3RVWCveORl1xxityVjNEyrHhwixsD-RgrcCjUe1-No17Vqbch99FAJSl6hk2wYTs_VzqhJvNc8PgxdNnktG2DcVUHNFm=w737-h189-s-no)
* Notifies if significant battery energy is used 
 <br>![Image 3](https://lh3.googleusercontent.com/pw/AIL4fc8OPia9vspZu_qPUp6HI42Oweo7eqPb3xTSd8C3XYOxKlUlBFwfED-1A0v0nBCLhCnNS1--SJxSMLBc10q2Fhri88zOjuyuw-unJ5wDaSfJSPs91jbJ3g1oix70Srdr1FPmpShAG2Rieoq2Qxiq0YTF=w776-h178-s-no)
* Automation App: Notification 
 <br>![Image 4](https://lh3.googleusercontent.com/pw/AIL4fc9XHbOisr4tyY_xFF04GFfbnlM9aNKWZ7iEjnjpMZ7SI_aSUH5MVLzUVAwEaxomF4cPUjpLH_WTPbYlGespX7TkMdyhiNz7wl-SFG_eZf2LeE-Kok_pGGHjS4wl5ZSMudrO_wlqlFT630LDywhQYZd_=w808-h194-s-no)
* Pushover Notification 
 <br>![Image 5](https://lh3.googleusercontent.com/pw/AIL4fc9jJhpSG273D8-7hKEmeJWOwzEF10y8wQWgPRo307y6fmfr9KexmlviERDbf-O-yv6AeaRyEeiMVRWWMFf7hpCsTrAE3I49G4AABntgokgUhAJbMBhv04wOa_BfUgG2xKzYKCV2trN1fa2f4wVr9csc=w1408-h658-s-no)

## Closing thoughts:

I've been using this script for years and it showed good results. Hereby, I wanted to share it with all the other Macbook users who are concerned about their battery health. Try it out and let me know your thoughts! 

Email: cr34u6rupg@pomail.net<br>
Instagram: <a href="https://www.instagram.com/vasanth_vanan">@vasanth_vanan</a>


