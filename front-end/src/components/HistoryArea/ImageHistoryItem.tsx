import { useNavigate } from 'react-router';
import imageIcon from '../../assets/icons/image-icon.svg';

interface ImageHistoryItemProps {
    imageId: string;
    createdAt: string;
    classification: string;
    selectedImageId?: string | undefined;
}

function formatDate(dateString: string): string {
    const date = new Date(dateString);
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    const year = String(date.getFullYear()).slice(-2);
    const hours = String(date.getHours()).padStart(2, '0');
    const minutes = String(date.getMinutes()).padStart(2, '0');

    return `${month}/${day}/${year}, ${hours}:${minutes}`;
}



export default function ImageHistoryItem({ imageId, createdAt, classification, selectedImageId }: ImageHistoryItemProps) {

    const navigate = useNavigate();

    function handleClick() {
        navigate(`/images/${imageId}`);
    }

    return (
        <div onClick={handleClick} className={`w-full bg-white border border-gray-200 rounded-lg p-3 flex flex-col justify-between shadow-sm hover:shadow-md transition-all cursor-pointer min-h-24 ${selectedImageId === imageId ? 'border-blue-500! border-2!' : ''}`}>
            <div className="flex items-start gap-3">
                <img src={imageIcon} alt="" className="w-5 h-5 mt-0.5" />
                <p className="text-sm text-gray-500">
                    {imageId}
                </p>
            </div>
            <div className="flex justify-between">
                <p className='text-xs '>
                    {classification}
                </p>

                <p className="text-sm text-gray-500">
                    {formatDate(createdAt)}
                </p>
            </div>
        </div>
    );
}