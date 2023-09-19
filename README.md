# Deploy FastApi App with ECS and Fargate
This repository contain necessary files to deploy an app in aws using ECS and Fargate. 

<img src="https://i.imgur.com/HKiCk88.png" alt="MarineGEO circle logo" style="height: 200px; width:500px;"/>

Fue necesario cambiar en ~/.docker/config.json credsStore por credStore
```

{
        "auths": {
                "XXXXXXXXXXX.dkr.ecr.XXXXX.amazonaws.com": {},
                "public.ecr.aws": {}
        },
        "credsStore": "desktop",
        "currentContext": "colima"
}
```

Ademas es necesario tener en el grupo de usuario políticas de AmazonEC2ContainerRegistryFullAccess y AWSAppRunnerServicePolicyForECRAccess para poder registrar la imagen en ECR. Muy importante, validar que en el security group tengamos el puerto adecuado activo, esto validando las reglas de salida.
