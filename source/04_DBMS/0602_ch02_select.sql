-- [II] SELECT문 - 조회 /* 여러줄 주석 */
-- 1. SELECT 문 작성법

	-- 현재 계정 (실행 CRTRL+ENTER)
	SHOW USER; 
	
	-- 현 계정이 가지고 있는 데이블들
	SELECT * FROM TAB; 
	
	-- EMP테이블의 모든 열, 모든 행
	SELECT * FROM EMP; 
	-- DEPT테이블의 모든 열, 모든 행
	SELECT * FROM DEPT; 
	-- SALGRADE테이블의 모든 열, 모든 행
	SELECT * FROM SALGRADE; 

-- 2. 특정열만 출력

	-- EMP 테이블 구조를 나타내는 ORACLE 명령
	DESC EMP;
	
	-- EMPNO, ENAME, SAL, JOB열만 모든 행 출력
	SELECT EMPNO, ENAME, SAL, JOB FROM EMP;
	
	SELECT EMPNO AS "사 번", ENAME AS "이 름", SAL AS "급 여", JOB AS "직책" FROM EMP;
	SELECT EMPNO "사 번", ENAME "이 름", SAL "급 여", JOB "직책" FROM EMP;
	SELECT EMPNO "사 번", ENAME 이름, SAL 급여, JOB FROM EMP;
	SELECT EMPNO No, ENAME ENAME, SAL SALARY FROM EMP;

-- 3. 특정 행 출력 : WHERE절(조건절) - 비교연산자 : 같다(=), 다르다(!=, ^=, <>), >, >=, <, <=

	SELECT EMPNO NO, ENAME, SAL FROM EMP WHERE SAL = 3000;
	
	-- 다르다(!=, ^=, <>) : 같은결과
	SELECT EMPNO NO, ENAME, SAL FROM EMP WHERE SAL != 3000;
	SELECT EMPNO NO, ENAME, SAL FROM EMP WHERE SAL <> 3000;
	SELECT EMPNO NO, ENAME, SAL FROM EMP WHERE SAL ^= 3000;

	-- 비교연산자 숫자, 문자, 날짜형 모두 가능
	-- ex1) 사원이름(ENAME)이 'A','B','C'로 시작하는 사원의 모든 필드
	-- A < AA < AAA < AAAA < B < C < D
	SELECT * FROM EMP WHERE ENAME < 'D';
	
	-- ex2) 82년도 이전에 입사한 사원의 모든필드
	SELECT * FROM EMP WHERE HIREDATE < TO_DATE('82/01/01', 'YY/MM/DD');

	-- ex3) 부서번호 (DEPTNO) 가 10번인 사원의 모든 필드
	SELECT * FROM EMP WHERE DEPTNO = 10;
	
	-- ex4) 이름 (ENAME 이 FORD인 직원의 EMPNO, ENAME, MGR(상사의 사번)을 출력
	SELECT EMPNO, ENAME, MGR FROM EMP WHERE ENAME = 'FORD';

	-- SQL문은 대소문자 구별없음, 데이터는 대소문자 구
	select empno, ename, mgr from emp where ename='FORD';

-- 4. 특정 행 출력 : WHERE절 (조건절) - 논리연산자 : AND, OR, NOT

	-- EX1) 급여(SAL)가 2000이상 3000이하인 직원의 모든 필드
	SELECT * FROM EMP WHERE SAL >= 2000 AND SAL <=3000;
	
	-- EX2) 82년도에 입사한 (HIREDATE) 사원의 모든 필드
	SELECT * FROM EMP WHERE HIREDATE >= '1982-01-01' AND HIREDATE <= '1982-12-31';
	
	-- 날짜 표기법 세팅(현재 : YY/MM/DD 또는 RR/MM/DD)
	
	ALTER SESSION SET NLS_DATE_FORMAT = 'YY-MM-DD';
	SELECT SYSDATE FROM DUAL;
	ALTER SESSION SET NLS_DATE_FORMAT = 'RR-MM-DD';
	SELECT SYSDATE FROM DUAL;
	
	SELECT * FROM EMP;
	SELECT TO_CHAR(HIREDATE,'YY/MM/DD') FROM EMP;
	-- 날짜 셋팅을 고려한 82년도 입사한 사원의 모든 필	
	SELECT * FROM EMP WHERE TO_CHAR(HIREDATE,'YY/MM/DD') >= '82/01/01' AND TO_CHAR(HIREDATE,'YY/MM/DD') <= '82/12/31';
	
	-- EX3) 연봉이 2400이산인 직원의 ENAME, SAL, 연봉(SAL*12)을 출력
	/*
	 * SELECT ENAME, SAL, SAL*12 AS "ANNUALSAL" 	-- (3)
		FROM EMP 								-- (1)
		WHERE ANNUALSAL >= 2400; 				-- (2) WHERE 절에는 필드의 별칭 사용 불가
	 */ 
		
	SELECT ENAME, SAL, SAL*12 AS "ANNUALSAL" -- (3)
		FROM EMP -- (1)
		WHERE SAL*12 >= 2400; -- (2)

	-- EX4) 연봉이 3000이상인 직원의 ENAME, SAL 연봉을 연봉순으로 출력
	SELECT ENAME, SAL, SAL*12 AS "ANNUALSAL" 	-- (3)
		FROM EMP 								-- (1)
		WHERE SAL*12 >= 3000 					-- (2) WHERE 절에는 필드의 별칭 사용 불가 
		ORDER BY ANNUALSAL;  					-- (4) ORDER BY 절에는 필드의 별칭 사용 가능 
		
	-- EX5) JOB이 MANAGER이거나, 10번 부서(DEPTNO) 외의 직원의 모든 필드
	SELECT * FROM EMP WHERE JOB = 'MANAGER' OR DEPTNO != 10;


