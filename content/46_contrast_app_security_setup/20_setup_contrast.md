+++
title = "Contrast Credentials Setup"
chapter = false
weight = 20
+++

Drag and drop the previously downloaded `contrast_security.yaml` file into the `~/environment/modernization-workshop/modules/30_workshop_app` directory within Cloud9.

Now we will use this file to create a parameters file that will be used during the ECS CloudFormation stack creation in the next step. To create the parameters file, we will use the following command to run a helper script to convert the YAML file into a parameters JSON file that CloudFormation will understand.

```bash
cd ~/environment/modernization-workshop/modules/30_workshop_app
python credential_helper.py
```

{{% notice info %}}
If successful, you should see the message as below.
{{% /notice %}}

<pre>
##### Opening contrast_security.yaml #####
##### Converting to CloudFormation parameters file #####
##### Creating ecs-parameters.json file #####
##### Done... Completed successfully. #####
</pre>

This will create an `ecs-parameters.json` file. Verify that this file is in the `~/environment/modernization-workshop/modules/30_workshop_app` directory.
