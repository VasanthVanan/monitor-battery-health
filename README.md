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
 <br>![Image 1](https://uc9a99df15c22fbacb8ccc3d1165.previews.dropboxusercontent.com/p/thumb/AB795HDZbn97vRRFEVqEqGLLh8aI8zv5bdk6S5E51PmJiPhMbUzFLv9nYzaxa9ZaJkDyEsv2t0YmoXSfZVpHH-qMmz03DNXlKWM-84LHGE-b3zQmvckTSwMw8ogq2ozBGk1fPpqwX4heAyoQIp8AvT0YDwQp89VQH1KqjvXrq_b2wzmzqWjJSRQhE0lkC2aMjgDUyfWCjgHTor1QeAGxwKxqExuAmPeBNcHpfO4XvyFv-QqNEgiv6hhh6OCRngF74IlU6WHxOnwzFXmEo53aAxHqjKZecgAUgYPbToGpeMjQPd6q8PpKDeSrU_kgQXSlMvU0B9Mu_f-5-a7iP5GivMEdaWWwtu5pb0zT6tkX8v1Us4zL5wMCiZEkGg5fvtGaMXObRltWkXy-ZPEQRbrzNMKfWCA8UgcuoAlrOzgfCwooMw/p.png)
* Notifies if charge goes down to 1% 
 <br>![Image 2](https://ucf61e794757737e386ee6510cab.previews.dropboxusercontent.com/p/thumb/AB7BF4vgWa24XEaPqqdknAyKSP4lEVDMLzB6vy5JMXsJE9W7v199wymXWj1VEsCTc-olvgF8JmVfzfXt7y4gzI3HvR5dfDqmiCZ6F-7rla1I-ejYu7jSgGrXjOF_hLRYIpcUYjWW_4qJWpVTVfBgKvFAoRE6Cw0SNWmovx1xMQdha5tTwESZ-DumL_3x6WCmN1lkPNwHWEf5y0E4ollSHkRta-QtWTZTh9itZ_mN7X5jNVMitvNXIRb7r6mvCMEpw4Pt54BqXwGUPrOkM5YOMjEYP-SCW5DKcYNHAwT_IIrdWB-_2Fsz3WcRVHb-JI0pVKcrkoeVWAs4FYVoeNlRPp_dFoCkMcp8nIcpHpN8wxmP3SNIJkoLdBs3Bet4702xlkDNKja6zPaRWqiMg-rs7H8oC9rxnAVqmAgNCcXlT-9UfA/p.png)
* Notifies if significant battery energy is used 
 <br>![Image 3](https://uc2c1ebe2fcaefbc663c3ea1f02d.previews.dropboxusercontent.com/p/thumb/AB7qKatR_FcMUkhFsqQt_qSV20MlDU9LqX89CWuZnZKPDFI5XxsmkOCznVOZ4xJRoAasl4QrtYDcFcZmp8LG9z9XqzGPPziCqUR7VJaIX0Ab-n2ZewJoNTmj6fkqT6ZMii07DbgiHmEF_4b0tHLV4Bgpnf1IQysbE16DI0IQJrLLCf_hy7urWgXUf36yWPYF7q7j-avfwfd9p8X0BkLif9LsCoahOLSLkZM3AU1YAIaBc-4MvUoetzRMD5FfjkSqG51BSz_wmadHu9fjz_wwaHPHN-7LSPdDudPubYaOBEV-cHNa5q2328KvGhYSne6nq5cu5g3Zk0FEQgtoL8hlDqpr_veCvm4iLHm0FexouB1n83lQoGRlICrsMBk-42ZzektOVhcSbj0N8J7V6_vEW7Q06cSOPCLmRHpe-aS5hXczVw/p.png)
* Automation App: Notification 
 <br>![Image 4](https://uccd7d43c36d0a72fa9a87f95297.previews.dropboxusercontent.com/p/thumb/AB4RUjgSkEenpmiVJu4wT8KhdcM3G7RtKKZvvMua_LomrfoUZfnIns_ytEgsg1yBJk1Yjq7FFGFqQw5lnTv0CqO6_O3Tzlh2w65dvuV_vbowoHBybQFY2y3S4DPu7_NoFblvq0JYcwthn-tJruUjhq6kWR4mFELUfcPZjP9T3rwEmKouBafCevDDo1Kmbi8aOAVLZSKkJ-bd3UltJtoSRc7O9Jf5K9viffe7hmkTpGjxbLrvcs6C5J--95ZSbBgg2T4mS_4j4qEEzpe5PxEBsUZ3HaIPuxYcMVnFM1XoblbgN7KBN41V_1vtPVRchmfEKU3SjTqSm4ExWQ95SdTJ3iU-4i6-XtJh1Y631mcM1mb1f2j214c2ECLHfb0ZFLq6CAcAH8hp89N5H4f-XffaebqqwLUMAptrPryfCU4fTIEXog/p.png)
* Pushover Notification 
 <br>![Image 5](https://ucf43ac81635c126dbf25182f5ae.previews.dropboxusercontent.com/p/thumb/AB7o2WkRGacpf5MaCSCgxRmzHsH9jXT43UBLRC1YqCq4Q50wrMppvOFMn-D0A0fZsIWmQ1QkDM45vz_fbxWGAD2eH7gnaeq6tFOJT-bybgIGRtaYRtDZYMrv7VxQ_K-wx3HvUc-vzp1ppUXP4QObPgA9eH7DlPwl34G6bp5rBVwwFADqrA_aKwIDYKtQDnV8sqAW4iIYPuDmW_CqGNlPLvtK2zooQRh-JhHvEk8SoLjNNxcZabZhG043N3DiIzAoQkEwMjt3YLARtj7Dry4b-uhTu8Z9QCUI123OS935faINRVw9cylimF9SenxtSgzi6iHVZra9SFvGwPwnZycHkEjJ0nTwq1F_6612APCF-leqpqJQ2dxtl72FSojbvOeBsxhmz9cKSTFa_OibVCVdkpM2GFmqISStA1Z355JzvU0YPQ/p.png)

## Closing thoughts:

I've been using this script for years and it showed good results. Hereby, I wanted to share it with all the other Macbook users who are concerned about their battery health. Try it out and let me know your thoughts! 

Email: cr34u6rupg@pomail.net<br>
Instagram: <a href="https://www.instagram.com/vasanth_vanan">@vasanth_vanan</a>


