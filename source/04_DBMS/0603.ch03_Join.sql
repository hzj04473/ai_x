-- [ III ] join : 2개 이상의 테이블을 연결하여 데이터를 검색하는 방법
-- 1행 
SELECT * FROM EMP WHERE ENAME='SCOTT';
-- 4행 
SELECT * FROM DEPT;

-- CROSS JOIN
	-- 1개 (EMP갯수) * 4개 (DEPT갯수) = 4
	SELECT *
		FROM EMP, DEPT
		WHERE ENAME='SCOTT';

-----------------------------------------------------------------------
-- ★ 1. EQUI JOIN : 동일한 컬럼을 기준으로 조인 (공통필드 값이 일치되는 조건만 JOIN)
-----------------------------------------------------------------------

SELECT * 
	FROM EMP, DEPT 
	WHERE ENAME='SCOTT' AND EMP.DEPTNO = DEPT.DEPTNO;

SELECT EMPNO AS "NO", ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPT.DEPTNO, DNAME, LOC 
	FROM EMP, DEPT 
	WHERE ENAME='SCOTT' AND EMP.DEPTNO = DEPT.DEPTNO;

SELECT EMPNO AS "NO", ENAME, JOB, MGR, HIREDATE, SAL, COMM, D.DEPTNO, DNAME, LOC 	-- (3)
	FROM EMP E, DEPT D																-- (1)
	WHERE ENAME='SCOTT' AND E.DEPTNO = D.DEPTNO										-- (2) 테이블 별칭만 사용 가
	ORDER BY NO;																	-- (4)
	
	-- ex1) 모든 사원의 사번, 이름, JOB, 상사번호, 부서번호, 부서명, 근무지
	SELECT EMPNO, ENAME, JOB, MGR, D.DEPTNO, DNAME, LOC 
		FROM EMP E, DEPT D
		WHERE E.DEPTNO = D.DEPTNO;
	
	-- ex2) 급여(SAL) 가 2000이상만 직원의 이름, JOB, 급여, 부서명, 근무
	SELECT ENAME , JOB, SAL, DNAME, LOC 
		FROM EMP E, DEPT D
		WHERE E.DEPTNO = D.DEPTNO AND SAL>2000;
	
	--ex3) 근무지(LOC)가 'CHICAGO'인 직원의 이름, JOB, 급여, 부서번호 출력
	SELECT ENAME, JOB, SAL, E.DEPTNO 
		FROM EMP E, DEPT D 
		WHERE E.DEPTNO = D.DEPTNO AND LOC ='CHICAGO';
	
	-- ex4) 82년도 입사한 10,20번 부서직원의 이름, 급여, 근무지(급여순) 출력
	SELECT E.ENAME , E.SAL, D.LOC
		FROM EMP E, DEPT D 
		WHERE TO_CHAR(E.HIREDATE,'RR') = '82' 
			AND E.DEPTNO IN (10,20)
		ORDER BY E.SAL DESC;
	
	-- ex5) JOB이 'SALESMAN'이거나 'MANAGER'인 사원의 
	-- 이름, 급여, 상여, 연봉(SAL+COMM)*12, 부서명, 근무지(연봉이 큰 순) 출력 
	SELECT ENAME, SAL, COMM, (SAL + NVL(COMM,0))*12 AS "연봉", DNAME, LOC 
		FROM EMP E, DEPT D 
		WHERE E.DEPTNO = D.DEPTNO AND JOB IN ('SALES','MANAGER')
		ORDER BY 연봉 DESC;
	
	-- ex6) COMM 이 NULL 이고, SAL 2000대인 사원의 이름, 급여, 입시일, 부서번호, 부서명
	-- 부서명순, 급여순 정렬
	SELECT * 
		FROM EMP E, DEPT D 
		WHERE E.DEPTNO = D.DEPTNO AND E.COMM IS NULL AND SAL BETWEEN 2000 AND 2999
		ORDER BY D.DEPTNO DESC, E.SAL DESC;
	
	
	-- 탄탄 다지기
	-- 탄탄1) 뉴욕에서 근무하는 사원의 이름과 급여를 출력하시오
	SELECT ENAME, SAL
		FROM EMP E, DEPT D 
		WHERE E.DEPTNO = D.DEPTNO AND D.LOC ='NEW YORK';
	-- 탄탄2) ACCOUNTING 부서 소속 사원의 이름과 입사일을 출력하시오
	SELECT ENAME, HIREDATE
		FROM EMP E, DEPT D 
		WHERE E.DEPTNO = D.DEPTNO AND D.DNAME ='ACCOUNTING';
	-- 탄탄3) 직급이 MANAGER인 사원의 이름, 부서명을 출력하시오
	SELECT ENAME, DNAME 
		FROM EMP E, DEPT D 
		WHERE E.DEPTNO = D.DEPTNO AND E.JOB = 'MANAGER';
	-- 탄탄4) Comm이 null이 아닌 사원의 이름, 급여, 부서코드, 근무지를 출력하시오.
	SELECT ENAME, SAL, E.DEPTNO, LOC 
		FROM EMP E, DEPT D 
		WHERE E.DEPTNO = D.DEPTNO AND E.COMM IS NOT NULL;