-- 5. 산술연산자(SELECT절, 조건절, ORDER BY 절)
	
	-- 모든 사원의 10% 인상된 월급과 사번(EMPNO), 이름(ENAME)을 출력
	SELECT EMPNO, ENAME, SAL, SAL*1.1 FROM EMP;
	-- 모든 사원의 이름(ENAME), 월급(SAL), 상여(COMM), 연봉(SAL*12+COMM)을 출력
	SELECT ENAME, SAL, COMM, SAL*12+COMM FROM EMP;
	-- 산술연산의 결과는 NULL을 포함하면 결과도 NULL
	-- 그래서, NVL(NULL일 수도 있는 필드명, NULL을 대체할 )을 이용 - 두 매개변수의 타입이 일치 
	SELECT ENAME, SAL, COMM, NVL(COMM,0), SAL*12+NVL(COMM,0) FROM EMP;
	-- 모든사원의 사번, 이름, 상사사번 (상사가 없으면, 'CEO'로 출력) 출력 
	SELECT EMPNO, ENAME, MGR FROM EMP;
	SELECT EMPNO, ENAME, NVL(TO_CHAR(MGR), 'CEO') AS MGR FROM EMP;
	DESC EMP;
	
-- 6. 연결연산자 (||) : 필드값이나 문자를 연결 
SELECT ENAME || '은 ' || JOB AS "EMPLOYEE" FROM EMP;

-- 7. 중복제거 (DISTINCT) 
SELECT DISTINCT JOB FROM EMP;
SELECT DISTINCT DEPTNO FROM EMP;

-- 연습문제 
-- 1. emp 테이블의 구조 출력
	DESC EMP;
-- 2. emp 테이블의 모든 내용을 출력 
	SELECT * FROM EMP;
