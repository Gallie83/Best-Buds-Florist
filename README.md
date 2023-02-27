# **Best Buds**
Best buds is a fictional florist shop that specialises in bouquets and indoor plants. Located in Dublin, Ireland, Best Buds has a big focus on interacting with their consumer base. The website allows customers to make accounts that stores their information, which then also allows them to leave reviews on products. The website also has a blog section called 'Best Blogs' where they keep customers up to date on new products or even events the business might host. The blog allows customers to comment on posts and interact with each other, strenghtening their connection with their customers.

[Live Website](https://best-buds.herokuapp.com/)

![Best Buds home page](media/readme/best-buds-homepage.png)

# Contents

* [**Website Goals**](<#website-goals>)
    * [Target Audience](<#target-audience>)
    * [Brand Image](<#brand-image>)
* [**Project Management**](<#project-management>)
    *  [Trello](<#trello>)
* [**User Experience**](<#user-experience-ux>)
    *  [User Stories](<#user-stories>)
    *  [Wireframes](<#wireframes>)
    * [Design Choices](<#design-choices>)



# Website Goals
## Target Audience

* While also offering services to those who need it for weddings/funerals, or offering valentines and birthday gift ideas, Best buds core target audience is aimed towards floral enthusiasts. This is reinforced with the blog section, where their customer community can directly interact with business and other customers.

## Brand Image

* Best buds brand image is that they are a website built by flower enthusiasts, for flower enthusiasts. Every part of this website has been designed to show that above all else, the business cares for it's product as much as it's customers.

![About us image](media/readme/about-us.png)

# Project Management

## Trello

* For this project I have used Trello to manage my projects progress. I have found trello monumentally helpful for monitoring my projects development and ensuring user stories were fulfilled in an efficient manner.

![Trello](media/readme/trello.png)

# User Experience (UX)

## User Stories

### Viewing And Navigation
* As a site user I want to quickly see what products and services are available.
* As a site user I want to be able to click on a product to find out more information about it.
* As a site user I want to have access to the website through any device.
* As a site user I want to have access to all pages through the navbar.
* As a site user I want to be able to sort products in different ways(A-Z/By Price).
* As a site user I want to be able to search the whole store for products.
* As a site user I want to be able to view contact information for the business.

### Registration And User Accounts
* As a customer I want to be able to be able to easily register an account.
* As a customer I want to be able to store my information with my profile to make the checkout process quicker.
* As a customer I want to be able to view my order history.
* As a customer I want to be able to review products I've purchased. 
* As a customer I want to be able to interact with blog posts.


### Products and Purchasing
* As a customer I want visual confirmation when adding or removing from my cart.
* As a customer I want to be able to see how much is currently in my cart on any page.
* As a customer I want to be able to receive email confirmation that I have made an order.
* As a customer I want to clearly see a summary of my cart before checkout is complete to ensure the order details are correct.
* As a customer I want to see an order confirmation after checkout with all the orders details.

### Site Admin
* As a Site Admin I want to be able to create, read, update and delete products and blog posts. 
* As a Site Admin I want to be receive visual confirmation that I have created updated or deleted a product/post.
* As a Site Admin I want to be able to access the admin panel.
 

[Back to top](<#contents>)

## Wireframes

These wireframes were produced in [Figma](https://figma.com). I made frames for a full width display and then modeled for smaller screens once I had designed the full width diplay. The finished site varies slightly from the wireframes due to developments that occured during the creation process. I then scaled down the site and stacked content to fit it on smaller devices.

![Desktop wireframe image](media/readme/home-wireframe.png)
![Desktop wireframe image](media/readme/products-wireframe.png)
![Desktop wireframe image](media/readme/details-wireframe.png)

For smaller screens I created a second navbar that would replace the original. I did this as the original navbar looked very messy on smaller screens. In this navbar I replaced the business logo with an elegant font that is also used in the image carousel.

![Small navbar image](media/readme/small-navbar.png)

[Back to top](<#contents>)

## Design Choices

### Logo

I used [Logo](https://logo.com/) to create the Best Buds Logo. I really like the simple, legible design of it and it immediately grabbed me when I saw it.

![Logo](media/best-buds-logo.png)

### Colour Scheme

For the colour scheme of this website, I wanted to use a palette with earthy tones that complimented its products. After searching through many colour palettes I decided on this one. I used [Coolors](https://coolors.co/) to browse through the colour schemes. I decided on this palette as I felt it really complimented the Best Buds logo.

![Colour Palette](media/readme/colour-palette.png)

### Typography
 
For the typography of the website I decided to stay with the original bootstrap font for most of the page as it is aesthetically pleasing and very legible. I used [Dancing Script](https://fonts.google.com/specimen/Dancing+Script?query=dancing+script) from google fonts for the small navbar title and for the carousel heading as I thought it looked elegant and fit the vibe of the website. 

![Font Image](media/readme/carousel.png)

[Back to top](<#contents>)

# Features 

## Navbar

This website uses two navbars, one for large screens and another for smaller screens. Both navbars show the current carts total at all times. They both have links to all available pages on the website.

![Large Navbar image](media/readme/large-nav.png)


For smaller screens I created a second navbar that would replace the original. I did this as the original navbar looked very messy on smaller screens. In this navbar I replaced the business logo with an elegant font that is also used in the image carousel.

![Small navbar image](media/readme/small-navbar.png)

## Home Page

The first thing that appears under the navbar on the home screen is a carousel(on small screens a div) that welcomes users to the site and lets users know that delivery on orders over 30 euro is free. This has a link to the products page directly below this to entice customers to view their products.

![Carousel Image](media/readme/carousel.png)

The second slide on the carousel points towards the Indoor Plants section with a corresponding link.

![Carousel second slide](media/readme/carousel2.png)

This is followed by a Collections section, showing the different cateogies that the business specialises in.

![Collections Image](media/readme/collections.png)

The last piece of content on the home page is the About Us section, which documents the business and its morales.

![About us image](media/readme/about-us.png)

## Products

The products page displays a list of all the products unless a user has searched or sorted for a certain type of product. The product card host basic information on each product such as a products image, name, price and what type of product it is.
There is a dropdown button at the top of the page, giving users an option to sort the way products are displayed in a variety of different ways.
If the user is logged in as an admin, small links appear on each card allowing them to edit or delete products.

![Products page](media/readme/products.png)

## Product details

This page displays all the information available about a product from the image and price to the description. The user can add the product to their cart from here aswell.

![Product Details](media/readme/product-details.png)

If the user adds an item to their cart, they receive a toast notification to confirm it has been added with a summary on the item they have added, as well as their carts current total and a link to view their cart.

![Added to cart](media/readme/added-to-cart.png)

Below the product details section is a review section, where logged in users can review products they have bought and document their experience. 

![Review Section](media/readme/review-section.png)

Below this shows all the previous reviews for that product and allows customers to delete reviews that they have left. After a review has been submitted, the customer also receives visual confirmation that they have posted a review.

![Customer Review](media/readme/customer-review.png)

## Occasions

This page details the business ability to cater for different events. The wedding section describes how excited and passionate the business is about catering for weddings, while the funerals page shows that the business handles funerals with professionalism and understanding.

![Occasions](media/readme/occasions.png)

## Best Blogs

The Best Blogs section allows customers to keep up to date with the business and directly interact with blog posts. A button appears at the top of the page for admins to add posts. Each post displayed here has the posts title, intro and date posted, if the user wants to read more they just have to click into the post.

![Best Blog](media/readme/best-blog.png)

Upon clicking into the post, the user can now see all the posts information. Underneath this, logged in customers are encouraged to leave a comment. Admin users can also delete posts from here.

![Blog Post](media/readme/blog-post.png)

Underneath the comment form is a list of all the comments for that post with information like when it was posted and by who. After a comment is posted, a toast pops up to tell the user their comment was successful.

![Blog Comment](media/readme/blog-comment.png)


Admins have access to the Add a blog post page. To create a post they only have to enter a title, intro and the body of the blog. This is then met with a toast confirmation. 

![Add Post](media/readme/add-blog.png)

## My Account

Users can customise their delivery information to make checking out quicker. From this page they can also access any previous orders they have made and view any order history information.

![Account](media/readme/account.png)

## Add Product

Admin user are able to add products from this page. They fill out a form with of all the products information, then they receive a toast to confirm its been added to the online store and be redirected to the new products page.

![Add Product](media/readme/add-product.png)

![New Product](media/readme/test-add.png)

## Login

I used django allauth for all user account and registration. All allauth templates have been styled in the same way with the flower heart image adjascent to whichever allauth form is currently in use.

![Login](media/readme/login.png)

![Register](media/readme/register.png)

## Cart

The users cart displays all the items they have added and gives users the option to update the quantity or remove an item from their bag entirely. At the bottom of this page the user can see a breakdown of their total and whether or not they have reached the free delivery amount. If they have not, there is a prompt letting them know how much more they need to spend.
Underneath this, there is a button that will take them to the checkout page.

![Cart](media/readme/cart.png)

If their cart is empty, there will be a button to the products page, incentivising them to add products to their cart.

![Empty Cart](media/readme/empty-cart.png)

## Checkout

On the checkout page, the user must now enter all their delivery and payment details and they are given the option if they want their delivery information saved. Next to this is another summary of their current cart. 
Below their payment information is a 'Complete Order' button where the amount the user will be charged is also displayed. Once this button is clicked, [Stripe](https://stripe.com/ie) then handle the payment and the user is brought to an order confirmation page.

![Checkout](media/readme/checkout.png)

## Order Confirmation

Upon completing an order, a user is brought to the order confirmation page where they can see all their order details from a recap of their order to all their delivery details. They also receive a message informing them that they will receive a confirmation email and a toast notification will appear with the order number.

![Order Confirmation](media/readme/confirmation.jpg)

## Footer

The footer for this website has been kept very basic, storing only the link to their facebook account and contact information 

![Footer](media/readme/footer.png)

## Toasts

Toasts have been used throughout this website as a way of informing both the admin and the user of their actions. From confirming a user has added a product to their cart, to letting an admin know that they have successfully deleted a product, toasts have been a fundamental part of the user experience.

![Toast](media/readme/toast1.png)
![Toast](media/readme/toast2.png)

[Back to top](<#contents>)

# Future Features

* Currently, any user who is logged in is able to review a product, whether they have purchsed it or not. In future versions of this project I aim to limit reviews to people who have actually purchased the product.

* Allow admins to make draft blog posts that they can save and come back to before posting.

* Allow admins to edit blog posts without having to delete the original and rewrite each post. I was not able to implement this feature due to time contraints.

* Have a page where admins are able to monitor how many users they have, how many orders are being made daily and gives them notifications when users leave a review or blog comment. 

* Allow users to delete/edit comments on posts. Again, this feature was not implemented due to time contraints with the project deadline.

* Display the average rating of the product on the product details page.

* Allow customers to track their order.

* Allow users to refine their product sorting even more. At the moment they can only sort products with a single filter(by price or by type) but ideally they would be able to sort by price while also filtering by type of product.

# Technologies Used

## Languages

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Provides the functionality for the site.
* [HTML5](https://en.wikipedia.org/wiki/HTML) - Provides the frontend content and structure for the website.
* [CSS3](https://en.wikipedia.org/wiki/CSS) - Provides the all stylings throughout the website.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Provides interactive elements of the website

## Frameworks & Software
* [Bootstrap](https://getbootstrap.com/) - A CSS framework that helps building solid, responsive, mobile-first sites
* [Django](https://www.djangoproject.com/) - A model-view-template Python framework used to throughout site
* [Figma](https://figma.com/) - Used to create the wireframe.
* [Git](https://git-scm.com/) - Used for version control
* [Github](https://github.com/) - Used to host and edit the website.
* [Heroku](https://en.wikipedia.org/wiki/Heroku) - A cloud platform that the application is deployed to.
* [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) - Used to test performance of site.
* [Favicon](https://favicon.io/) - Used to create the favicon.
* [VSCode](https://code.visualstudio.com/) - Used for writing all the websites code.
* [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Used to debug and test responsiveness.
* [Trello](https://trello.com/en-GB) - A project management tool to organize the project.
* [Amazon Web Services](https://aws.amazon.com/) - A service that hosts all static files and images in the project.
* [PostgreSQL](https://www.postgresql.org/) - Database used for production
* [ElephantSQL](https://www.elephantsql.com/) - A PostgreSQL database hosting service.
* [HTML Validation](https://validator.w3.org/) - Used to validate HTML code
* [CSS Validation](https://jigsaw.w3.org/css-validator/) - Used to validate CSS code
* [Stripe](https://stripe.com/ie) - Used for all the websites payment functionality

# Testing

## Testing User Stories

### Viewing And Navigation

* As a site user I want to quickly see what products and services are available.

    * There is a link to view all products and product types from the navbar as well as a link to the occassions page which has information about the business' catering.
     
* As a site user I want to be able to click on a product to find out more information about it.

    * Clicking on product card from the products page directs the user to the products detail page which has all product information.

* As a site user I want to have access to the website through any device.

    * Website is * [responsive](<#responsiveness>) on all screen sizes and browsers.

* As a site user I want to have access to all pages through the navbar.

    * Navigation links for each page are available through the navbar

* As a site user I want to be able to sort products in different ways(A-Z/By Price).

    * At the top of the products page there is a Sort By dropdown button which has a variety of ways site users can sort products.

* As a site user I want to be able to search the whole store for products.

    * In the navbar there is a search form. This form does not only check if the searched words are in the title, but also if they appear in the description.

* As a site user I want to be able to view contact information for the business.

    * Contact information for the business is available in the footer.

### Registration And User Accounts

* As a customer I want to be able to be able to easily register an account.

    * A navigation link to the registration page can be found under the Accounts dropdown.

* As a customer I want to be able to store my information with my profile to make the checkout process quicker.

    * Logged in customers can either update their delivery information from their account page, or click the 'Save my Information' button from the checkout page.

* As a customer I want to be able to view my order history.

    * Customer can see their whole order history from their Account page, as well as click into each order for all available information regarding that order.

* As a customer I want to be able to review products I've purchased. 

    * Logged in customers can leave reviews on products by going to the details page of that product and filling out the review form below the products information section.

* As a customer I want to be able to interact with blog posts.

    * Logged in customers are able to leave comments below blog posts by clicking into the blog posts page and filling out the comment section below the post.

### Products and Purchasing

* As a customer I want visual confirmation when adding or removing from my cart.

    * Upon adding, removing or changing the an item's quantity, the customer receives a toast pop up to confirm their action.

* As a customer I want to be able to see how much is currently in my cart on any page.

    * On any screen size, a cart icon with the current total of the customers cart is available at the navbar at all times.

* As a customer I want to be able to receive email confirmation that I have made an order.

    * Upon completing an order, the customer is brought to a checkout success page where a message will appear, confirming that they will receive email confirmation. They will shortly after receive a personalised message with all the orders information.

* As a customer I want to clearly see a summary of my cart before checkout is complete to ensure the order details are correct.

    * A summary of the customers cart(all items names, quantities, the cart's subtotal and delivery cost) appears on the cart page, the checkout page and then again once the order has been completed on the checkout success page.

* As a customer I want to see an order confirmation after checkout with all the orders details.

    * Once an order has been placed, the user will be brought to the checkout success page where they will receive both a summary of the orders details, a message stating they will receive email confirmation, and also a toast pop up of the order number.

* As a Site Admin I want to be able to create, read, update and delete products and blog posts. 

    * Site admins are able to create, read update and delete products with ease either through the Add Product link on the navbar or the products page.

    * Unfortunately admins are only able to create read or delete blog posts at the moment as editing blog posts functionality has yet to be added.

* As a Site Admin I want to be receive visual confirmation that I have created updated or deleted a product/post.

    * Upon creating, updating or deleting a product/post, the admin will receive a toast with a message confirming their actions.

* As a Site Admin I want to be able to access the admin panel.

    * Site users that are logged in have access to the admin panel through the URL.









  * ### Responsiveness
      * The website is responsive accross all screen sizes. On small screen sizes the images and content stack ontop each other. The website was tested on the following browsers with no visible issues for the user. Google Chrome, Microsoft Edge and Mozilla Firefox.

      * The responsive design tests were carried out manually with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/).

|        | Moto G4 | Galaxy S5 | iPhone 5 | iPad | Display <1200px | Display >1200px |
|--------|---------|-----------|----------|------|-----------------|-----------------|
| Render | pass    | pass      | pass     | pass | pass            | pass            |
| Images | pass    | pass      | pass     | pass | pass            | pass            |
| Links  | pass    | pass      | pass     | pass | pass            | pass            |

