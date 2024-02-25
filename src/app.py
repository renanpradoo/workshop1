from frontend import ExcelValidatorUI
from backend import process_excel, excel_to_sql
import logging
import sentry_sdk

sentry_sdk.init(
    dsn="https://0b1f5be457ec3280ac26b53c66ad0225@o4506804869332992.ingest.sentry.io/4506804896137216",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)



def main():
    ui = ExcelValidatorUI()
    ui.display_header()

    upload_file = ui.upload_file()

    if upload_file:
        df, result, errors = process_excel(upload_file)
        ui.display_results(result, errors)

        if errors:
            ui.display_wrong_message()
            logging.error("Planilha com formato incorreto.")
            sentry_sdk.capture_message("Sentry: Planilha com formato incorreto.")
        elif ui.display_save_button():
            excel_to_sql(df)
            ui.display_success_message()
            logging.info("SQL atualizado com sucesso.")
            sentry_sdk.capture_message("Sentry: SQL atualizado com sucesso.")
            
if __name__ == "__main__":
    main()