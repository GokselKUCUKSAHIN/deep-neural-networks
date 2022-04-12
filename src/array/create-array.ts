export function createArray(size: number, value = 0): number[] {
    return [...Array(size)].fill(value);
}