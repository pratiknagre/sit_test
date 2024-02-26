studies in following topics=
1. sql-joins like inner,left,right,self joins
2. sub-query like outer query using inner query
3. window fuctions = it is advance level of sql
4. generate CSV file Report using python & using pandas ,matplotlib & boto3 liabraries.
5. managing code repository using git & i am using git to version control code ,track changes & collaborate with team member.
6. exporting CSV FILE rEPORT TO S3 bucket in AWS cloud system.


def generate_report():
    report_content="This is a sample report."
# save the report to a file
    with open('report.txt','w') as f :
        f.write(report_content)

def export_report_to-s3():
# setup the s3 client
s3=boto3.client('s3')
with open ('report.txt','rb') as f :
    s3.upload_fileobj(f,'my-s3-bucket','reports/report.txt'):

    PANDAS LIABRARY
# high performance data analysis tool
# working with large data set
# supports or load data set
# more flexible
# represents in tabular way(row & columns)
# working on missing data 
# indexing-slicing-subsetting the large datasets
# merge & join two different datasets easily.git