-----------------------------------------------------------------------	
-- ★ 2. Non-Equi Join : 동일한 컬럼없이 다른 조건을 사용하여 조인
-----------------------------------------------------------------------
	
-- 직원정보
SELECT * FROM EMP WHERE ENAME = 'SCOTT';
-- 급여등급 정보
SELECT * FROM SALGRADE;
	
SELECT * 
	FROM EMP, SALGRADE 
	WHERE ENAME = 'SCOTT' AND SAL BETWEEN LOSAL AND HISAL;

	-- ex1) 모든 사원의 사번, 이름, JOB, 상사사번, 급여, 급여등급(1등급,2등급...)
	SELECT ENAME, JOB, MGR, SAL, GRADE || '듭급' AS "GRADE"
		FROM EMP, SALGRADE 
		WHERE SAL BETWEEN LOSAL AND HISAL ;

	-- ex2) 모든 사원의 사번, 이름, JOB, 상사사번, 급여, 급여등급, 부서명
	SELECT ENAME, JOB, MGR, SAL, GRADE || '듭급' AS "GRADE", DNAME
		FROM EMP E, SALGRADE S, DEPT D
		WHERE SAL BETWEEN LOSAL AND HISAL AND E.DEPTNO  = D.DEPTNO;


	-- 탄탄다지기 연습문제
	-- 탄탄1) Comm이 null이 아닌 사원의 이름, 급여, 등급, 부서번호, 부서이름, 근무지를 출력하시오.
	SELECT ENAME, JOB, MGR, SAL, GRADE || '듭급' AS "GRADE", D.DEPTNO ,  DNAME
		FROM EMP E, SALGRADE S, DEPT D
		WHERE SAL BETWEEN LOSAL AND HISAL AND E.DEPTNO  = D.DEPTNO AND E.COMM IS NOT NULL;
	-- 탄탄2) 이름, 급여, 입사일, 급여등급
	SELECT ENAME, SAL, HIREDATE, GRADE 
		FROM EMP E, SALGRADE
		WHERE SAL BETWEEN LOSAL AND HISAL;
	-- 탄탄3) 이름, 급여, 급여등급, 연봉, 부서명을 부서명순으로 정렬하여 출력. 부서가 같으면 연봉순. 연봉=(sal+comm)*12 comm이 null이면 0
	SELECT ENAME, SAL, GRADE, (SAL+NVL(COMM, 0)), D.DNAME 
		FROM EMP E, SALGRADE S, DEPT D
		WHERE E.SAL BETWEEN S.LOSAL AND S.HISAL AND E.DEPTNO  = D.DEPTNO AND E.COMM IS NOT NULL ORDER BY D.DNAME , (SAL+NVL(COMM, 0));
	-- 탄탄4) 이름, 업무, 급여, 등급, 부서코드, 부서명 출력. 급여가 1000~3000사이. 정렬조건 : 부서별, 부서같으면 업무별, 업무같으면 급여 큰순
	SELECT ENAME, JOB, SAL, GRADE || '듭급' AS "GRADE", D.DEPTNO , DNAME
		FROM EMP E, SALGRADE S, DEPT D
		WHERE SAL BETWEEN LOSAL AND HISAL AND SAL BETWEEN '1000' AND '3000' AND E.DEPTNO  = D.DEPTNO
		ORDER BY DNAME, SAL DESC;
	-- 탄탄5) 이름, 급여, 등급, 입사일, 근무지. 81년에 입사한 사람. 등급 큰순
	SELECT ENAME, SAL, GRADE, E.HIREDATE, D.LOC , D.DEPTNO , DNAME
		FROM EMP E, SALGRADE S, DEPT D
		WHERE TO_CHAR(HIREDATE, 'RR') = '81'  AND E.DEPTNO  = D.DEPTNO
		ORDER BY GRADE DESC;

