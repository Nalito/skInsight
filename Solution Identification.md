# Solution Identification

## skInsight
skInsight is an expert system that leverages computer vision in identifying skin defects present in images, and recommending local skincare firms, vendors, and consultants to people with the need for skincare products or consultation. The system makes use of ResNet50, a popular computer vision model in identifying skin defects present in images.


### Justification of Choice
This solution was selected for the following reasons:
1. **Contribution to the local market**: Through the proposed recommendation algorithm of skInsight that will prioritize quality local products of imported ones. People would be enlightened on the presence and importance of using local skincare products. This would contribute to the nation's GDP and internal revenue.
2. **Improved adoption of skincare products**: A lot of people have bad sentiments about skincare products because they have used either a bad skincare product or the wrong one in the past, and the trauma of the side effects of using those products still haunt them. skInsight offers a platform that educates people on the use of the right skincare products for the right defects, and also recommends proper products they can use to treat identified skin defects.
3. **Solves the problem of shortage of dermatologists**: A lot of locations have an acute shortage of dermatologists, and even when these professionals are present, not everyone can afford them. skInsight is an expert system that bridges the gap between the less priviliged and access to quality skincare consultations.

### Scope of solution
1. **Training Data**: The dataset used for this solution was sourced from Google's SCIN data [repository](http://research.google/blog/scin-a-new-resource-for-representative-dermatology-images/). The Skin Condition Image Network (SCIN) dataset is a valuable resource for researchers and developers working on dermatology-related projects. It offers a diverse and representative collection of skin condition images, addressing the limitations of existing datasets that often lack diversity and focus on specific conditions.
2. **Defect Identification**: The first MVP would be trained on a select number of skin defects and subsequent progressions would be trained on a wider range of defects.
3. **Deployment**: skInsight is to be deployed on a web application for easy consumption by the target customers. 
4. **Skincare Recommendation System**: The first MVP of skInsight would focus majorly on the development of a highly accurate computer vision model that can process imput images to identify skin defects present in them. Subsequent MVPs would include an expert system that collaborates with skincare vendors and firms to recommend skincare products that can be used to treat the identified skincare defects.
