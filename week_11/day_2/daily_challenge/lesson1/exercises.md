### Exercise 1
Repeat all of the above steps, then :

- Create a route called blog, that welcomes your users
- Create a route called blog/articles, that display a list of article titles
__*Run your app*__

### Exercise 2
Repeat all of the above steps, then :

- Create a route called `/blog`, that welcomes your users
- Create a route called `/blog/articles`, that display a list of articles' title
- Hint: Use the render_template_string() function
- __*Run your app*__

### Exercise 3
- Create a template called homepage.html
- Create a route called blog, that welcomes your users (use the template homepage.html)
- Create a template called articles.html
- Create a route called blog/articles, that display a list of articles inside the articles.html. This list must be a dictionnary with some keys (title, content, author) and values. This dictionary must be passed from the route, to the template file
- Add a button "Go back to homepage" to the template articles.html, that redirects the user to the /blog route.
- Create a new route called profile. The developer didn't finish this route, so instead of giving an error to the user, redirect him to the /blog route
__*Run your app*__