# Lee Pancoast

## CS499 - Computer Science Capstone


### Professional Self-assessment

When I was in fourth grade my family bought our first computer. Ever since then, I have been an avid enthusiast of everything related to computers: software, hardware, programming, you name it. With that first computer, and while still in elementary school, I learned how to type extremely well, and how to navigate, customize, (break,) and fix the operating system. Before middle school was over, I was taking apart computers, swapping components, remotely controlling friend’s computers (non-malicious pranks, of course), and programming simple web pages. It wasn’t until early in my adulthood that I began having the desire to pursue this passion as a career. More specifically, out of the various programming ventures I have undertaken, there have been some that have really made an impact with past (and current) employers. Seeing something I had programmed have a meaningful impact on a business really made want to do it full-time; with that, I began applying for jobs. Unfortunately for me (however understandable), most employers wanted a formal education for those applying for Software Engineer positions. Despite the years of self-learning and albeit small, collection of software projects being actively used, it appeared that without a degree I would have a hard time of pursing my goal of becoming a Software Engineer. Thus, began my journey at SNHU.

My adventure in the Computer Science program at SNHU has accomplished many things for me both on personal and professional levels. In a technical sense, I have learned and grown to love new programming languages like Python and Java. I’ve learned how to create server-side applications and use non-relational databases, like MongoDB. I’ve had the opportunity to gain exposure to the emerging fields of AI and ML, and create simple applications utilizing those technologies. I’ve learned the means and importance, of testing and debugging as well as, writing clean, semantic, re-usable and maintainable code. Of the many experiences in my time at SNHU, one of the most important, intangible, aspects I’ve grown to appreciate is collaborating in a team environment specifically, how to be an effective contributor. As a project’s size and complexity increases, so does the need for teamwork. Similarly, as a project changes and/or evolves, collaboration with management and the clients are also vital. While I have learned many new topics, technologies, and theologies in regard to the field of computer science, my experience has also been humbling. While I would have considered myself as have knowing a lot about computers prior to attending SNHU, my experience here has revealed that even after all of my courses, I have only scratched the surface of computer science.  I’ve come to learn, that being a software engineer is a process of evolution; I began that journey many years ago but, SNHU has helped to make me more well-rounded and enhanced my capabilities of seeing the big picture. Furthermore, my experiences here at SNHU have also helped affirm the area of Computer Science I wish to be a part of, cyber security. Some of the topics covered in the program, including but not limited to, hash algorithms and cryptography, gave me new insight into how security works and has led to my desire for further research into this area.

As part of my e-portfolio, I have included a code review and enhancements for a software artifact that I created in a previous class at SNHU. The enhancements to the artifact were targeted for three specific areas: _Software Design and Engineering_, _Algorithms and Data Structures_, and, _Databases_. These documents will help to showcase some of my new, and improved upon, abilities such as: using Python, creating a RESTful API, creating server- and client-side components, and using non-relational databases. Additionally, a common element of security was applied to reveal my interest in the field.

### The artifact

The artifact is a RESTful API that I created in the end of 2019 for CS-340 at SNHU. The API is written in Python and is designed to perform operations on a Mongo database. In regard to the Software Design and Engineering category, I have chosen this artifact because it follows a popular design technique, REST, and uses one of the languages I am most confident in, Python. The API shows my ability to use the Python language proficiently, as well as, my capabilities of creating simple and elegant solutions. In regards to the Algorithms and Data Structure category, I feel this artifact showcases my ability to create functionality while adhering to simplicity. The functions are not overly complex, and, I use only the necessary data structures to accomplish the task which, initially was a simple variable. In regard to the Databases category, I feel this artifact showcases my ability to use NoSQL databases specifically, MongoDB as well as, perform basic CRUD functions and advanced queries.

