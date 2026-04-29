package J0129_01;

public class Person {
	long id;
	String name;
	
	Person(){}
	Person(long id, String name){
		this.id = id;
		this.name = name;
	
	}
	
	Person(Person p){//복사생성자
		this.id = p.id;//복사생성자
		this.name = p.name;//복사생성자
	}
	
	@Override
	public String toString() {
		return String.format("%d,%s",id,name);
	}
	
	@Override
	public boolean equals(Object obj) {
		if(this.name.equals( ( (Person)obj ).name) ) {
			return true;
		}
		return false;
	}
}
