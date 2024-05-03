package co.com.pruebasqa;

import com.intuit.karate.Results;
import com.intuit.karate.Runner;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestParallel {

    private final static int WORKERS = 1;

    @Test
    public void testAll() {
      Results results = Runner.path()
              .outputCucumberJson(true)
              .relativeTo(getClass())
              .parallel(WORKERS);
      assertEquals(0, results.getFailCount(), results.getErrorMessages());
    }
}
