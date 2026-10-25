
# CS 340 Portfolio — Grazioso Salvare Rescue Dashboard

**Cristian Alejandro**  
**Southern New Hampshire University**  
**CS 340: Client/Server Development**

## Project Overview

For Project Two, I developed a dashboard to help Grazioso Salvare review Austin Animal Center records and identify dogs that might be good candidates for rescue training.

The dashboard connects to MongoDB through a reusable Python CRUD module. Users can filter animals for water rescue, mountain or wilderness rescue, and disaster or individual tracking. They can also review a data table, a breed chart, and a map showing a selected animal's location.

## How do you write programs that are maintainable, readable, and adaptable?

I try to keep my programs organized by giving each part of the code a clear job. In this course, I built a Python CRUD module for Project One and reused it in Project Two to connect my dashboard to MongoDB.

Instead of putting all the database connection and query code inside the dashboard, I kept those operations in the `AnimalShelter` class. This made the dashboard code easier to read and helped me avoid repeating the same code in different places.

If I need to change how the database is accessed later, I can work on the CRUD module without rewriting the entire dashboard. I could also reuse this module in another application that needs to search or update animal records, such as a shelter management tool.

## How do you approach a problem as a computer scientist?

I start by looking at what the client needs and breaking the work into smaller tasks. For Grazioso Salvare, I needed to understand which animal records would be useful for different rescue categories, how to query those records, and how to display them in a way that people could actually use.

I worked on the database connection first, then connected it to the dashboard filters, table, chart, and map. This felt different from some earlier assignments because the pieces had to work together as one application rather than just producing one correct output.

In the future, I would continue by reviewing client requirements, planning the database fields and queries, testing with sample records, and checking that the final interface gives users accurate results.

## What do computer scientists do, and why does it matter?

Computer scientists solve problems by creating systems that organize information and make tasks easier. They do more than write code; they also have to think about how people will use the software and whether it works correctly.

My Grazioso Salvare dashboard is an example because it turns a large collection of shelter records into information that is easier to search and understand.

Instead of checking animal records one by one, a rescue organization can use the filters and visualizations to narrow down possible training candidates. A tool like this could save time, support better decisions, and let staff focus more of their effort on helping animals and people.

## Portfolio Artifacts

This repository includes the following files from my CS 340 coursework:

- **ProjectTwoDashboard.ipynb** — Final interactive dashboard created for Project Two.
- **CRUD_Python_Module.py** — Reusable Python module that connects to MongoDB and performs CRUD operations.
- **CS340 Project Two README.docx** — Project Two documentation with explanations and screenshots.
- **Grazioso Salvare Logo.png** — Logo used in the dashboard.

## Skills Demonstrated

Throughout this project, I gained experience with:

- Python programming
- MongoDB database operations
- CRUD functionality
- Client/server development
- Dash dashboard development
- Database filtering and queries
- Data visualization
- Debugging and troubleshooting
- Writing reusable and maintainable code

## Conclusion

This project helped me understand how different parts of an application work together. I learned how to connect a database to a user interface and present information in a way that is useful to the client.

As I continue working toward my computer science degree and a career in software development, I plan to use these skills to build applications that solve real-world problems.
