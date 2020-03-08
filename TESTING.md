Validation: 

 HTML -  [W3.orgvalidator](https://validator.w3.org/nu/) 

 CSS -  [W3CCSSvalidation](https://jigsaw.w3.org/css-validator) 

Python - [PEP8validator](http://pep8online.com/) 

Javascript - [Esprima](https://esprima.org/demo/validate.html) 



#### part 1 User testing: User stories:

* As a user i would like to be able to type in a keyword to search for items im interested in. - My project features a search bar that when the user imputs a key word it will display a card that matches thae search result.
* As a user i would like to be able to see the price for an artifact and other details pertaining it to make an informed decision on whether to purchase or not. - A price is desplayed on each card to show customer the price of said artifact .
* As a user i would like to be able to bid on/purchase an artifact to potentially aquire said item. This was only partially satisfied. The user is able to purchase an item if they add item to the basket however they cannot bid as I wasnt able to workout how to implememt this feature in time.
* As a user i would like to be able to learn about the some history or events of the item. Each card has a description of said artifact exclaiming some history about the artifact.




#### part 2 Manual testing: 

Navigation bar :

1) When logged in click the Nav links and see if they take you to the respective pages.

2) When the Navigation bar is collapsed click the menu button to see if a dropdown menu is displayed.

3) When on another page other than the artifact page click on the text logo button on the far left hand siode of the nav bar and see if it takes you back to the homepage. Welcome page :

4) Hover over nav links and see if they highlight. 

5) Add an artifact to the cart and see if a number displays next to the cart. 

6) when logged out see if the nav link "login" appears. When logged in see if the nav link "logout " appears.


Login/logout features :

1) when on login page (signed out) try to enter the wrong credentials and see if an error msg appears. 

2) while signed out try to add an artifact to cart and see if you are redirected  to the login page.

3) Try to login and see if a message displays indicating user is logged in./ Try to logout and see if a message displays indicating the user is logged out. 


Register features:

1) click on the regester form. Follow the input requirement in each form. and create an account. See if sucess message is displayed. 
2) Try to enter two different passwords in the register form and see if error message appears. 
3) Try to enter the the same email as your registered account. you should be redirected back to the register form.
4) Try to submit an empty form field see if an error message appears telling you " field is required". 

Reset password : 

1) On the login page, click the link to the reset password page see if you are redirected to the correct page. 
2) Enter email associated with an account and submit see if you are redirected to a page that informs you an email has been sent. 
3) Enter an email or random text not associated with an account and see if an error message displays. 
4) when testing password_reset, according to the code institute videos, in gitpod/locally you won't be able to send/receive an email to a real account therefore the alternative is to use the a terminal. 
Input an email associated with an account you would like to reset the email of into password reset form. Next submit the email and then check the terminal to see if an email message is displayed.  
click the unique link and it should take you to another page that you can then reset your password on.  
5) on the password reset form, input two different passwords to see if an error message appears. 

Cart: 
* Try to add an artifact to cart from the main page and see if it appeaers. 
* Try to amend the total QTY of an artfact. 

Checkout: 
* Try to submit a blank field in the form see if an error message appears. 
* Add an artifact then Enter in the approprete credentials and then use the card number "4242424242424242" and submit payment.


Responsive tests

1) check how the app looks on various screen sizes do this through " dev tools". ( I tested the app on the screen sizes listed below.)
2) make sure theres no horzontal scrolling.
3) Check that the back to top button still appears on smaller screen sizes.
4) Check the text displays clearly and doesnt go off the screen.
5) Check that the layout changes on mobile view.
6) Check the charaters cards are in single file stacked on top of each other when in mobile view.

Screen sizes

* Galaxy 5 | 360x640
* Pixel 2 | 411 x 731
* Iphone 5/SE | 320 x 568
* IPhone 6/7/8 | 375 x 667
* IPhone 6/7/8 plus. | 414 x 736
* IPad | 768 x 1024
* IPad pro | 1024 x 1366
 
 Responsive test Results:

The app passed all the responsive tests.


#### part 3 browser compatibility tests :

I tested this app on several browsers such as :

Internet explorer | Everything good. 
Google chrome | Everything Good.
Google Chrome (Mobile) | Everything Good.
Firefox (mobile) | Everything Good
Samsung mobile internet | Everything Good

 
#### part 4 Issues/bugs :

Stripe card payment: I had a problem with card payments on the app.
I found that when I tried to pay for an item the payment woudnt go through unless i put these exact details:
```

Card number: 4242424242424242
month:03
year:2031

```
The [stripe testing](https://stripe.com/docs/testing) docs specify thay any number can be used for the "month"
and the "year"fields however when I just put the card number specified above 
and random digits in the "month" and "year" fields  i would get two errors: 

* in dev tools: " (index):3 POST https://api.stripe.com/v1/tokens 402 "
* In the app itself : "we are unable to make payment with this card" this is the result
of the else code:
```
if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
...
       else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card")
```

overall the payment system does work as when I made a payment I checked on my stripe payment via my stripe 
account as seen [here](https://github.com/xxkaminaxx/XxRelix4U/blob/master/static/images/test-pay.jpg)
however there is no indication that the payment is made via the users end. i wasnt able to get to the bottom of this as I didn't have enough time. 




