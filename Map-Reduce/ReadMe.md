

- Goal:ttempt to identify the default number of companies from the CSV file.

- Use the core concepts, HDFS and MapReduce of Big Data Hadoop Platform to solve the problem.

- Processing large volumes of data in parallel by dividing the work into a set of independent tasks.(Assuming our csv is big data)

- Use MapReduce process file to break it into chunks and process it in parallel.(how the code works underhood to achive scalability)

Mapper:

- This function works by dividing the large input into smaller sub-problem inputs, which are then distributed to nodes. Each node further divides the sub-tasks into smaller sub-sub tasks. After the processing is complete, the data is mapped into key-value pairs. Before being sent to the reducer function, the key-value pairs are shuffled and sorted based on their keys.

Reducer:

- This function is  used for processing tasks such as calculating the total count for each key or performing other types of analysis. It typically produces a single result or set of results based on the input data.