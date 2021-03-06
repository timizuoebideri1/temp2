from nautobot.dcim.models import Site
from nautobot.extras.jobs import *

import time



class CustomFieldCreation(Job):

    class Meta:
        name = "Create Logs"
        description = "Provision a new branch site"

    def run(self, data, commit):
        for x in range(500):
            time.sleep(1)
            site = Site.objects.first()
            self.log_success(obj=site, message="Created new site")
            self.log_info(obj=site, message="Creating Custom Fields")

            output = ["device creation", "device okay"]

        return '\n'.join(output)

    # def post_run(self):
    #     for x in range(2000):
    #         time.sleep(1)
    #         self.log_info(message=f"POST RUN REACHED INFO - {x}")

