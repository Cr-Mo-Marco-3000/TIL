# 쓰레드

## 1. 메인 스레드

모든 자바 프로그램은 메인 스레드가 main() 메서드를 실행하면서 시작된다.

메인 스레드는 main() 메서드의 첫 코드부터 순차적으로 실행되고, main() 메서드의 마지막 코드를 실행하거나 return을 만나면 종료된다.

메인 스레드에서는 다른 작업 스레드들을 만들고 실행시킬 수 있다.

싱글 스레드에서는 메인 스레드가 종료되면 프로세스도 종료되는 반면, 
멀티스레드에서는 실행중인 스레드가 하나라도 있다면 프로세스는 종료되지 않고 모든 스레드가 종료될 때까지 기다린다.

작업 스레드보다 메인 스레드가 먼저 종료될 수도 있다는 것을 기억하자.



## 2. 작업 스레드 직접 생성

1. Thread에 Runnable 객체를 인자로 집어넣은 후, 오버라이딩한 `run()`메서드에 실행시킬 코드를 작성, start() 메서드로 해당 스레드를 실행

2. Thread에 Runnable를 집어넣는 대신 그 자체를 상속한 후 run()메서드를 재정의해서 사용도 가능하다.
   - 단, Runnable의 익명 클래스를 만드는 것과 같이 Thread 익명 클래스를 만들어서 더 많이 사용된다.

1. Runnable 인터페이스의 run() 사용
   - 상속 등 확장성을 위해 많이 사용.

```java
package com.main_thread;

public class Main {

	public static void main(String[] args) {
		// Runnalbe은 스레드가 작업을 실행할 때 사용하는 인터페이스
		// Runnable 인터페이스를 매개변수로 받아서 작동
		Thread thread = new Thread(new Runnable() {
			@Override
			public void run() {
				for(int i=0; i< 5; i++) {
					System.out.println("내부 스레드 실행: " + i);
					try {
						Thread.sleep(500);			// 스레드를 0.5초간 일시정지
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
				}
			}
		});
		
		// 작업 스레드를 실행
		thread.start();
		for (int i=0; i < 5; i++ ) {
			System.out.println("외부 스레드 실행: " + i);
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}

}

```

2. Thread의 run 사용

```java
package com.main_thread;

public class Main {

	public static void main(String[] args) {
		// Runnable은 스레드가 작업을 실행할 때 사용하는 인터페이스
		// Runnable 인터페이스를 매개변수로 받아서 작동
		Thread thread = new Thread() {
			@Override
			public void run() {
				for(int i=0; i< 5; i++) {
					System.out.println("내부 스레드 실행: " + i);
					try {
						Thread.sleep(500);			// 스레드를 0.5초간 일시정지
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
				}
			}
		};
		
		// 작업 스레드를 실행
		thread.start();
        
		for (int i=0; i < 5; i++ ) {
			System.out.println("외부 스레드 실행: " + i);
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}

}

```



## 3. 스레드 이름

각 스레드는 자신의 이름을 가지고 있는데, 메인 스레드는 main이라는 이름, 작업 스레드는 자동적으로 Thread-n이라는 이름을 가진다.

`thread.setName("스레드 이름")` 메서드를 통해 스레드의 이름을 바꿔줄 수 있다.

스레드 이름은 디버깅할 때 어떤 스레드가 작업을 하는지 조사할 목적으로 주로 사용된다.

`Thread.currentThread();`로 현재 Thread의 정보를 얻은 후, getName()으로 스레드의 이름을 얻는다.

```java
package com.main_thread;

public class Main {

	public static void main(String[] args) {
		
		Thread mainThread = Thread.currentThread();							// 해당 코드를 실행하는 스레드 객체 참조 얻기
		System.out.println(mainThread.getName());
		
		for (int i = 0; i<5; i++) {
			Thread subThread = new Thread() {
				@Override
				public void run() {
					System.out.println("서브스레드 이름: " + getName());		// getName으로 해당 스레드의이름 얻기
				}
			};
			subThread.start();
		}
		
		for (int j=0; j<5; j++) {
			Thread subThread2 = new Thread(new Runnable () {
				@Override
				public void run() {
					System.out.println(Thread.currentThread().getName()+ "실행");	
				}
			});
			subThread2.setName("쓰레드" + j);								  //작업 스레드 이름 변경
			subThread2.start();
		}
	}

}

```



