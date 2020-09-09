Steps to execute Sparkify 7 file in  cluster shell:

1)Enter the ssh command : ssh -i C:\Users\nskir\Desktop\UNH\Scalable\Sparkify-6\spark.pem hadoop@ec2-3-235-134-222.compute-1.amazonaws.com

2)We need to "unset PYSPARK_DRIVER_PYTHON" in shell

3)Open file in vi.s7.py

4)Run spark-submit s7.py on shell

5) output file is created in s3 bucket.