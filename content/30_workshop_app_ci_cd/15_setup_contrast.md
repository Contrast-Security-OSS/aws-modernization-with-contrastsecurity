+++
title = "Contrast Credentials Setup"
chapter = false
weight = 20
+++

### Contrast Credentials Setup 
In order for the Contrast Agent to connect to the Contrast UI, we need to get API credential configuration information from the Contrast UI.

In the Contrast Security Console click the `Add Agent` button.

![Add Agent](/images/contrast-add-agent.png)

Skip `Step 1: Agent Selection` and go to `Step 2: Configuration` to download the `contrast_security.yaml` configuration file.
![Step 2: Configuration](/images/contrast-download-config.png)

Click `Download Config File` to download this to your local system then drag and drop this credentail file into the `~/environment/modernization-workshop/modules/30_workshop_app` directory.

Now we will use this file to create a parameters file that will be passed to the ECS CloudFormation in the next step. To do this we will use the following command to run a helper script to convert the YAML file into a parameters file.

```bash
cd ~/environment/modernization-workshop/modules/30_workshop_app
python credential_helper.py
```

This will create an `ecs-parameters.json` file. Verify that this file is in the `~/environment/modernization-workshop/modules/30_workshop_app` directory.
