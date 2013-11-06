# Salsita Sofware, s.r.o., Express & Angular Skeleton

## FAQ

### How do I run it locally?
1. Install node.js
2. `npm install -g coffee-script grunt-cli bower karma phantomjs`
3. `git clone https://github.com/salsita/salsitasoft.com.git`
4. `git checkout develop` (if you want the latest code, otherwise stay in master, i.e. do nothing).
5. In `code/client`:
  * `npm install`
  * `bower install`
  * `grunt build && grunt test`
5. In `code/server`:
  * `npm install`
  * `grunt dev`...This will start the Express server on port 3000.

Then go to `localhost:3000` and you should see it up and running.
