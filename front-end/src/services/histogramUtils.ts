/**
 * Transform histogram array data to Recharts-compatible format
 * 
 * @param histogram - Array of frequency counts (256 values for 0-255 intensity)
 * @returns Array of objects with intensity and count properties
 */
export function transformHistogramData(histogram: number[]) {
    return histogram.map((count, index) => ({
        intensity: index,
        count: count
    }));
}
