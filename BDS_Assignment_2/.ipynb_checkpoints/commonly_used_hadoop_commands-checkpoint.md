# To list directory

hadoop fs -ls /home/vinayak/hdfs_output

# To display contents of file

hadoop fs -ls /home/vinayak/hdfs_output/part-00000

# To execute a map-reduce job

## Country Job
hadoop jar /home/vinayak/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/transactions_per_country/mapper.py -mapper mapper.py -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/transactions_per_country/reducer.py -reducer reducer.py -input /assignment2_retail_data.csv -output /home/vinayak/country_output/

## Customer Job
hadoop jar /home/vinayak/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/transactions_per_customer/mapper.py -mapper mapper.py -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/transactions_per_customer/reducer.py -reducer reducer.py -input /assignment2_retail_data.csv -output /home/vinayak/customer_output/

# Report-Generation Job
hadoop jar /home/vinayak/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/report_generation/mapper.py -mapper mapper.py -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/report_generation/reducer.py -reducer reducer.py -input /assignment2_retail_data.csv -output /home/vinayak/temp/

# Map Reduce with Command Line Arguments
hadoop jar /home/vinayak/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/report_generation/mapper.py -mapper mapper.py -D mapper.pattern="hello_world" -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/report_generation/reducer.py -reducer reducer.py -input /assignment2_retail_data.csv -output /home/vinayak/temp/


# To put a file in hdfs

hdfs dfs -put /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/data/assignment2_retail_data.csv /home/vinayak/hdfs_input

# To delete a directory from hdfs

hdfs dfs -rm -r /home/vinayak/temp