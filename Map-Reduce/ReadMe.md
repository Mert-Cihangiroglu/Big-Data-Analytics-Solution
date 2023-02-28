

Goal: Attempt to identify the default and non default number of companies where Operating Profit Rate is greater than 0.5 in the CSV file.

Mapper:

- This function works by dividing the large input into smaller sub-problem inputs, which are then distributed to nodes. Each node further divides the sub-tasks into smaller sub-sub tasks. After the processing is complete, the data is mapped into key-value pairs. Before being sent to the reducer function, the key-value pairs are shuffled and sorted based on their keys.

Reducer:

- This function is  used for processing tasks such as calculating the total count for each key or performing other types of analysis. It typically produces a single result or set of results based on the input data.

- Comment to start the job: hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.0.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input data/data.csv -output output
