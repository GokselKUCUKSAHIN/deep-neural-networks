import {createArray} from "./create-array";

export function create2DArray(row: number, col: number, value = 0) {
    return createArray(row).map(_ => createArray(col, value));
}