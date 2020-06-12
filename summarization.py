from transformers import pipeline

summarizer = pipeline("summarization")

ARTICLE = """ The landscape of the business world changes every day. With every new business offering better products and solutions, the competition is getting tougher and only the fittest and smartest can survive. In this context, a business should identify its key focus areas and find out where they need to improve to increase their sales or to make their operations more efficient. Providing better customer experience, automating lead follow-ups etc can help a business perform better, but it comes at the cost of needing more human resources. Trouble is, increasing human resources isn’t a solution because no number of people is ever sufficient to process the ever-growing data generated in a business or to engage with the increasing number of customers. So, how can an enterprise overcome this challenge?

Artificial Intelligence (AI) can be used to solve problems across the board. It can help a business increase sales, improve customer experience, automate work processes, provide predictive analysis etc. From conversational tools to driverless cars, AI in various shapes and forms is transforming industries. Today, AI-assisted job automation is emerging as a norm for businesses; and enterprises. Those who adapt will survive the competition and those who delay will perish in the long run. By the time a late adopter completes system development, integration, interaction learning, and AI application governance, early adopters will have taken up a considerable market share and will be operating at substantially lower costs with enhanced performance.
"""

print(summarizer(ARTICLE, max_length=130, min_length=30))