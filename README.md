CogniTalk - Helping people practice, maintain, and improve their communication skills.

## Get started

Go to the client folder and install the dependencies...

```bash
cd client
npm install
```

...then create your build files:
```bash
npm run build
```

In a separate CMD/PowerShell, navigate to the backend folder and install the dependency for the analysis library:

```bash
cd backend
pip install praat-parselmouth
```

...then run the server:
```bash
python server.py
```

Navigate to [localhost:5000](http://localhost:5000). You should see your app running.

To load changes in the src files, you must do a full-refresh (Ctrl-F5) of the entire page.

---

The following information below is about Svelte only and is not required for running the project.

## Building and running in production mode

To create an optimised version of the app:

```bash
npm run build
```

You can run the newly built app with `npm run start`. This uses [sirv](https://github.com/lukeed/sirv), which is included in your package.json's `dependencies` so that the app will work when you deploy to platforms like [Heroku](https://heroku.com).


## Single-page app mode

By default, sirv will only respond to requests that match files in `public`. This is to maximise compatibility with static fileservers, allowing you to deploy your app anywhere.

If you're building a single-page app (SPA) with multiple routes, sirv needs to be able to respond to requests for *any* path. You can make it so by editing the `"start"` command in package.json:

```js
"start": "sirv public --single"
```


## Deploying to the web

### With [now](https://zeit.co/now)

Install `now` if you haven't already:

```bash
npm install -g now
```

Then, from within your project folder:

```bash
cd public
now deploy --name my-project
```

As an alternative, use the [Now desktop client](https://zeit.co/download) and simply drag the unzipped project folder to the taskbar icon.

### With [surge](https://surge.sh/)

Install `surge` if you haven't already:

```bash
npm install -g surge
```

Then, from within your project folder:

```bash
npm run build
surge public my-project.surge.sh
```