-- 3. 현 scott 계정에서 사용가능한 테이블 출력
SELECT * FROM TAB;
-- 4. emp 테이블에서 사번, 이름, 급여, 업무, 입사일 출력
SELECT EMPNO, ENAME, SAL, JOB, HIREDATE FROM EMP;
-- 5. emp 테이블에서 급여가 2000미만인 사람의 사번, 이름, 급여 출력
SELECT * FROM EMP WHERE SAL <= 2000;
-- 6. 입사일이 81/02이후에 입사한 사람의 사번, 이름, 업무, 입사일 출력
SELECT EMPNO, ENAME, SAL, JOB, HIREDATE FROM EMP WHERE TO_CHAR(HIREDATE,'YYYY/MM') >= '1981/02';
-- 7. 업무가 SALESMAN인 사람들 모든 자료 출력
SELECT * FROM EMP WHERE JOB = 'SALESMAN';
-- 8. 업무가 CLERK이 아닌 사람들 모든 자료 출력
SELECT * FROM EMP WHERE JOB != 'CLERK';
-- 9. 급여가 1500이상이고 3000이하인 사람의 사번, 이름, 급여 출력
SELECT * FROM EMP WHERE SAL >= 1500 AND SAL <=3000;
-- 10. 부서코드가 10번이거나 30인 사람의 사번, 이름, 업무, 부서코드 출력
SELECT * FROM EMP WHERE DEPTNO = '10' OR DEPTNO = '30';
-- 11. 업무가 SALESMAN이거나 급여가 3000이상인 사람의 사번, 이름, 업무, 부서코드 출력
SELECT EMPNO, ENAME, JOB, DEPTNO  FROM EMP WHERE JOB = 'SALESMAN' OR SAL >= 3000;
-- 12. 급여가 2500이상이고 업무가 MANAGER인 사람의 사번, 이름, 업무, 급여 출력
SELECT EMPNO, ENAME, JOB, SAL FROM EMP WHERE SAL >= 2500 AND MGR='MANAGER';
-- 13. “ename은 XXX 업무이고 연봉은 XX다” 스타일로 모두 출력(연봉은 SAL*12+COMM)
SELECT ename || '은 ' || JOB || ' 업무이고 연봉은 ' || (SAL*12 + NVL(COMM, 0)) || '이다. ', SAL, NVL(COMM,0)  FROM EMP;

-- 8. SQL연산자 (BETWEEN, IN, LIKE, IS NULL)
	
	SELECT * FROM EMP;
	
	-- (1) BETWEEN A AND B : A부터 B까지 (A, B 포함)
		-- EX1). SAL이 1500이상 3000이하인 직원의 사번, 이름, 급여
		SELECT EMPNO, ENAME, SAL FROM EMP WHERE SAL >= 1500 AND SAL <=3000;
		SELECT EMPNO, ENAME, SAL FROM EMP WHERE SAL BETWEEN 1500 AND 3000;
		-- SELECT EMPNO, ENAME, SAL FROM EMP WHERE SAL BETWEEN 3000 AND 1500; 이렇게 쓰면 안됨.
	
		-- EX2) SAL이 1500미만, 3000 초과
		SELECT EMPNO, ENAME, SAL FROM EMP WHERE SAL NOT BETWEEN 1500 AND 3000;
		SELECT EMPNO, ENAME, SAL FROM EMP WHERE SAL < 1500 OR SAL > 3000;
		
		-- EX3) 이름이 'A', 'B', 'C' 로 시작하는 직원의 모든 필드
		SELECT * FROM EMP WHERE ENAME BETWEEN 'A' AND 'D' AND ENAME != 'D';
		
		-- EX4) 82연도에 입사한 직원의 모든 필드
		SELECT * FROM EMP WHERE TO_CHAR(HIREDATE,'RR/MM/DD') BETWEEN '82/01/01' AND '82/12/31';
		
	-- (2) 필드명 IN (값1, 값2, 값3)
		-- EX1) 부서번호가 (DEPTNO) 가 10, 20, 40번인 직원의 모든 필드
		SELECT * FROM EMP WHERE DEPTNO = 10 OR DEPTNO = 20 OR DEPTNO = 40;
		SELECT * FROM EMP WHERE DEPTNO IN (10, 20, 40);

		-- EX2) 직책이 (JOB) MANAGER, ANALYST 직원의 모든 필드
		SELECT * FROM EMP WHERE JOB IN ('MANAGER', 'ANALYST');
		
	-- (3) 필드명 LIKE 패턴 : %(0글자 이상),  _(한글자)를 포함한 패턴
		-- EX1) 이름이 M으로 시작하는 사원의 모든 필드
		SELECT * FROM EMP WHERE ENAME LIKE 'M%';
	
		-- EX2) 이름에 N이 들어가거나 JOB에 N 이 들어가는 직원의 모든 필드
		SELECT * FROM EMP WHERE ENAME LIKE '%N%' OR JOB LIKE '%N%';
		
		-- EX3) 급여(SAL)가 5로 끝나는 사원의 모든 필드
		SELECT * FROM EMP WHERE SAL LIKE '%5';
		
		-- EX4) 82년도에 입사한 사원의 모든 필드 
		SELECT * FROM EMP WHERE HIREDATE LIKE '82%';
		
		-- EX5) 1월에 입사한 사원의 모든 필
		SELECT * FROM EMP WHERE TO_CHAR(HIREDATE,'MM') LIKE '%01%'; -- 이게 좀....
		
	-- (4) 필드 IS NULL (해당 필드가 NULL 여부)
		--EX1) 상여금(COMM) 을 받지 않는 사원의 모든 필드 
		SELECT * FROM EMP WHERE COMM = 0 OR COMM IS NULL;
		--EX2) 상여금(COMM) 을 받은 사원의 모든 필드
		SELECT * FROM EMP WHERE COMM != 0 OR COMM IS NOT NULL;
		SELECT * FROM EMP WHERE COMM != 0 OR NOT COMM IS NULL;
	

