function fn() {
  const uuid = java.util.UUID.randomUUID();
  const config = {
    headers: {
      'Message-Id': uuid,
    },
    urlBase: 'https://reqres.in/api'
  };

  karate.configure('connectTimeout', 2000);
  karate.configure('readTimeout', 2000);
  karate.configure('ssl', true);
  return config;
}
