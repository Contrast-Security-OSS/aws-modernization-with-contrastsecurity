+++
title = "How to discover a new vulnerability"
chapter = false
weight = 20
+++

In this part we will discover a new vulnerability in Webgoat application and examine the finding in Contrast Security.

It is important to reiterate that Contrast Security identifies vulnerabilities by looking at the normal traffic that goes through the application. With that in mind, let's identify a SQL injection in Webgoat with Contrast.

1. Use the username `webgoat` and passowrd `webgoat` to log into the Webgoat application.

2. Navigate to Injection Flaws --> String SQL injection.

3. Enter `Smith` or any other string into the field and click on `Go` button:

{{< figure src="/images/contrast/wg_1.png" style="border: 1px solid #000; max-width:auto; max-height:auto;">}}

4. Go back to Contrast Security platform and click on Vulnerabilities within the `WebGoat` application. As you can see, the Contrast agent has identified new vulnerabilities: Cross-Site Scripting (XSS) and SQL injection.

{{< figure src="/images/contrast/ce_4.png" style="border: 1px solid #000; max-width:auto; max-height:auto;">}}

Now you can click on either vulnerabilities to get more information.