-- 9. 정렬 (오름차순, 내림차순) : ORDER BY 절
	-- SAL 기준 오름차순 정
	SELECT * FROM EMP ORDER BY SAL; 

	-- SAL 기분 오름차순 정렬 (SAL이 같으면, ENAME 오름차) 
	SELECT * FROM EMP ORDER BY SAL, ENAME; 
	
	-- SAL 기준 내림차순 정렬 
	SELECT * FROM EMP ORDER BY SAL DESC;
	
	-- SAL 기분 내림차순 정렬 (SAL이 같으면, HIREDATE 내림차순) 
	SELECT * FROM EMP ORDER BY SAL DESC, HIREDATE DESC; 
	
	
-- 연습문제 전 형변환 함수 : TO_CHAR, TO_DATE
-- 날짜형(HIREDATE)을 문자영으로 변환 : TO_CHAR(날자형데이터, 패턴)
	-- YYYY, YY, RR : 연도 / MM : 월 / DD : 일 / DY 월 / DAY 월요일
	-- HH24, HH12, HH : 시 / AM이나 PM / MI : 분 / SS : 초
	
	SELECT ENAME, TO_CHAR(HIREDATE, 'YY/MM/DD AM HH12:MI:SS') FROM EMP;
	
	-- 82년도전에 입사한 사원의 데이터 
	SELECT * FROM EMP WHERE TO_CHAR(HIREDATE,'RR/MM/DD') < '82/01/01';
	SELECT * FROM EMP WHERE HIREDATE < TO_DATE('82/01/01','RR/MM/DD');
	
	
