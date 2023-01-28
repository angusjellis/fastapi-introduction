Project: create an example car dealership internal website.



Examples of user stories:

"As a manager at this car dealership, I want to see who has sold the most cars (in the past x amount of time)."
"As an accountant, I want to be able to calculate total sales for the business for the past month."
"As a public user, I want to see what cars are for sale at this dealership."
"As a car salesperson, I want to add new cars for sale."
"As a car salesperson, I want to be able to calculate how much commission I will receive this month."
"As a shady manager, I want to adjust the car comission formula to stop my employees from getting too much money."
"As a manager, I want to know which dealerships are selling the most."

As we can see, some data returned by the API will/may be public.

Other data may need to be locked down to JWT auth (and maybe also only be available to certain groups of users, or even individual users).

We will start off as a purely internal facing website. But with a view to showing the public what cars are for sale.

MINIMUM VIABLE PRODUCT

A website that shows all sales for the business.