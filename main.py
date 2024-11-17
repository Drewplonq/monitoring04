import sentry_sdk

sentry_sdk.init(
    dsn="https://49e057bace2668d6713bfd7ff78e15d4@o4508314378698752.ingest.de.sentry.io/4508314702315600",
    environment="develop",
    release=1.0
)

if __name__ == "__main__":
    division_zero = 1 /0