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
 <br>![Image 1](https://uc9a99df15c22fbacb8ccc3d1165.previews.dropboxusercontent.com/p/thumb/AB795HDZbn97vRRFEVqEqGLLh8aI8zv5bdk6S5E51PmJiPhMbUzFLv9nYzaxa9ZaJkDyEsv2t0YmoXSfZVpHH-qMmz03DNXlKWM-84LHGE-b3zQmvckTSwMw8ogq2ozBGk1fPpqwX4heAyoQIp8AvT0YDwQp89VQH1KqjvXrq_b2wzmzqWjJSRQhE0lkC2aMjgDUyfWCjgHTor1QeAGxwKxqExuAmPeBNcHpfO4XvyFv-QqNEgiv6hhh6OCRngF74IlU6WHxOnwzFXmEo53aAxHqjKZecgAUgYPbToGpeMjQPd6q8PpKDeSrU_kgQXSlMvU0B9Mu_f-5-a7iP5GivMEdaWWwtu5pb0zT6tkX8v1Us4zL5wMCiZEkGg5fvtGaMXObRltWkXy-ZPEQRbrzNMKfWCA8UgcuoAlrOzgfCwooMw/p.png)
* Notifies if charge goes down to 1% 
 <br>![Image 2](https://ucf61e794757737e386ee6510cab.previews.dropboxusercontent.com/p/thumb/AB75J-mEkm3_PJEqQ9QWcmvm9DWUtZMp4LD1dnzi3C2wI-oTB935ubVHmi7BYH6crydtJQALMdwHbzlDIU5JyHWyr6kAolmSvPNP9v29isARGerUOj5LGyNIaq4ROdvLpV-C4DLDgoCRm9zt2yCuSq_OSTL0a-lbjax4xpMRGV9oyopcZkjrzhgxZN3xz8J2Am9XQ4ptsTUAi_Zsy4dDSv0_p3DFsI7X1bBRrSLWTAFrFTrScrk8xsRV6m7qFKbVIUDQD954sjG8q1jmeyYAOegTycjooFdpCtMVgp8mqCDBXPmfSjUZicZterLkb8mHfQCZ6gx0EcI58pMvgi-7DAwEt0qXHOMQgKIrcpXfWUUclNg_3Uj5aTf6uyv_r_jGywafUEDjQi0vmty1PS_Yof04Lt0Z158LoRBFlprjOwUQvQ/p.png)
* Notifies if significant battery energy is used 
 <br>![Image 3](https://uc2c1ebe2fcaefbc663c3ea1f02d.previews.dropboxusercontent.com/p/thumb/AB7qKatR_FcMUkhFsqQt_qSV20MlDU9LqX89CWuZnZKPDFI5XxsmkOCznVOZ4xJRoAasl4QrtYDcFcZmp8LG9z9XqzGPPziCqUR7VJaIX0Ab-n2ZewJoNTmj6fkqT6ZMii07DbgiHmEF_4b0tHLV4Bgpnf1IQysbE16DI0IQJrLLCf_hy7urWgXUf36yWPYF7q7j-avfwfd9p8X0BkLif9LsCoahOLSLkZM3AU1YAIaBc-4MvUoetzRMD5FfjkSqG51BSz_wmadHu9fjz_wwaHPHN-7LSPdDudPubYaOBEV-cHNa5q2328KvGhYSne6nq5cu5g3Zk0FEQgtoL8hlDqpr_veCvm4iLHm0FexouB1n83lQoGRlICrsMBk-42ZzektOVhcSbj0N8J7V6_vEW7Q06cSOPCLmRHpe-aS5hXczVw/p.png)
* Automation App: Notification 
 <br>![Image 4](https://uccd7d43c36d0a72fa9a87f95297.previews.dropboxusercontent.com/p/thumb/AB4RUjgSkEenpmiVJu4wT8KhdcM3G7RtKKZvvMua_LomrfoUZfnIns_ytEgsg1yBJk1Yjq7FFGFqQw5lnTv0CqO6_O3Tzlh2w65dvuV_vbowoHBybQFY2y3S4DPu7_NoFblvq0JYcwthn-tJruUjhq6kWR4mFELUfcPZjP9T3rwEmKouBafCevDDo1Kmbi8aOAVLZSKkJ-bd3UltJtoSRc7O9Jf5K9viffe7hmkTpGjxbLrvcs6C5J--95ZSbBgg2T4mS_4j4qEEzpe5PxEBsUZ3HaIPuxYcMVnFM1XoblbgN7KBN41V_1vtPVRchmfEKU3SjTqSm4ExWQ95SdTJ3iU-4i6-XtJh1Y631mcM1mb1f2j214c2ECLHfb0ZFLq6CAcAH8hp89N5H4f-XffaebqqwLUMAptrPryfCU4fTIEXog/p.png)
* Pushover Notification 
 <br>![Image 5](https://ucf43ac81635c126dbf25182f5ae.previews.dropboxusercontent.com/p/thumb/AB4jB8ZU7aT5PPaTiI6lEFQniOsSB1Pjvsx69YLTOFUUJ51uI1Co5jQXUZ_NTyVOmGvpUCSEhUZI45q1duGNsbCmw2gVWjgX4fJl_JWguxT07PAw5o0iI7ZiL07M7xuLOSEielsMmnFcnjQ0t3Dq3P8ZYfH6y8UZcS9-5G5HkO3OZbcwx_j2kEIXoJCWnbRss42TPu9LTBkF-ZSDvGrP4skUxxkcwppjjHhm3Vwf7sxs5cII1bs4QOuaErh16YN-yX0desOYAD0AEYvudL2uEtGYnj7V4xfKbgQi-Err4MA-M-_gy-dQNLNTq_7pIMEfkcaPGlydzhH2ibYYlvV6a9vNeOCBPeb65am4kJxSA19NZIJsAHuqvcP-ksu5sQEEUCJA-ScDQ0PI6oNJ-VHwnR-8TmJLTrp_YeInGjsW2_kI_Q/p.png)

## Closing thoughts:

I've been using this script for years and it showed good results. Hereby, I wanted to share it with all the other Macbook users who are concerned about their battery health. Try it out and let me know your thoughts! 

Email: cr34u6rupg@pomail.net<br>
Instagram: <a href="https://www.instagram.com/vasanth_vanan">@vasanth_vanan</a>