### Code Review
This is my [code review](https://youtu.be/IXFesAuqato) of my selected artifact. (re-directs to YouTube)

### Enhancement One - Category: _Software Design and Engineering_
[Improvements](source/api/enhancedFinalREST.py) of the artifact as they relate to the category, software design and engineering, have been made to include the use of static routing, a custom JSON encoder, and HTTP request error handling. Originally, the API used dynamic routing to handle HTTP requests as they pertained to which CRUD operation to perform on the database. The original enhancement was to replace all of individual routes with one dynamic route that would parse the entire query into the appropriate command and document data. The revised enhancement uses a static route for each CRUD operation and passes the database data as JSON through the HTTP request data. This presented fewer challenges, had better data obscurity, and followed the principles of REST more closely. A custom JSON encoder function was also implemented to encode/decode MongoDB’s ObjectId and datetime formats. Originally the document ID was ignored due to the lack of support from the JSON module however, without using the document ID to filter documents, duplication of data was inevitable. Lastly, HTTP request errors are handled by returning a custom response status and message.
Overall, my experience with enhancing this artifact has been positive, informative, and successful. One of the more surprising things I have learned is that the bottlepy framework does not have any built-in security methods such as SSL/TSL; at least as what’s available via the documentation. The biggest challenge I faced was encoding and decoding JSON when attempting to use a document’s ID and date fields. However, I learned how to create my own JSON encoder and thus, improved the functionality of the API. 

### Enhancement Two - Category: _Algorithims and Data Structures_
[Improvements](source/api/enhancedFinalREST.py) of the artifact as the relate to the category, algorithms and data structure, have been made to include a list, data validation of function arguments, and a close connection statement. The new list contains elements that represent the allowed document fields in the database collection. These are used to valid the HTTP request contents prior to acting on the database thus, improving security of the API and integrity of the database. As an added benefit, should the request come from a place other than the client-side web interface (e.g. cURL), the validation within the API will preserve this security. The close connection statement that was added was previously not included; the statement to close the database should have been there all along so, although technically not an enhancement as much as it is a fix, it nonetheless improves security and integrity of the database. In Module One, I outlined a plan to include data structures to use in data validation. I have successfully completed this plan as well as achieved course outcomes of: having a security mindset, solving a problem using standards and practices appropriate for the solution, and, delivering value through use of skills and tools in computer science.
Overall, my experience with enhancing this artifact has been positive and successful. I was able to build upon my previous enhancement of the artifact from the previous module, and, complete my planned enhancement for this module. One of the things I learned while working on this artifact, while not particularly useful in this case, is that an instance of a MongoClient can support multiple independent databases. The biggest challenge I faced initially with the most recent enhancement was deciding when to perform the data validation – in the HTML interface, or, in the API itself. Ultimately, I decided to use both because if the API was accessed via an address bar (i.e. outside of the client-side web interface), for example, there would be no validation. By having some validation in the API, security and integrity can be maintained from any origin that calls the API’s function.

### Enhancement Three - Category: _Databases_
[Improvements](source/html/index.html) of the artifact as the relate to the category, databases, have been made to include an HTML/JavaScript interface. The interface not only presents and easy to use platform for users to interact with the database through the API, it also is the first point of data validation. The user chooses a pymongo command via buttons and inputs document field data through various input fields which, limits the available options to what has been pre-defined. In Module One, I outlined a plan to implement a web interface for the database/API. I have successfully completed this plan as well as achieved course outcomes of: having a security mindset, solving a problem using standards and practices appropriate for the solution, and, delivering value through use of skills and tools in computer science.
Overall, my experience with enhancing this artifact has been again, positive and successful. I was able to improve my original artifact, and, complete my planned enhancement for this module. I’ve learned and improved my skills in several areas with this enhancement. For example, I have used the Vue JavaScript framework for implementing the scripting portion of my webpage as well as, the Axios framework for handling HTTP requests to and from the REST API. I’ve also improved my capabilities in terms of styling and rendering responsive web layouts using HTML5 and CSS3. In addition, and in response to problems caused by the same, I learned how to deal with and overcome cross-origin-resource-sharing.

[Client Interface](img/client-interface/main.PNG)

[Instant Search](img/client-interface/search.PNG)

[Modal dialog](img/client-interface/update.PNG)
