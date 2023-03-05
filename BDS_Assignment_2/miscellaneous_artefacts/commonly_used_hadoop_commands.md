# To list directory

hadoop fs -ls /home/vinayak/hdfs_output

# To display contents of file

hadoop fs -ls /home/vinayak/hdfs_output/part-00000

# To execute a map-reduce job

## Query 2
hadoop jar /home/vinayak/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_2/mapper.py -mapper mapper.py -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_2/reducer.py -reducer reducer.py -input /hdfs_input/assignment2_retail_data_utf8.csv -output /home/query2_output/

## Query 3
hadoop jar /home/vinayak/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_3/mapper.py -mapper mapper.py -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_3/reducer.py -reducer reducer.py -input /hdfs_input/assignment2_retail_data_utf8.csv -output /home/query3_output/

## Query 4
hadoop jar /home/vinayak/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_4/mapper.py -mapper mapper.py -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_4/reducer.py -reducer reducer.py -input /hdfs_input/assignment2_retail_data_utf8.csv -output /home/query4_output/

## Query 5
hadoop jar /home/vinayak/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_5/mapper.py -mapper mapper.py -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_5/reducer.py -reducer reducer.py -input /hdfs_input/assignment2_retail_data_utf8.csv -output /home/query5_output/

## Query 6
hadoop jar /home/vinayak/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_6/mapper.py -mapper mapper.py -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_6/reducer.py -reducer reducer.py -input /hdfs_input/assignment2_retail_data_utf8.csv -output /home/query6_output/

## Query 7
hadoop jar /home/vinayak/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_7/mapper.py -mapper mapper.py -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_7/reducer.py -reducer reducer.py -input /hdfs_input/assignment2_retail_data_utf8.csv -output /home/query7_output/

## Customer Job
hadoop jar /home/vinayak/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/transactions_per_customer/mapper.py -mapper mapper.py -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/transactions_per_customer/reducer.py -reducer reducer.py -input /assignment2_retail_data.csv -output /home/vinayak/customer_output/

# Report-Generation Job
hadoop jar /home/vinayak/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/report_generation/mapper.py -mapper mapper.py -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/report_generation/reducer.py -reducer reducer.py -input /assignment2_retail_data.csv -output /home/vinayak/temp/

# Map Reduce with Command Line Arguments
hadoop jar /home/vinayak/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/report_generation/mapper.py -mapper mapper.py -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/report_generation/reducer.py -reducer reducer.py -input /assignment2_retail_data.csv -output /home/vinayak/temp/

# For filtering
hadoop jar /home/vinayak/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_data/mapper.py -mapper mapper.py -input /assignment2_retail_data.csv -output /home/vinayak/filter_output/


# To put a file in hdfs

hdfs dfs -put /home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/data/assignment2_retail_data_utf8.csv /home/vinayak/hdfs_input

# To delete a directory from hdfs

hdfs dfs -rm -r /home/vinayak/temp