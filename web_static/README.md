# 0x01. AirBnB clone - Web static
## Learning Objectives

### General

* What is HTML
* How to create an HTML page
* What is a markup language
* What is the DOM
* What is an element / tag
* What is an attribute
* How does the browser load a webpage
* What is CSS
* How to add style to an element
* What is a class
* What is a selector
* How to compute CSS Specificity Value
* What are Box properties in CSS

| Task | File |
| ---- | ---- |
| 0. Inline styling | [0-index.html](./0-index.html) |
| 1. Head styling | [1-index.html](./1-index.html) |
| 2. CSS files | [2-index.html](./2-index.html), [styles/2-common.css](./styles/2-common.css), [styles/2-header.css](./styles/2-header.css), [styles/2-footer.css](./styles/2-footer.css) |
| 3. Zoning done! | [3-index.html](./3-index.html), [styles/3-common.css](./styles/3-common.css), [styles/3-header.css](./styles/3-header.css), [styles/3-footer.css](./styles/3-footer.css), [images/](./images/) |
| 4. Search! | [4-index.html](./4-index.html), [styles/4-common.css](./styles/4-common.css), [styles/3-header.css](./styles/3-header.css), [styles/3-footer.css](./styles/3-footer.css), [styles/4-filters.css](./styles/4-filters.css), [images/](./images/) |
| 5. More filters | [5-index.html](./5-index.html), [styles/4-common.css](./styles/4-common.css), [styles/3-header.css](./styles/3-header.css), [styles/3-footer.css](./styles/3-footer.css), [styles/5-filters.css](./styles/5-filters.css), [images/](./images/) |
| 6. It's (h)over | [6-index.html](./6-index.html), [styles/4-common.css](./styles/4-common.css), [styles/3-header.css](./styles/3-header.css), [styles/3-footer.css](./styles/3-footer.css), [styles/6-filters.css](./styles/6-filters.css), [images/](./images/) |
| 7. Display results | [7-index.html](./7-index.html), [styles/4-common.css](./styles/4-common.css), [styles/3-header.css](./styles/3-header.css), [styles/3-footer.css](./styles/3-footer.css), [styles/6-filters.css](./styles/6-filters.css), [styles/7-places.css](./styles/7-places.css), [images/](./images/) |
| 8. More details | [8-index.html](./8-index.html), [styles/4-common.css](./styles/4-common.css), [styles/3-header.css](./styles/3-header.css), [styles/3-footer.css](./styles/3-footer.css), [styles/6-filters.css](./styles/6-filters.css), [styles/8-places.css](./styles/8-places.css), [images/](./images/) |

# Tasks
## 0. Inline styling
* An HTML page that displays a header and a footer
* Layout:
	* Body:
		* no margin
		* no padding
	* Header:
		* color #FF0000 (red)
		* height: 70px
		* width: 100%
	* Footer:
		* color #00FF00 (green)
		* height: 60px
		* width: 100%
		* text `Best School` center vertically and horizontally
		* always at the bottom at the page
## 1. Head styling
* An HTML page that displays a header and a footer by using the `style` tag in the `head` tag(same as `0-index.html`)
	* Layout must be exactly the same as `0-index.html`
## 2. CSS files
* An HTML page that displays a header and a footer by using CSS files(same as `1-index.html`)
	* Layout must be exactly the same as `1-index.html`
## 3. Zoning done!
* An HTML page that displays a header and a footer by using CSS file(same as `2-index.html`)
	* Common:
		* no margin
		* no padding
		* font color: #484848
		* font size: 14px
		* font family: Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;
		* [icon](./images/icon.png) in the browser tab
	* Header:
		* color: white
		* height: 70px
		* width: 100%
		* border bottom 1px #CCCCCC
		* [logo](./images/logo.png) align on left and center vertically (20px space at the left)
	* Footer:
		* color white
		* height: 60px
		* width: 100%
		* border top 1px #CCCCCC
		* text `Best School` center vertically and horizontally
		* always at the bottom of the page
