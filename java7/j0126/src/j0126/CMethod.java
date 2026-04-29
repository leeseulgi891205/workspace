package j0126;

public class CMethod {
//	CMethod(){} //기본생성자

	int[] method(int num) {
		int a = 10;
		int[] arr = {1,2,3};
		// 입력받은 숫자를 곱함.
		for(int i=0;i<arr.length;i++) {
			arr[i] = arr[i]*num;
		}
		return arr;
	}
}