## 4. 스레드 상태

start() 메서드를 호출하더라도, 곧바로 스레드가 실행되는게 아니라, 실행 대기상태(Runnable)이 된다.

실행 대기하는 스레드는 CPU 스케쥴링에 따라 CPU를 점유하고 run() 메소드를 실행한다. 이때를 실행(Running) 상태라고 한다.

해당 스레드의 run()을 모두 실행하기 전에 Runnable로 돌아갈 수 있다. 그리고 다른 스레드가 실행 항태가 된다.

이렇게 스레드는 실행 상태와 대기 상태를 번갈아가며 자신의 run() 메소드를 조금씩 실행하다가, run() 메소드를 모두 실행하면 종료되게 된다.

이 종료 상태를 Terminated라고 한다.

**실행상태에서 일시 정지 상태로 가기도 하는데**, 일시정지 상태는 해당 스레드가 실행할 수 없는 상태를 말한다.

다시 실행 상태로 가기 위해서는 일시정지 상태에서 실행 대기상태로 돌아가야 한다.

다음은 상태전환을 위한 메소드들이다.

1. 실행 -> 일시정지
   - `sleep(long millis)`
     - 주어진 시간 동안 일시정지
   - `join()`
     - join()을 붙인 스레드가 종료될 때까지, join()을 소환한 스레드를 대기시킨다.
   - `wait()`
     - 동기화 블록 내에서 스레드를 일시 정지 상태로 만든다
     - Object()의 메서드

2. 일시정지 -> 실행 대기
   - `interrupt()`
     - 일시 정지 상태일 경우, interruptedException을 발생시켜 실행 대기 상태 또는 종료 상태로 만든다.
   - `notify()`, `notifyAll()`
     - wati() 메소드로 인해 일시 정지 상태인 스레드를 실행 대기 상태로 만든다.
     - Object()의 메서드

3. 실행 -> 실행대기
   - `yield()`
     - 실행 상태에서 다른 스레드에게 실행을 양보하고 실행 대기 상태가 된다.

### 1. sleep()

- 주어진 시간 동안 일시 정지
- milisecond단위로 숫자 설정
- InterruptedException이 발생 가능하기에 예외 처리 필수

```java
try {
    Thread.sleep(1000);
} catch (InterruptedException e) {
    
}
```



### 2. join()

- 다른 스레드가 종료될 때까지 기다렸다가 실행을 해야 하는 경우

```java
package com.main_thread;

class SumThread extends Thread {
	private long sum;
	
	public long getSum() {
		return sum;
	}
	
	public void setSum(long sum) {
		this.sum = sum;
	}
	
	@Override
	public void run() {
		for(int i = 1; i <= 100; i++) {
			sum += i;
		}
	}
}

public class Main {
	public static void main(String[] args) {
		
		SumThread sumThread = new SumThread();
		sumThread.start();						// sumThread 실행시킴 
		try {
			sumThread.join();					// sumThread가 종료될 때까지 main thread를 일시정지시킨다. 
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		System.out.println("1 ~ 100 합: " + sumThread.getSum());
	}
}

```

### 3. yield()

` yield()`를 호출한 스레드는 실행 대기 상태로 돌아가고, 다른 스레드가 실행 상태가 된다.

```java
package com.main_thread;

class WorkThread extends Thread {
	public boolean work = true;
	
	public WorkThread(String name) {
		setName(name);
	}
	
	@Override
	public void run() {
		while(true) {
			if(work) {
				System.out.println(getName() + ": 작업처리");
			} else {
				Thread.yield();
			}
		}
	}
}

public class Main {
	public static void main(String[] args) {
		WorkThread threadA = new WorkThread("workThreadA");
		WorkThread threadB = new WorkThread("workThreadB");
		
		threadA.start();
		threadB.start();
		
		try {
			Thread.sleep(5000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		threadA.work = false;		// ThreadA로 계속해서 들어가지만, yield()를 만나는 즉시 실행 대기 상태로 바꿈 => continue와 비슷
		
		
		try {
			Thread.sleep(10000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		threadA.work = true;
	}
}

```

