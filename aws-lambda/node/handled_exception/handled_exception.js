const Sentry = require('@sentry/node');

exports.handler = async function (event, context, callback) {
  Sentry.init({
    dsn: "<your DSN>",
  });

  try {
    undefinedFunCall(); // call undefined function.
  } catch (e) {
    Sentry.captureException(e); // Capture the exception in the Sentry dashboard.
    await Sentry.flush(2000);
  }

  const response = {
    statusCode: 200,
    body: "Handled exception",
  };

  callback(null, response);
};