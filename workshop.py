from job import Job

class Workshop:
    def load_job(self, job: Job):
        print("Workshop received job:")
        job.summary()
