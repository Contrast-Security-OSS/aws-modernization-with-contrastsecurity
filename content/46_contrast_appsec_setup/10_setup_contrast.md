+++
title = "Contrast Setup"
chapter = false
weight = 10
+++

We will now setup the environment for the Contrast Security module.

Copy the files from the `~/environment/modernization-workshop/modules/40_contrast_security/root_files` to the `~/environment/modernization-workshop` root directory.

```bash
cp ~/environment/modernization-workshop/modules/40_contrast_security/root_files/* ~/environment/modernization-workshop
```

Drag and drop the previously downloaded `contrast_security.yaml` file from your local workstation into the `~/environment/modernization-workshop/modules/40_contrast_security` directory within the Cloud9 IDE.

Now we will use this file to create a `ecs-parameters.json` file that will be used during the ECS CloudFormation stack creation in the next step. To create this file, we will use the following command to run the provided `credential_helper.py` helper script to convert the YAML file into a JSON file that CloudFormation will be able to understand.

```bash
cd ~/environment/modernization-workshop/modules/30_workshop_app
python credential_helper.py
```

If successful, this will create an `ecs-parameters.json` file in the `~/environment/modernization-workshop` directory. Verify that this file is in the `~/environment/modernization-workshop/modules/30_workshop_app` directory.
