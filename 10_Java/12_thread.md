# 쓰레드

## 0. 프로세스 vs 쓰레드

스레드로 구현된 자바 서버(서블릿, JSP)

## 1. 메인 스레드

모든 자바 프로그램은 메인 스레드가 main() 메서드를 실행하면서 시작된다.

메인 스레드는 main() 메서드의 첫 코드부터 순차적으로 실행되고, main() 메서드의 마지막 코드를 실행하거나 return을 만나면 종료된다.

메인 스레드에서는 다른 작업 스레드들을 만들고 실행시킬 수 있다.

싱글 스레드에서는 메인 스레드가 종료되면 프로세스도 종료되는 반면, 
멀티스레드에서는 실행중인 스레드가 하나라도 있다면 프로세스는 종료되지 않고 모든 스레드가 종료될 때까지 기다린다.

작업 스레드보다 메인 스레드가 먼저 종료될 수도 있다는 것을 기억하자.

우선권은 5이다.

- 스레드의 단계
  - 시작
  - 준비
  - 실행
  - blocked
  - 제거

## 2. 작업 스레드 직접 생성

1. Thread에 Runnable 객체를 인자로 집어넣은 후, 오버라이딩한 `run()`메서드에 실행시킬 코드를 작성, start() 메서드로 해당 스레드를 실행
   - Thread class는 Runnable 인터페이스를 implements받은 객체이다.
   - Runnable을 구현한 객체를 선언해서 사용할 수도 있지만, 익명 클래스를 만들어서 더 많이 사용한다.
2. Thread에 Runnable를 집어넣는 대신 그 자체를 상속한 후 run()메서드를 재정의해서 사용도 가능하다.
   - 단, Runnable의 익명 클래스를 만드는 것과 같이 Thread 익명 클래스를 만들어서 더 많이 사용된다.

### 0. 기본 사용

```java
package com.main_thread;

class Go implements Runnable {
	@Override
	public void run() {
		System.out.println("러너블 클래스 출력");
	}
}

class Go2 extends Thread {
	
	@Override
	public void run() {
		System.out.println("고투 출력");
	}
}

public class Main {
	public static void main(String[] args) {
		Go go = new Go();
		Thread myThread = new Thread(go);
		myThread.start();
		
		Thread myThread2 = new Go2();
		myThread2.start();
	}
}

```

- 응용: 시계 만들기

```java
package com.clock;

import java.util.Date;

class MyClock extends Thread {
	@Override
	public void run () {
		while (true) {
			Date date = new Date();
			try {
				Thread.sleep(1000);
			} catch (Exception e) {
			}
			System.out.println(date);
		}
	}
}

public class Clock {

	public static void main(String[] args) {
		MyClock myThread = new MyClock();
		myThread.start();
	}

}

```



### 1. Runnable 인터페이스의 run() 사용

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



### 2. Thread의 run 사용

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

### 3. 우선권 확인 / 변경

- 우선권 확인
  - `thread.getPriority()`
- 우선권 변경
  - `thread.setPriority(number)`
  - 1 ~ 10
  - 기본값 5

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

- 다른 스레드가 종료될 때까지 기다렸다가 실행을 해야 하는 경우 사용

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

## 5. 스레드 동기화

멀티 스레드는 하나의 객체를 공유해서 작업할 수도 있다.

이 때, 특정 스레드 작업이 끝날 때까지 **특정 객체에 잠금을 거는 용도**로 자바는 동기화 메서드와 블록을 제공한다.

** 특정한 객체 내부에 동기화 메서드와 동기화 블록이 여러개가 있다면**, 스레드가 이들 중 하나를 실행할 때 다른 스레드는 해당 메서드는 물론이고 다른 동기화 메서드 및 블록도 실행할 수 없다.

**하지만 일반 메서드는 실행이 가능하다.**

### 1. 동기화 메서드 및 블록 선언

- 동기화 메서드 선언

  - `public synchronized void method() {}`

  - 스레드가 동기화 메소드를 실행하는 즉시 객체는 잠금이 일어나고, 메소드 실행이 끝나면 잠금이 풀린다.

- 동기화 블록 선언
  - 메소드 전체가 아닌 일부 영역을 실행할 때만 객체 잠금을 걸고 싶다면 다음과 같이 동기화 블록을 생성한다.

```java
public void method () {
    // 여러 스레드가 실행할 수 있는 영역 1
    synchronized(공유객체) {
        // 단 하나의 스레드만 실행하는 영역
    }
    // 여러 스레드가 실행할 수 있는 영역 2
}
```

- 예시

  - 하나의 Calculator 객체를 공유하는 쓰레드 클래스를 2개 만든 다음, 1 -> 2 순서로 실행시킨다.

  - 실행 순서는 다음과 같다.

    1. 동기화 메서드 시작

    2. 동기화 블록 시작 전!
       - 쓰레드 내부에서 동기화 블록을 아직 만나지 않았기 때문에, 해당 프린트는 실행된다.
    3. 5초 후 동기화 메서드 마지막의 thread1이 출력
    4. 동기화 블록 시작!
       - 동기화 메서드가 끝났기 때문에, 동기화 블록 내부로 들어간다.
    5. 2초 후 동기화 블록 마지막의 thread 2가 출력