-----------------------------------------------------------------------
-- ★ 3. Self Join : 한 테이블 내에서 조인.
-----------------------------------------------------------------------
	
-- 직원정보
SELECT * FROM EMP WHERE ENAME = 'SMITH';
-- SMITH 상사 정
SELECT EMPNO, ENAME FROM EMP WHERE EMPNO = 7902;

-- 한테이블...
SELECT WORKER.EMPNO, WORKER.ENAME, WORKER.MGR, MANAGER.EMPNO ,MANAGER.ENAME 
	FROM EMP WORKER, EMP MANAGER
	WHERE WORKER.ENAME = 'SMITH' AND WORKER.MGR = MANAGER.EMPNO;

	-- ex1) 모든 사원의 사번, 이름, 상사의 사번, 상사이름
	SELECT W.EMPNO, W.ENAME, W.MGR ,M.ENAME AS "MANAGERNAME"
		FROM EMP W, EMP M
		WHERE W.MGR = M.EMPNO;
	
	-- ex2) SMITH의 상사는 JONES 이다. 포멧으로 출력 
	SELECT W.ENAME || '의 상사는 ' || M.ENAME || '이다.'
		FROM EMP W, EMP M
		WHERE W.MGR = M.EMPNO;


	-- 탄탄 다지기
	-- 탄탄1) 매니저가 KING인 사원들의 이름과 직급을 출력하시오.
	SELECT WORKER.ENAME, WORKER.JOB
	FROM EMP WORKER, EMP MANAGER
	WHERE WORKER.MGR=MANAGER.EMPNO AND MANAGER.ENAME='KING';
	
	-- 서브쿼리 이용 시작
	SELECT EMPNO FROM EMP WHERE ENAME = 'KING'; -- SELF JOIN 이
	SELECT EMPNO, JOB FROM EMP WHERE MGR = (SELECT EMPNO FROM EMP WHERE ENAME = 'KING');
	-- 서브쿼리 이용 
	
	-- 탄탄2) SCOTT과 동일한 부서번호에서 근무하는 사원의 이름을 출력하시오
	SELECT MANAGER.ENAME
		FROM EMP WORKER, EMP MANAGER
		WHERE WORKER.DEPTNO =MANAGER.DEPTNO AND WORKER.ENAME='SCOTT' AND NOT MANAGER.ENAME = 'SCOTT';
	
	-- 탄탄3) SCOTT과 동일한 근무지에서 근무하는 사원의 이름을 출력하시오(2단계 최종문제) – 6장 수업후 subquery 사용 추천
	--	SELECT DEPTNO FROM EMP WHERE ENAME ='SMITH';
	SELECT ENAME 
		FROM EMP 
		WHERE DEPTNO = (SELECT DEPTNO FROM EMP WHERE ENAME ='SMITH') AND ENAME !='SCOTT';

-----------------------------------------------------------------------
-- ★ 4. Outer Join : 조인 조건에 만족하지 않는 행도 나타나는 조
-- Self join, Equi join 시 소전이 만족하지 않는 행까지 나타나게 하는 JOIN
-----------------------------------------------------------------------
-- 배제된 행을 결과에 포함시킬 경우 +기호를 정보가 부족한 컬럼이름 뒤에 덧붙	
-- (1) selef join 에서의 OUTER JOIN
SELECT W.EMPNO, W.ENAME, W.MGR ,M.ENAME
		FROM EMP W, EMP M
		WHERE W.MGR = M.EMPNO(+);
	-- ex1) 모든 사원에 대해 'SMITH'의 상사는 FORD다' ... 'KING의 상사는 없다'
	SELECT W.ENAME || '의 상사는 ' || NVL(M.ENAME,'없') || '다' AS "MESSAGE"
		FROM EMP W, EMP M
		WHERE W.MGR = M.EMPNO(+)
	
	-- 말단 직원 
	SELECT M.ENAME
		FROM EMP W, EMP M
		WHERE W.MGR(+) = M.EMPNO AND W.ENAME IS NULL;
		
-- EQUI JOIN 에서의 OUTER JOIN
-- 10, 20, 30, 40
SELECT * FROM DEPT;
-- 10, 20, 30
SELECT * FROM EMP;
		