## 4. Search!
* An HTML page that displays a header, footer and a filters box with a search button
* Layout:(based on `3-index.html`)
	* Container:
		* between `header` and `footeer` tags, add a `div`:
			* classname: `container`
			* max width 1000px
			* margin top and bottom 30px - it should be 30px under the bottom of the `header`
			* center horizontally
		* Filter section:
			* tag `section`
			* classname `filters`
			* inside the `.container`
			* color white
			* height: 70px
			* width: 100px of the container
			* border 1px#DDDDDD with radius 4px
		* Button search:
			* tag `button`
			* text `Search`
			* font size: 18px
			* inside the section filters
			* background color #FF5A5F
			* text color #FFFFFF
			* height: 48px
			* width: 20% of the section filters
			* no borders
			* border radius: 4px
			* center vertically and at 30px of the right border
			* change opacity to 90% when the mouse is on the button
## 5. More filters
* An HTML page that displays a header, footer and a filters box
* Layout: (based on `4-index.html`)
	* Locations and Amenities filters:
		* tag: `div`
		* classame: `locations` for location tag and `amenities` for the other
		* inside the section filters(same level as the `button` Search)
		* height: 100% of the section filters
		* width: 25% of the section filters
		* border right #DDDDDD 1px only for the first left filter
		* contains a title:
			* tag: `h3`
			* font weight: 600
			* text `States` or `Amenities`
		* contains a subtitle:
			* tag: `h4`
			* font weight: 400
			* font size: 14px
			* text with fake contents
## 6. It's (h)over
* An HTML page that displays a header, footer and a filters box with dropdown
* Layout: (based on `5-index.html`)
	* Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter `div`:
		* tag `ul`
		* classname `popover`
		* inside each `div`
		* not displayed by default
		* color #FAFAFA
		* width same as the `div` filter
		* border #DDDDDD 1px with border radius 4px
		* no list display
		* Location filter has 2 levels of `ul`/`li`:
			* state -> cities
			* state name must be displayed in a `h2` tag(font size 16px)
## 7. Display results
* An HTML page that displays a header, footer and a filters box with dropdown and results
* Layout: (based on `6-index.html`)
	* Add Places section:
		* tag: `section`
		* classname: `places`
		* same level as the filters section, inside `.container`
		* contains a title:
			* tag: `h1`
			* text: `Places`
			* align in the top left
			* font size: 30px
		* contains multiple "Places" as listin  (horizontal or vertical) describe by:
			* tag: `article`
			* width: 390px
			* padding and margin 20px
			* border #FF5A5F 1px with radius 4px
			* contains the place name:
				* tag: `h2`
				* font size: 30px
				* center horizontally
## 8. More details
* An HTML page that displays a header, footer, a filter box(dropdown list) and the result of the search.
* Layout: (based on `7-index.html`)
	* Add more information to a Place `article`:
		* Price by night:
			* tag: `div`
			* classname: `price_by_night`
			* same level as the place name
			* font color: #FF5A5F
			* border: #FF5A5F 4px rounded
			* min width: 60px
			* height: 60px
			* font size: 30px
			* align: the top right(with space)
		* Information section:
			* tag: `div`
			* classname: `information`
			* height: 80px
			* border: top and bottom #DDDDDD 1px
			* contains (align vertically):
				* Number of guests:
				  	* tag: `div`
				  	* classname: `max_guest`
				  	* width: 100px
				  	* fake text
				  	* [icon](./images/icon_group.png)
				  * Number of bedrooms:
				  	* tag: `div`
				  	* classname: `number_rooms`
				  	* width: 100px
				  	* fake text
				  	* [icon](./images/icon_bed.png)
				  * Number of bathrooms
				  	* tag: `div`
				  	* classname: `number_bathrooms`
				  	* width: 100px
				  	* fake text
				  	* [icon](./images/icon_bath.png)
		* User section:
			* tag:`div`
			* classname: `user`
			* text: `Owner: <fake text>`
			* `Owner` text should be in bold
		* Description section:
		    	* tag: `div`
		    	* classname: `description`
