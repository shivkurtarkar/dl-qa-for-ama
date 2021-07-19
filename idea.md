
Project : Semantic Search for ama qa

Initial Idea: I wanted to scrape slack #ama_session channel and use question answering model from listed on Stanford Question Ansering Dataset (SQuAD) Challange page [https://rajpurkar.github.io/SQuAD-explorer/].

initial components were
1. scrapper
	to scrape slack channel
2. filter
	rate the text to see if there is factual data. if it passes threshold add it to dataset.
3. semantic search v1 
	semantic search using transformer + faiss 
	in python + flask
4. semantic search v2
	semantic search using transformer + faiss 
	in c++ + cpprestsdk
5. gateway
	micro service to allow us to configure how much traffic we want to shift to which micro service
6. front end


refrences:
c++ micro service
https://medium.com/@ivan.mejia/modern-c-micro-service-implementation-rest-api-b499ffeaf898

https://github.com/Microsoft/cpprestsdk

semantic search
https://kstathou.medium.com/

https://blog.onebar.io/building-a-semantic-search-engine-using-open-source-components-e15af5ed7885

https://towardsdatascience.com/billion-scale-semantic-similarity-search-with-faiss-sbert-c845614962e2

https://medium.com/@khanadnanxyz/communications-how-d7516a2d4e6d