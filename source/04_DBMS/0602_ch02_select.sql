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

-- ex2) 81년도 이전에 입사한 사원의 모든필드
SELECT * FROM EMP WHERE HIREDATE < TO_DATE('81/01/01', 'YY/MM/DD');

-- ex2) 82년도 이전에 입사한 사원의 모든필드
SELECT * FROM EMP WHERE HIREDATE < TO_DATE('82/01/01', 'YY/MM/DD');






