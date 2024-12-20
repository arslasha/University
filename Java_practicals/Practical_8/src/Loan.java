public class Loan {
    private double annualInterestRate;
    private int numberOfYears;
    private double loanAmount;
    private java.util.Date loanDate;

    public Loan() {
        this(2.5, 1, 1000);
    }

    /**
     * Создает кредит с указанными: годовой процентной ставкой,
     * количеством лет и суммой кредита
     */
    public Loan(double annualInterestRate, int numberOfYears, double loanAmount) {
        // Проверка параметров на допустимость
        if (annualInterestRate <= 0) {
            throw new IllegalArgumentException("Годовая процентная ставка должна быть больше 0.");
        }
        if (numberOfYears <= 0) {
            throw new IllegalArgumentException("Количество лет должно быть больше 0.");
        }
        if (loanAmount <= 0) {
            throw new IllegalArgumentException("Сумма кредита должна быть больше 0.");
        }

        this.annualInterestRate = annualInterestRate;
        this.numberOfYears = numberOfYears;
        this.loanAmount = loanAmount;
        loanDate = new java.util.Date();
    }

    /** Возвращает годовую процентную ставку */
    public double getAnnualInterestRate() {
        return annualInterestRate;
    }

    /** Присваивает новую годовую процентную ставку */
    public void setAnnualInterestRate(double annualInterestRate) {
        if (annualInterestRate <= 0) {
            throw new IllegalArgumentException("Годовая процентная ставка должна быть больше 0.");
        }
        this.annualInterestRate = annualInterestRate;
    }

    /** Возвращает количество лет */
    public int getNumberOfYears() {
        return numberOfYears;
    }

    /** Присваивает новое количество лет */
    public void setNumberOfYears(int numberOfYears) {
        if (numberOfYears <= 0) {
            throw new IllegalArgumentException("Количество лет должно быть больше 0.");
        }
        this.numberOfYears = numberOfYears;
    }

    /** Возвращает сумму кредита */
    public double getLoanAmount() {
        return loanAmount;
    }

    /** Присваивает новую сумму кредита */
    public void setLoanAmount(double loanAmount) {
        if (loanAmount <= 0) {
            throw new IllegalArgumentException("Сумма кредита должна быть больше 0.");
        }
        this.loanAmount = loanAmount;
    }

    /** Вычисляет и возвращает ежемесячный платеж по кредиту */
    public double getMonthlyPayment() {
        double monthlyInterestRate = annualInterestRate / 1200;
        double monthlyPayment = loanAmount * monthlyInterestRate /
                (1 - (1 / Math.pow(1 + monthlyInterestRate, numberOfYears * 12)));
        return monthlyPayment;
    }

    /** Вычисляет и возвращает общую стоимость кредита */
    public double getTotalPayment() {
        return getMonthlyPayment() * numberOfYears * 12;
    }

    /** Возвращает дату взятия кредита */
    public java.util.Date getLoanDate() {
        return loanDate;
    }
}
