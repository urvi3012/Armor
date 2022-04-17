<p>
  <h1 align="center"><b> ⭐ Armor ⭐</h1>
</p>


## Inspiration

The United States stands at 56th position with a crime index of 47.8 in the world. Also, the total crime rate of the US is much higher than that of other developed countries. Crime like assaults, gun shootings, murder, robbery, and others happen due to many factors. The most affecting factor is the lack of awareness amongst corps and the victim. Alerting people about safe and unsafe locations can help us reduce the crime rate.
Notifying the corps of the probability of crimes can increase surveillance and make a huge difference.

## What it does

The Armor is an alert application that takes the gender and age of a person and sends them a message alert when they enter an unsafe zone. It also provides the functionality to report a crime, call a friend, or emergency when in trouble. I aimed to ensure user safety and reduce crime rates.

The idea of this application came after I read the sad news of the mass gun shooting in Sacramento on April 3rd, 2022. It was so upsetting and disturbing to know about injured and murdered victims. HackDavis provided us with an opportunity to implement it. 


## How I built it

I started by collecting the dataset while merging it with some existing datasets. I analyzed and visualized all the datasets and combinations using four distinct integrated Tableau dashboards. Also, I built several models like Linear Regression, Random Forest Classifier, Gradient Boosting, and Google VertexAI AutoML Model. The model gave us an average accuracy of around 96%. The models classified locations as safe and unsafe locations and sent Twilio message notifications to the user when in the danger zone. Moreover, it also gave functionality of calling emergency (Twilio), calling a friend (Twilio), and reporting a crime.

## Challenges I ran into
The happening of a crime depends on several factors. The major challenge was to scrape websites to create the recent dataset and merge different existing datasets. I analyzed five distinct datasets and their combinations. Starting from gunshots, crimes per county, unemployment, education level, and types of crime, to the crime per year dataset.

Another challenge was extracting the real-time location of the user and training the machine learning models with high accuracy. Also, I tried using StreamLit but unfortunately, I wasn't able to make it work.


## Accomplishments that I'm proud of

I am proud of developing an idea with exactly the same functionalities I thought of. High accuracy of the Machine Learning model while merging multiple datasets also gave us satisfaction. Also, embedding Tablue into the Flask framework is an achievement for us.

## What I learned

I learned to embed Tableau into the Flask web app. Also, it was fun using Twilio. I also learned to augment data by actual scraping rather than data augmentation for good model building. Apart from tech, I learned teamwork and different concepts from participants in the hackathon.

## What's next for Armor

With the Report Crime button, we can further add to the dataset. Also, the dataset can be used to send alerts to corps by predicting the trend of possible crimes to happen and decreasing the probability.  Also, states can use it to amend the gun laws according to the gun shoot crime rates per state.
