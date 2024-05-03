function fn() {
  const uuid = java.util.UUID.randomUUID();
  const config = {
    headers: {
      'Message-Id': uuid,
    },
    urlBase: 'https://g3dq9810zj.execute-api.us-east-1.amazonaws.com/qa'
  };

  karate.configure('connectTimeout', 2000);
  karate.configure('readTimeout', 2000);
  karate.configure('ssl', true);
  return config;
}