SELECT ENAME, E.DEPTNO, DNAME 
	FROM EMP E, DEPT D
	WHERE E.DEPTNO(+) = D.DEPTNO;



-- (2)

-- ★ < 연습문제>
-- Part1
--1. 모든 사원에 대한 이름, 부서번호, 부서명을 출력하는 SELECT 문장을 작성하여라.
SELECT ENAME, E.DEPTNO, DNAME  FROM EMP E, DEPT D WHERE E.DEPTNO = D.DEPTNO;
--2. NEW YORK에서 근무하고 있는 사원에 대하여 이름, 업무, 급여, 부서명을 출력
SELECT ENAME, JOB, SAL, DNAME, LOC  FROM EMP E, DEPT D WHERE E.DEPTNO = D.DEPTNO AND D.LOC ='NEW YORK';
--3. 보너스를 받는 사원에 대하여 이름,부서명,위치를 출력
SELECT ENAME, DNAME, LOC  FROM EMP E, DEPT D WHERE E.DEPTNO = D.DEPTNO AND COMM > 0;
--4. 이름 중 L자가 있는 사원에 대하여 이름,업무,부서명,위치를 출력
SELECT ENAME, JOB, DNAME, LOC FROM EMP E, DEPT D WHERE E.DEPTNO = D.DEPTNO AND ENAME LIKE '%L%';
--5. 사번, 사원명, 부서코드, 부서명을 검색하라(단, 사원명기준으로 오름차순 정렬)
SELECT EMPNO, ENAME, E.DEPTNO, D.DNAME FROM EMP E, DEPT D WHERE E.DEPTNO = D.DEPTNO ORDER BY E.ENAME;
--6. 사번, 사원명, 급여, 부서명을 검색하라. 
--단 급여가 2000이상인 사원에 대하여 급여를 기준으로 내림차순으로 정렬하시오
SELECT EMPNO, ENAME, SAL, D.DNAME FROM EMP E, DEPT D WHERE SAL BETWEEN '2000' AND '2999' AND E.DEPTNO = D.DEPTNO ORDER BY SAL DESC;
--7. 사번, 사원명, 업무, 급여, 부서명을 검색하시오. 단 업무가 MANAGER이며 급여가 2500이상인
-- 사원에 대하여 사번을 기준으로 오름차순으로 정렬하시오.
SELECT EMPNO, ENAME, JOB, SAL, D.DNAME FROM EMP E, DEPT D WHERE JOB = 'MANAGER' AND SAL > 2500 AND E.DEPTNO = D.DEPTNO ORDER BY EMPNO;
--8. 사번, 사원명, 업무, 급여, 등급을 검색하시오(단, 급여기준 내림차순으로 정렬)
SELECT EMPNO, ENAME, JOB, SAL, S.GRADE FROM EMP E, SALGRADE S WHERE SAL BETWEEN S.LOSAL AND S.HISAL ORDER BY SAL DESC;




-- Part2
--1. 이름, 직속상사명
SELECT W.ENAME, M.ENAME AS "MANAGER_NAME" FROM EMP W, EMP M WHERE W.MGR = M.EMPNO ;

--2. 이름, 급여, 업무, 직속상사명
SELECT W.ENAME, W.SAL, W.JOB, M.ENAME AS "MANAGER_NAME" FROM EMP W, EMP M WHERE W.MGR = M.EMPNO ;
--3. 이름, 급여, 업무, 직속상사명 . (상사가 없는 직원까지 전체 직원 다 출력.
-- 상사가 없을 시 '없음'으로 출력)
SELECT W.ENAME, W.SAL, W.JOB, NVL(M.ENAME,'없음') AS "MANAGER_NAME" FROM EMP W, EMP M WHERE W.MGR = M.EMPNO(+) ;
--4. 이름, 급여, 부서명, 직속상사명
SELECT W.ENAME, W.SAL, D.DNAME, NVL(M.ENAME,'없음') AS "MANAGER_NAME" 
	FROM EMP W,
	EMP M,
	DEPT D
	WHERE
	W.MGR = M.EMPNO
	AND W.DEPTNO = D.DEPTNO
	AND M.DEPTNO = D.DEPTNO;