```java
package com.sync;

// 공유할 Calculator 객체
class Calculator {
	private int memory;
	
	public int getMomory() {
		return memory;
	}
	
	public synchronized void setMemory1(int memory) {	// 동기화 메서드
		System.out.println("동기화 메서드 시작!");
		this.memory = memory;							// 메모리 값 저장
		try {
			Thread.sleep(5000);							// 5초간 정지
		} catch (InterruptedException e) {
		}
		System.out.println(Thread.currentThread().getName() + ": " + this.memory);	// 메모리 값을 읽기
	}
	
	public void setMemory2(int memory) {
		System.out.println("동기화 블록 시작 전!");
		synchronized(this) {							// 동기화 블럭
			System.out.println("동기화 블록 시작!");
			this.memory = memory;
			try {
				Thread.sleep(2000);
			} catch (InterruptedException e) {
			}
			System.out.println(Thread.currentThread().getName() + ": " + this.memory);	// 메모리 값을 읽기
		} 
		System.out.println("동기화 블록 종료!");
	}
}

// 쓰레드 클래스 2개 생성
class User1Thread extends Thread {
	private Calculator calculator;
	
	public User1Thread() {
		setName("User1Thread");
	}
	
	public void setCalculator(Calculator cal) {
		calculator = cal;
	}
	
	@Override
	public void run () {
		calculator.setMemory1(100);
	}
}

class User2Thread extends Thread {
	private Calculator calculator;
	
	public User2Thread() {
		setName("User2Thread");
	}
	
	public void setCalculator(Calculator cal) {
		calculator = cal;
	}
	
	@Override
	public void run () {
		calculator.setMemory2(50);
	}
}

public class ThreadSync {

	public static void main(String[] args) {
		
		Calculator calculator = new Calculator();
		
		User1Thread user1Thread = new User1Thread();
		user1Thread.setCalculator(calculator);
		user1Thread.start();
		
		User2Thread user2Thread = new User2Thread();
		user2Thread.setCalculator(calculator);
		user2Thread.start();
	}

}

```



### 2. wait()와 notify()를 이용한 스레드 제어

경우에 따라서는 두 개의 스레드를 교대로 번갈아 가며 실행할 때도 있다.

**정확한 교대 작업이 필요할 경우**, 자신의 작업이 끝나면 상대방 스레드를 일시 정지 상태에서 풀어주고 자신은 일시 정지 상태로 만들면 된다.

이 방법의 핵심은 특정 객체를 공유하는 데에 있으며, 하나의 객체를 두 개의 스레드가 공유하며 번갈아 동기화 메서드, 혹은 블럭을 실행하고 멈춘다.

1. notify()는 wait()에 의해 일시 정지된 스레드 중 한 개를 실행 대기 상태로 만든다.

2. wait()는 자기 자신의 스레드를 일시 정지 상태로 만든다.
3. notifyAll()은 일시 정지된 모든 스레드를 실행 대기 상태로 만든다.

단, 위 메서드들은 동기화 블럭, 혹은 동기화 메서드 내부에서만 사용 가능함에 주의!

```java
package com.sync;

// 공유할 Calculator 객체
class WorkObject {
	public synchronized void methodA ( ) {			// 동기화 메서드
		Thread thread = Thread.currentThread();
		System.out.println(thread.getName() + ": " + "methodA 작업 실행");
		notify();									// 다른 스레드들 중 하나를 실행 대기 상태로 만듦
		try {
			wait();									// 자기 스레드는 일시정지로 만듦
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	
	public synchronized void methodB () {
		Thread thread = Thread.currentThread();
		System.out.println(thread.getName() + ": " + "methodB 작업 실행");
		notify();									// 다른 스레드들 중 하나를 실행 대기 상태로 만듦
		try {
			wait();									// 자기 스레드는 일시정지로 만듦
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}

class ThreadA extends Thread {
	
	private WorkObject workObject;
	
	public ThreadA (WorkObject o) {
		setName("ThreadA");
		workObject = o;
	}
	
	@Override
	public void run() {
		for(int i=0; i <10; i++) {
			workObject.methodA();
		}
	}
}

class ThreadB extends Thread {
	
	private WorkObject workObject;
	
	public ThreadB (WorkObject o) {
		setName("ThreadB");
		workObject = o;
	}
	
	@Override
	public void run() {
		for(int i=0; i <10; i++) {
			workObject.methodB();
		}
		
	}
}

public class ThreadSync {

	public static void main(String[] args) {
		WorkObject wo = new WorkObject();	// 공유작업 객체 생성
		
		ThreadA tA = new ThreadA(wo);
		ThreadB tB = new ThreadB(wo);
		
		tA.start();
		tB.start();
	}

}

```

## 6. 스레드 종료

