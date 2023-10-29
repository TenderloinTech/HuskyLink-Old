# Reflex Development

We've worked with reflex throughout the hackathon, and here are our findings.

## Deploying Locally

Deploying locally worked initially, but late into the competition, we kept getting websocket errors. It appeared that the websocket server was not working, and we got several "unable to connect to the websocket" errors.

## Deploying to the cloud

Deplying to the Reflex cloud did not work. The reflex cloud, which appeared to be using fly.io, did not work. The program claimed to have failed to deploy our app, but upon reading the deploy logs, nothing seemed to be wrong.

```
──────────────────────────────────────────────────────────────── Deploying production app. ─────────────────────────────────────────────────────────────────
Deployment will start shortly. Closing this command now will not affect your deployment.
Waiting for server to report progress ...
Hosting server reports failure.
Check the server logs using `reflex deployments build-logs huskylink1`
```

Logs of running `reflex deployments build-logs huskylink1`: https://pastebin.com/raw/rAUcpu4J

After viewing the url for the app, huskylink1.reflex.run, the site showed a static version of the app, with what appeared to be cached database data. It then complained it was unable to communicate with the websocket, which was hosted at `rxh-prod-huskylink1.fly.dev`.