-- <총 연습문제>
--1. EMP 테이블에서 sal이 3000이상인 사원의 empno, ename, job, sal을 출력
SELECT empno, ename, job, sal FROM EMP WHERE SAL >= 3000;
--2. EMP 테이블에서 empno가 7788인 사원의 ename과 deptno를 출력
SELECT empno, deptno FROM EMP WHERE empno = 7788;
--3. 연봉(SAL*12+COMM)이 24000이상인 사번, 이름, 급여 출력 (급여순정렬)
SELECT EMPNO, ENAME, SAL, (SAL*12+NVL(COMM,0)) AS "연봉" FROM EMP ORDER BY 연봉 DESC; 
--4. 입사일이 1981년 2월 20과 1981년 5월 1일 사이에 입사한 사원의 사원명, 직책, 입사일을 출력 (단 hiredate 순으로 출력)
SELECT ENAME, DEPTNO , HIREDATE FROM EMP WHERE TO_CHAR(HIREDATE,'YYYY-MM-DD') BETWEEN '1981-02-20' AND '1981-05-01' ORDER BY HIREDATE ;
--5. deptno가 10,20인 사원의 모든 정보를 출력 (단 ename순으로 정렬)
SELECT * FROM EMP WHERE DEPTNO IN (10,20) ORDER BY ENAME;
--6. sal이 1500이상이고 deptno가 10,30인 사원의 ename과 sal를 출력 (단 출력되는 결과의 타이틀을 employee과 Monthly Salary로 출력)
SELECT ENAME AS "employee과", SAL AS "Monthly Salary" FROM EMP WHERE SAL >= 1500 AND DEPTNO IN (10,30);
--7. hiredate가 1982년인 사원의 모든 정보를 출력
SELECT * FROM EMP WHERE TO_CHAR(HIREDATE,'YYYY') = '1982';
--8. 이름의 첫자가 C부터  P로 시작하는 사람의 이름, 급여 이름순 정렬
SELECT ENAME, SAL FROM EMP WHERE ENAME BETWEEN 'C' AND 'Q' AND ENAME != 'Q';
--9. comm이 sal보다 10%가 많은 모든 사원에 대하여 이름, 급여, 상여금을 출력하는 SELECT 문을 작성
SELECT ENAME, SAL, (SAL * 1.1) , NVL(COMM,0)  FROM EMP WHERE COMM > SAL * 1.1;
--10. job이 CLERK이거나 ANALYST이고 sal이 1000,3000,5000이 아닌 모든 사원의 정보를 출력
SELECT * FROM EMP WHERE JOB IN ('CLERK','ANALYST') AND NOT SAL IN (1000,3000,5000);
--11. ename에 L이 두 자가 있고 deptno가 30이거나 또는 mgr이 7782인 사원의 모든 정보를 출력하는 SELECT 문을 작성하여라.
SELECT * FROM EMP WHERE  (DEPTNO = 30 OR MGR = 7782) AND ENAME LIKE '%L%L%';
--12. 입사일이 81년도인 직원의 사번, 사원명, 입사일, 업무, 급여를 출력
SELECT EMPNO, ENAME, HIREDATE, JOB, SAL FROM EMP WHERE TO_CHAR(HIREDATE, 'YY') = '82';
--13. 입사일이81년이고 업무가 'SALESMAN'이 아닌 직원의 사번, 사원명, 입사일, 업무, 급여를 검색하시오.
SELECT EMPNO, ENAME, HIREDATE, JOB, SAL FROM EMP WHERE TO_CHAR(HIREDATE, 'YY') = '81' AND NOT JOB='SALESMAN';
--14. 사번, 사원명, 입사일, 업무, 급여를 급여가 높은 순으로 정렬하고, 급여가 같으면 입사일이 빠른 사원으로 정렬하시오.
SELECT EMPNO, ENAME, HIREDATE, JOB, SAL FROM EMP ORDER BY SAL DESC, HIREDATE ASC;
--15. 사원명의 세 번째 알파벳이 'N'인 사원의 사번, 사원명을 검색하시오
SELECT EMPNO, ENAME FROM EMP WHERE ENAME LIKE '__N%';
--16. 사원명에 'A'가 들어간 사원의 사번, 사원명을 출력
SELECT EMPNO, ENAME FROM EMP WHERE ENAME LIKE '%A%';
--17. 연봉(SAL*12)이 35000 이상인 사번, 사원명, 연봉을 검색 하시오.
SELECT EMPNO "사번", ENAME "사원명", (SAL*12) AS "연봉" FROM EMP WHERE (SAL*12) > 3500 ORDER BY 연봉 DESC;