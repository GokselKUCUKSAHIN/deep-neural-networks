import {create2DArray} from "./array/create-2d-array";

export class Matrix {
    private readonly data: number[][];

    static create(row: number, col: number, init?: number) {
        Matrix.checkRowColNotNegative(row, col);
        return new Matrix(row, col, init);
    }

    protected constructor(row: number, col: number, init: number = 0) {
        this.data = create2DArray(row, col, init);
    }

    row(): number {
        return this.data.length;
    }

    col(): number {
        return this.data[0].length;
    }

    get(row: number, col: number): number {
        Matrix.checkRowCol(row, col, this.row(), this.col());
        return this.data[row][col];
    }

    set(row: number, col: number, value: number): void {
        Matrix.checkRowCol(row, col, this.row(), this.col());
        this.data[row][col] = value;
    }

    print(): void {
        console.table(this.data);
    }

    /* STATIC REALM */
    protected static checkRowColNotNegative(row: number, col: number): void {
        if (row < 1 || col < 1) throw Error("row or col cannot be lesser than 1!");
    }

    protected static checkRowColInRange(row: number, col: number, rRange: number, cRange: number): void {
        if (row <= rRange || col <= cRange) throw Error(`[${row}, ${col}] is Out of Range! Range is [${rRange}, ${cRange}]`);
    }

    protected static checkRowCol(row: number, col: number, rRange: number, cRange: number): void {
        Matrix.checkRowColNotNegative(row, col);
        Matrix.checkRowColInRange(row, col, rRange, cRange);
    }
}

const m = Matrix.create(5, 4);
console.log(m.row(), m.col());
m.print()