--5. 상사가 없는 직원과 상사가 있는 직원 모두에 대해 이름, 급여, 부서코드, 부서명, 근무지, 직속상사명을 출력하시오(단, 직속상사가 없을 경우 직속상사명에는 ‘없음’으로 대신 출력하시오)
SELECT W.ENAME, W.SAL, D.DEPTNO ,D.DNAME, D.LOC , NVL(M.ENAME,'없음') AS "MANAGER_NAME" 
	FROM EMP W, EMP M, DEPT D 
	WHERE W.MGR = M.EMPNO(+) AND W.DEPTNO = D.DEPTNO(+);	
--6. 이름, 급여, 등급, 부서명, 직속상사명. 급여가 2000이상인 사람
SELECT W.ENAME, W.SAL, S.GRADE ,D.DEPTNO ,D.DNAME, D.LOC , NVL(M.ENAME,'없음') AS "MANAGER_NAME" 
	FROM EMP W, EMP M, DEPT D, SALGRADE S
	WHERE W.MGR = M.EMPNO(+) AND W.DEPTNO = D.DEPTNO(+) AND W.SAL BETWEEN S.LOSAL AND S.HISAL ;

--7. 이름, 급여, 등급, 부서명, 직속상사명, (직속상사가 없는 직원까지 전체직원 부서명 순 정렬)
SELECT W.ENAME, W.SAL, S.GRADE , D.DNAME, NVL(M.ENAME,'없음') AS "MANAGER_NAME" 
	FROM EMP W, EMP M, SALGRADE S, DEPT D
	WHERE W.MGR = M.EMPNO(+) AND W.SAL BETWEEN S.LOSAL AND S.HISAL AND W.DEPTNO = D.DEPTNO;
--8. 이름, 급여, 등급, 부서명, 연봉, 직속상사명. 연봉=(급여+comm)*12으로 계산 
SELECT W.ENAME, W.SAL, S.GRADE, D.DNAME, (W.SAL+NVL(W.COMM,0)*12) AS "YEARSAL", NVL(M.ENAME,'없음') AS "MANAGER_NAME" 
	FROM EMP W, EMP M, SALGRADE S, DEPT D
	WHERE W.MGR = M.EMPNO(+) AND W.SAL BETWEEN S.LOSAL AND S.HISAL AND W.DEPTNO = D.DEPTNO;
--9. 8번을 부서명 순 부서가 같으면 급여가 큰 순 정렬
SELECT W.ENAME, W.SAL, S.GRADE, D.DNAME, (W.SAL+NVL(W.COMM,0)*12) AS "YEARSAL", NVL(M.ENAME,'없음') AS "MANAGER_NAME" 
	FROM EMP W, EMP M, SALGRADE S, DEPT D
	WHERE W.MGR = M.EMPNO(+) AND W.SAL BETWEEN S.LOSAL AND S.HISAL AND W.DEPTNO = D.DEPTNO ORDER BY DNAME, YEARSAL DESC;
--10. 사원테이블에서 사원명, 사원의 상사를 검색하시오(상사가 없는 직원까지 전체).
SELECT W.ENAME, NVL(M.ENAME,'없음') AS "MANAGER_NAME" 
	FROM EMP W, EMP M
	WHERE W.MGR = M.EMPNO(+);
--11. 사원명, 상사명, 상사의 상사명을 검색하시오(self join)
--SELECT W.ENAME, M.ENAME
--	FROM EMP W, EMP M, EMP MM
--	WHERE  W.ENAME = M.ENAME AND W.ENAME = MM.ENAME;
--12. 위의 결과에서 상위 상사가 없는 모든 직원의 이름도 출력되도록 수정하시오(outer join)
--SELECT W.ENAME
--	FROM EMP W, EMP M
--	WHERE W.MGR = M.EMPNO(+) AND M.ENAME IS NULL;

  --11. 사원명, 상사명, 상사의 상사명을 검색하시오
SELECT W.ENAME WORKER, M.ENAME MANAGER, MM.ENAME TOPMANAGER
  FROM EMP W, EMP M, EMP MM
  WHERE W.MGR=M.EMPNO AND M.MGR=MM.EMPNO;
  
  --12. 위의 결과에서 상위 상사가 없는 모든 직원의 이름도 출력되도록 수정하시오
SELECT W.ENAME WORKER, M.ENAME MANAGER, MM.ENAME TOPMANAGER
  FROM EMP W, EMP M, EMP MM
  WHERE W.MGR=M.EMPNO(+) AND M.MGR=MM.EMPNO(+);
