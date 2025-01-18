class ReportServicce:
    def __init__(self, report_repository):
        self.report_repository = report_repository

    def send_report(self, report_id):
        return self.report_repository.send_report(report_id)