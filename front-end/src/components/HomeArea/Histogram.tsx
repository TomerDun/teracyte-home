import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from 'recharts';
import { transformHistogramData } from '../../services/histogramUtils';

interface HistogramProps {
    histogram: number[];
}

export default function Histogram({ histogram }: HistogramProps) {
    const data = transformHistogramData(histogram);

    return (
        <div className="bg-white border border-gray-200 rounded-md w-full h-full p-4">
            <h3 className="text-base font-medium mb-2">Intensity Histogram</h3>
            <ResponsiveContainer width="100%" height="90%">
                <BarChart data={data}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#e5e7eb" />
                    <XAxis 
                        dataKey="intensity" 
                        label={{ value: 'Intensity', position: 'insideBottom', offset: -5 }}
                        tick={{ fontSize: 12 }}
                    />
                    <YAxis 
                        label={{ value: 'Frequency', angle: -90, position: 'insideLeft' }}
                        tick={{ fontSize: 12 }}
                    />
                    <Tooltip 
                        contentStyle={{ 
                            backgroundColor: 'white', 
                            border: '1px solid #e5e7eb',
                            borderRadius: '6px'
                        }}
                    />
                    <Bar dataKey="count" fill="#3b82f6" />
                </BarChart>
            </ResponsiveContainer>
        </div>
    );
}
